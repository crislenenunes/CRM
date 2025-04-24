import streamlit as st
import requests

BASE_URL = "http://localhost:8000"  # Alterar quando for para produção

# Função para exibir leads
def show_leads():
    response = requests.get(f"{BASE_URL}/leads/")
    leads = response.json()
    for lead in leads:
        st.write(f"Nome: {lead['nome']}, Status: {lead['status']}, Contato: {lead['data_contato']}")

# Formulário para adicionar novo lead
st.title("Mini CRM")

with st.form(key="lead_form"):
    nome = st.text_input("Nome")
    email = st.text_input("E-mail")
    telefone = st.text_input("Telefone")
    status = st.selectbox("Status", ["Em negociação", "Convertido", "Perdido"])
    origem = st.text_input("Origem")
    data_contato = st.date_input("Data de Contato")
    submit_button = st.form_submit_button("Adicionar Lead")
    
    if submit_button:
        lead_data = {
            "nome": nome,
            "email": email,
            "telefone": telefone,
            "status": status,
            "origem": origem,
            "data_contato": str(data_contato),
        }
        requests.post(f"{BASE_URL}/lead/", json=lead_data)
        st.success("Lead adicionado com sucesso!")

# Exibe todos os leads
st.subheader("Lista de Leads")
show_leads()
