from typing import Optional
from pydantic import BaseModel, validator

class Aluno(BaseModel):
    id: Optional[int] = None
    nome: str
    sexo:  str
    idade: int  
    peso: float
    altura: float
    objetivo: str  

    @validator('idade')
    def validar_idade(cls, idade: int):
        # Validacao 1
    
        if idade < 16 :
            
            raise ValueError('A idade deve ser maior que 16 anos.')
        return idade
alunos = [
    Aluno(id=1, nome='José Costa',sexo='masc',idade=39, peso=75.0, altura=1.75, objetivo='Perder Barriga'),
    Aluno(id=2, nome='Leticia Silva ',sexo='fem',idade= 35, peso=55.0, altura=1.55, objetivo='Tonificar pernas'),
]