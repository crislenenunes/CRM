# Mini CRM com FastAPI e Streamlit

Este projeto consiste em um **CRM funcional e flexível**, desenvolvido com **FastAPI** no backend e **Streamlit** no frontend. A aplicação foi projetada para gerenciar leads de forma eficiente, oferecendo funcionalidades essenciais como cadastro, visualização e acompanhamento de interações. É uma solução ideal para pequenas empresas ou equipes de vendas que buscam organizar suas operações de forma simples e eficaz.

## Funcionalidades

- **Cadastro de Leads**: Permite registrar e armazenar informações completas sobre os leads, como nome, e-mail, telefone, status e origem.
- **Visualização de Leads**: Exibe uma lista completa dos leads cadastrados, facilitando o acompanhamento e análise.
- **Histórico de Interações**: Registra as interações realizadas com os leads, possibilitando um histórico detalhado de contato.
- **Dashboard de Vendas**: Apresenta o status dos leads e a visualização do funil de vendas, ajudando na análise de performance e tomada de decisões.

## Como Rodar o Projeto

1. **Instalar as dependências**:
   Execute o seguinte comando para instalar todas as dependências:
   ```bash
   pip install -r requirements.txt
   ```

2. **Iniciar o Backend com FastAPI**:
   Para rodar o servidor do backend, use o comando:
   ```bash
   uvicorn backend.main:app --reload
   ```

3. **Iniciar o Frontend com Streamlit**:
   Para iniciar o frontend, execute:
   ```bash
   streamlit run frontend/app.py
   ```

## Melhorias Futuras

- **Autenticação**: Implementação de login com autenticação para maior controle de acesso.
- **Banco de Dados**: Substituição do armazenamento em JSON por um banco de dados relacional (SQLite ou PostgreSQL).
- **Filtros e Busca**: Funcionalidade de busca e filtros avançados para leads, permitindo segmentações por status, origem, data de contato, entre outros.
- **Análises e Relatórios**: Implementação de gráficos interativos e relatórios detalhados sobre o desempenho de vendas e status do funil.
- **Notificações e Alertas**: Funcionalidade de alertas e notificações automáticas para follow-ups de leads.

## Fluxograma do Sistema

```plaintext
+----------------+     +--------------------+     +----------------------+
|  Cadastro de   |---->|  Visualização de    |---->|  Histórico de        |
|    Leads       |     |  Leads              |     |  Interações          |
+----------------+     +--------------------+     +----------------------+
       |                        |
       v                        v
+----------------+     +----------------------+
|   Dashboard    |<----|  Funil de Vendas     |
|   de Vendas    |     |  (Análises e Relatórios) |
+----------------+     +----------------------+
```

---
## 📄 Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

---

<div align="center">  
  <p>Desenvolvido com ❤️ por <a href="https://github.com/crislenenunes">Crislene Nunes</a></p>  
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" alt="Python">  
  <img src="https://img.shields.io/badge/scikit--learn-1.3+-orange?logo=scikit-learn" alt="Scikit-learn">  
  <img src="https://img.shields.io/badge/Gradio-4.28.3-green?logo=gradio" alt="Gradio">  
</div>
