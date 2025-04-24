from pydantic import BaseModel
from datetime import datetime

# Modelo de dados para Lead
class Lead(BaseModel):
    id: int               # Identificador único do lead
    nome: str             # Nome do lead
    email: str            # E-mail do lead
    telefone: str         # Telefone do lead
    status: str           # Status do lead (ex: Novo, Em Contato, Fechado)
    origem: str           # Origem do lead (ex: Website, Campanha, etc)
    data_criacao: datetime  # Data de criação do lead

    class Config:
        # Configuração para permitir a leitura de datas no formato ISO 8601
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }

