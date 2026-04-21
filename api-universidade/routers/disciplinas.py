from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models, schemas

router = APIRouter(prefix="/disciplinas", tags=["Disciplinas"])

# Listar todas
@router.get("/", response_model=list[schemas.DisciplinaResponse])
def listar_disciplinas(db: Session = Depends(get_db)):
    return db.query(models.Disciplina).all()

# Buscar por ID
@router.get("/{id}", response_model=schemas.DisciplinaResponse)
def buscar_disciplina(id: int, db: Session = Depends(get_db)):
    disciplina = db.query(models.Disciplina).filter(models.Disciplina.id == id).first()
    if not disciplina:
        raise HTTPException(status_code=404, detail="Disciplina não encontrada")
    return disciplina

# Cadastrar
@router.post("/", response_model=schemas.DisciplinaResponse)
def cadastrar_disciplina(disciplina: schemas.DisciplinaCreate, db: Session = Depends(get_db)):
    nova = models.Disciplina(**disciplina.dict())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

# Editar
@router.put("/{id}", response_model=schemas.DisciplinaResponse)
def editar_disciplina(id: int, dados: schemas.DisciplinaCreate, db: Session = Depends(get_db)):
    disciplina = db.query(models.Disciplina).filter(models.Disciplina.id == id).first()
    if not disciplina:
        raise HTTPException(status_code=404, detail="Disciplina não encontrada")
    for key, value in dados.dict().items():
        setattr(disciplina, key, value)
    db.commit()
    db.refresh(disciplina)
    return disciplina

# Deletar
@router.delete("/{id}")
def deletar_disciplina(id: int, db: Session = Depends(get_db)):
    disciplina = db.query(models.Disciplina).filter(models.Disciplina.id == id).first()
    if not disciplina:
        raise HTTPException(status_code=404, detail="Disciplina não encontrada")
    db.delete(disciplina)
    db.commit()
    return {"mensagem": "Disciplina deletada com sucesso"}