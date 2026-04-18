from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define o local do arquivo do banco de dados na raiz do projeto
SQLALCHEMY_DATABASE_URL = "sqlite:///./raizes_nordeste.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Função para obter uma conexão e fechar depois do uso
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()