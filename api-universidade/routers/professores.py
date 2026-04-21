from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models, schemas

router = APIRouter(prefix="/professores", tags=["Professores"])

# Listar todos
@router.get("/", response_model=list[schemas.ProfessorResponse])
def listar_professores(db: Session = Depends(get_db)):
    return db.query(models.Professor).all()

# Buscar por ID
@router.get("/{id}", response_model=schemas.ProfessorResponse)
def buscar_professor(id: int, db: Session = Depends(get_db)):
    professor = db.query(models.Professor).filter(models.Professor.id == id).first()
    if not professor:
        raise HTTPException(status_code=404, detail="Professor não encontrado")
    return professor

# Cadastrar
@router.post("/", response_model=schemas.ProfessorResponse)
def cadastrar_professor(professor: schemas.ProfessorCreate, db: Session = Depends(get_db)):
    novo = models.Professor(**professor.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

# Editar
@router.put("/{id}", response_model=schemas.ProfessorResponse)
def editar_professor(id: int, dados: schemas.ProfessorCreate, db: Session = Depends(get_db)):
    professor = db.query(models.Professor).filter(models.Professor.id == id).first()
    if not professor:
        raise HTTPException(status_code=404, detail="Professor não encontrado")
    for key, value in dados.dict().items():
        setattr(professor, key, value)
    db.commit()
    db.refresh(professor)
    return professor

# Deletar
@router.delete("/{id}")
def deletar_professor(id: int, db: Session = Depends(get_db)):
    professor = db.query(models.Professor).filter(models.Professor.id == id).first()
    if not professor:
        raise HTTPException(status_code=404, detail="Professor não encontrado")
    db.delete(professor)
    db.commit()
    return {"mensagem": "Professor deletado com sucesso"}