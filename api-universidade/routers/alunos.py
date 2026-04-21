from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models, schemas

router = APIRouter(prefix="/alunos", tags=["Alunos"])

# Listar todos
@router.get("/", response_model=list[schemas.AlunoResponse])
def listar_alunos(db: Session = Depends(get_db)):
    return db.query(models.Aluno).all()

# Buscar por ID
@router.get("/{id}", response_model=schemas.AlunoResponse)
def buscar_aluno(id: int, db: Session = Depends(get_db)):
    aluno = db.query(models.Aluno).filter(models.Aluno.id == id).first()
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return aluno

# Cadastrar
@router.post("/", response_model=schemas.AlunoResponse)
def cadastrar_aluno(aluno: schemas.AlunoCreate, db: Session = Depends(get_db)):
    novo = models.Aluno(**aluno.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

# Editar
@router.put("/{id}", response_model=schemas.AlunoResponse)
def editar_aluno(id: int, dados: schemas.AlunoCreate, db: Session = Depends(get_db)):
    aluno = db.query(models.Aluno).filter(models.Aluno.id == id).first()
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    for key, value in dados.dict().items():
        setattr(aluno, key, value)
    db.commit()
    db.refresh(aluno)
    return aluno

# Deletar
@router.delete("/{id}")
def deletar_aluno(id: int, db: Session = Depends(get_db)):
    aluno = db.query(models.Aluno).filter(models.Aluno.id == id).first()
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    db.delete(aluno)
    db.commit()
    return {"mensagem": "Aluno deletado com sucesso"}