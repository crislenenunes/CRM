from fastapi import FastAPI
from pydantic import BaseModel
from .crud import create_lead, get_leads
from .database import load_data, save_data

app = FastAPI()

# Carrega dados da 'database' (JSON)
leads_db = load_data()

class Lead(BaseModel):
    nome: str
    email: str
    telefone: str
    status: str
    origem: str
    data_contato: str

@app.post("/lead/")
async def add_lead(lead: Lead):
    new_lead = create_lead(lead.dict())
    return new_lead

@app.get("/leads/")
async def list_leads():
    return get_leads()

@app.get("/")
def read_root():
    return {"message": "Bem-vindo ao Mini CRM!"}
