from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Departamento(Base):
    __tablename__ = "departamentos"
    id   = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)

class Curso(Base):
    __tablename__ = "cursos"
    id              = Column(Integer, primary_key=True, index=True)
    nome            = Column(String(100), nullable=False)
    departamento_id = Column(Integer, ForeignKey("departamentos.id"))

class Professor(Base):
    __tablename__ = "professores"
    id              = Column(Integer, primary_key=True, index=True)
    nome            = Column(String(100), nullable=False)
    email           = Column(String(100), unique=True, nullable=False)
    departamento_id = Column(Integer, ForeignKey("departamentos.id"))

class Aluno(Base):
    __tablename__ = "alunos"
    id       = Column(Integer, primary_key=True, index=True)
    nome     = Column(String(100), nullable=False)
    email    = Column(String(100), unique=True, nullable=False)
    curso_id = Column(Integer, ForeignKey("cursos.id"))

class Disciplina(Base):
    __tablename__ = "disciplinas"
    id            = Column(Integer, primary_key=True, index=True)
    nome          = Column(String(100), nullable=False)
    carga_horaria = Column(Integer, nullable=False)
    curso_id      = Column(Integer, ForeignKey("cursos.id"))