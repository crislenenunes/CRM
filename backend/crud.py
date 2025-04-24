from .database import save_data

def create_lead(lead_data: dict):
    leads = load_data()
    leads.append(lead_data)
    save_data(leads)
    return {"msg": "Lead criado com sucesso!", "lead": lead_data}

def get_leads():
    return load_data()
