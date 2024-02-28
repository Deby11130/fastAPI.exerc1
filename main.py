from typing import Dict, List, Optional, Any

from fastapi.responses import JSONResponse
from fastapi import Response
from fastapi import Path
from fastapi import Query
from fastapi import Header
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from fastapi import Depends
from time import sleep
from models import Aluno
from models import alunos


def fake_db():
    try:
        print('Abrindo conexão com banco de dados...')
        sleep(1)
    finally:
        print('Fechando conexão com banco de dados...')
        sleep(1)

app = FastAPI(
    title='API de Exercicio_Funcional',
    version='0.0.1',
    description='Uma API Fast'
)

@app.get('/alunos',
         description='Retorna todos os dados ou uma lista vazia.',
         summary='Retorna todos os dados_alunos',
         response_model=List[Aluno],
         response_description='Alunos encontrados com sucesso.')
async def get_alunos(db: Any = Depends(fake_db)):
    return alunos

@app.post('/alunos', status_code=status.HTTP_201_CREATED, response_model=Aluno)
async def post_alunos(aluno: Aluno):
    next_id: int = len(alunos) + 1
    aluno.id = next_id
    alunos.append(aluno)
    return aluno

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=5001, reload=True)
