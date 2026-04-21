from fastapi import FastAPI
from database import engine, Base
from routers import alunos, professores, disciplinas

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Universidade",
    description="Sistema de cadastro de alunos, professores e disciplinas",
    version="1.0.0"
)

app.include_router(alunos.router)
app.include_router(professores.router)
app.include_router(disciplinas.router)

@app.get("/")
def inicio():
    return {"mensagem": "API Universidade funcionando!"}