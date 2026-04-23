import uuid
from datetime import datetime, timezone
import jwt
from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel 
from src.api.routes import pedido_routes
from src.infrastructure.database.database import engine, Base
from src.infrastructure.database import models 

SECRET_KEY = "raizes_nordeste_secret"
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class LoginSchema(BaseModel):
    username: str
    password: str

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Raízes do Nordeste - API",
    description="Sistema de gestão multicanal com integração de pagamento Mock, Banco de Dados e Segurança JWT.",
    version="1.2.0"
)

@app.middleware("http")
async def add_request_id(request: Request, call_next):
    request.state.request_id = str(uuid.uuid4())
    response = await call_next(request)
    return response

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    detalhes = []
    for erro in exc.errors():
        campo = erro["loc"][-1] if erro["loc"] else "desconhecido"
        detalhes.append({"field": str(campo), "issue": erro["msg"]})

    return JSONResponse(
        status_code=422,
        content={
            "error": "UNPROCESSABLE_ENTITY",
            "message": "Erro de validação nos dados enviados.",
            "details": detalhes,
            "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "path": request.url.path,
            "requestId": getattr(request.state, "request_id", "N/A")
        }
    )

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": f"ERROR_{exc.status_code}",
            "message": exc.detail,
            "details": [],
            "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "path": request.url.path,
            "requestId": getattr(request.state, "request_id", "N/A")
        }
    )


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")

@app.post("/token", tags=["Segurança"], include_in_schema=False)
async def login_token(form_data: OAuth2PasswordRequestForm = Depends()):
    return {
        "access_token": jwt.encode({"sub": form_data.username, "perfil": "ADMIN"}, SECRET_KEY, algorithm=ALGORITHM),
        "token_type": "bearer"
    }

@app.post("/auth/login", tags=["Segurança"], summary="Autenticação de Usuário")
async def login_rota_professor(dados: LoginSchema):
    if dados.username == "admin" and dados.password == "admin":
        token = jwt.encode({"sub": dados.username, "perfil": "ADMIN"}, SECRET_KEY, algorithm=ALGORITHM)
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Usuário ou senha incorretos")


app.include_router(pedido_routes.router, prefix="/pedidos", dependencies=[Depends(get_current_user)])

@app.get("/", tags=["Home"])
def home():
    return {"mensagem": "API Raízes do Nordeste ativa, operante e protegida!"}

@app.get("/produtos", tags=["Produtos"])
def listar_produtos():
    return [
        {"id": 1, "nome": "Cuscuz com Manteiga", "preco_unitario": 15.0, "categoria": "Cuscuz"},
        {"id": 2, "nome": "Tapioca de Carne Seca", "preco_unitario": 22.0, "categoria": "Tapioca"}
    ]

@app.get("/estoque/{unidade_id}", tags=["Estoque"])
def consultar_estoque(unidade_id: int):
    if unidade_id == 10:
        return {
            "unidade_id": 10,
            "itens": [
                {"produto_id": 1, "quantidade": 50},
                {"produto_id": 2, "quantidade": 30}
            ]
        }
    raise HTTPException(status_code=404, detail="Unidade não encontrada")