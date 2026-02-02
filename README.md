# 📊 Dashboard de Vendas – Jerf S/A
### Data Analytics e Tomada de Decisão - Senai

Sistema interativo de **Business Intelligence** desenvolvido em **Streamlit**, voltado para a análise de vendas da empresa **Jerf S/A** no ano fiscal de **2018**. O dashboard oferece uma visão estratégica do desempenho comercial por meio de KPIs, gráficos interativos, mapas e análises executivas.

---

## 💼 Contexto de Negócio e Objetivos

Este projeto foi desenvolvido para solucionar a fragmentação de dados em registros transacionais brutos, um desafio recorrente em departamentos de **Controladoria e Gestão Financeira**. Através da automação em Python, o objetivo é transformar relatórios estáticos em uma ferramenta estratégica de **Business Intelligence** para:

- **Monitoramento de KPIs Estratégicos:** Centralização e visualização moderna do faturamento por mês, cidade, produto e vendedor.
- **Identificação de Gargalos de Receita:** Monitoramento mensal para detecção de sazonalidades ou quedas abruptas de performance, permitindo ajustes rápidos.
- **Inteligência Regional:** Avaliação de desempenho por localidade para direcionamento de estratégias em regiões com baixo volume de vendas.
- **Otimização e Agilidade:** Substituição de extrações manuais e planilhas estáticas por uma interface dinâmica, reduzindo o tempo de resposta da gestão e automatizando a entrega de dados.

---

## 🧭 Estrutura do Dashboard

O sistema possui navegação lateral com as seguintes páginas:

- 🏠 **Home** – Apresentação do portal de BI  
- 📈 **KPIs** – Indicadores gerais de vendas  
- 🗺️ **Mapas** – Distribuição geográfica das vendas no Brasil  
- 📦 **Produtos** – Performance financeira por produto  
- ⚠️ **Atenção** – Produtos com menor desempenho  
- 👥 **Vendedores** – Ranking dos Top 3 vendedores  
- 📊 **Dados** – Visualização detalhada da base de dados  
- 🔍 **Revisão** – Análise executiva do ciclo de 2018  
- 🤝🏽 **Agradecimento** – Encerramento institucional  

---

## 🔍 Funcionalidades

- Filtros globais por:
  - Mês  
  - Cidade  
  - Produto  

- KPIs automáticos:
  - Total de vendas  
  - Quantidade de produtos vendidos  
  - Quantidade de vendas  
  - Ticket médio  

- Gráficos interativos com Plotly:
  - Barras  
  - Funil de vendas  
  - Waterfall  
  - Mapa geográfico  

- Ranking dos vendedores  
- Revisão estratégica automática baseada nos dados  

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Streamlit**
- **Pandas**
- **Plotly Express**
- **Plotly Graph Objects**

---

## 📊 Base de Dados

O arquivo `vendas2018.csv` deve conter, no mínimo, as seguintes colunas:

- `Mês`
- `Cidade`
- `Produto`
- `Vendedor`
- `Quantidade Vendida`
- `Total`

📌 Os dados utilizados correspondem exclusivamente ao **ano fiscal de 2018**.

---

## ▶️ Como Executar o Projeto

1️⃣. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/jerf-dashboard.git
```
2️⃣. Instale as dependências:
```bash
pip install streamlit pandas plotly
```
3️⃣. Execute o aplicativo:
```bash
streamlit run app.py
```
4️⃣. Acesse no navegador:   
```bash
http://localhost:8501
```
---

###  Projeto publicado através do Streamlit. Acesse-o pelo link

* 🔗 [Streamlit](https://dashboard-relatorio-vendas-2018-jerfzz.streamlit.app/)

---

## 📈 Principais Insights

- Identificação do produto líder de faturamento
- Detecção de produtos com baixa performance
- Concentração de vendas em grandes capitais
- Reconhecimento dos vendedores de maior destaque

---

## 🎓 Contexto Acadêmico

- Projeto desenvolvido com fins acadêmicos e demonstrativos, aplicando conceitos de:
- Business Intelligence
- Análise Exploratória de Dados
- Visualização de Dados
- Storytelling com Dados

---

## 📁 Estrutura do Projeto

* `app.py` — Código principal da aplicação Streamlit
* `vendas2018.csv` — Dataset processado utilizado nas visualizações
* `README.md ` — Documentação do projeto

---

## 📈 Evidências

Seguem algumas evidências do projeto:

<img width="600" height="400" alt="image" src="https://github.com/user-attachments/assets/86ad11bb-1070-4ff3-97f8-5a707818df71" />
<img width="600" height="400" alt="image" src="https://github.com/user-attachments/assets/76b8f418-ea7a-4a23-9b99-bf3555bec984" />
<img width="600" height="400" alt="image" src="https://github.com/user-attachments/assets/12bb6528-62c4-48d5-8dd9-15a321b8a471" />
<img width="600" height="400" alt="image" src="https://github.com/user-attachments/assets/4a2a33de-1b06-4a87-888e-e0602ed08a7d" />

---

## 🤝 Agradecimentos

Agradecimento especial a professores, colegas e profissionais que contribuíram para o desenvolvimento técnico e profissional ao longo da jornada.

---

## 👤 Autor

**Jerfeson Silva Santos**

* 🔗 *[LinkedIn](https://www.linkedin.com/in/jerfss/)*
* 💻 *[GitHub / Portfólio](https://github.com/jerfzz?tab=repositories)*
* 🟥 *[Streamlit](https://share.streamlit.io/user/jerfzz)*

---

📌 *Este projeto foi desenvolvido com fins educacionais durante o curso de **Data Analytics e Tomada de Decisão ofertado pelo Senai***.
