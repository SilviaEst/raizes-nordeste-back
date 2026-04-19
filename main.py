from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from src.api.routes import pedido_routes
from src.infrastructure.database.database import engine, Base
from src.infrastructure.database import models 
import jwt 

SECRET_KEY = "raizes_nordeste_secret"
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Raízes do Nordeste - API",
    description="Sistema de gestão multicanal com integração de pagamento Mock, Banco de Dados e Segurança JWT.",
    version="1.1.0"
)

@app.post("/token", tags=["Segurança"])
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    
    return {
        "access_token": jwt.encode({"sub": form_data.username, "perfil": "ADMIN"}, SECRET_KEY, algorithm=ALGORITHM),
        "token_type": "bearer"
    }

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")

app.include_router(pedido_routes.router, prefix="/pedidos", dependencies=[Depends(get_current_user)])

@app.get("/", tags=["Home"])
def home():
    return {"mensagem": "API Raízes do Nordeste ativa, operante e protegida!"}


@app.get("/produtos", tags=["Produtos"])
def listar_produtos():
    return [
        {"id": 1, "nome": "Cuscuz com Manteiga", "preco_base": 15.0, "categoria": "Cuscuz"},
        {"id": 2, "nome": "Tapioca de Carne Seca", "preco_base": 22.0, "categoria": "Tapioca"}
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