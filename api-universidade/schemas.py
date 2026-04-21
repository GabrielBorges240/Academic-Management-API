from pydantic import BaseModel

# --- Aluno ---
class AlunoCreate(BaseModel):
    nome:     str
    email:    str
    curso_id: int

class AlunoResponse(AlunoCreate):
    id: int
    class Config:
        from_attributes = True

# --- Professor ---
class ProfessorCreate(BaseModel):
    nome:            str
    email:           str
    departamento_id: int

class ProfessorResponse(ProfessorCreate):
    id: int
    class Config:
        from_attributes = True

# --- Disciplina ---
class DisciplinaCreate(BaseModel):
    nome:          str
    carga_horaria: int
    curso_id:      int

class DisciplinaResponse(DisciplinaCreate):
    id: int
    class Config:
        from_attributes = True