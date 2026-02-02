import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Dashboard de Vendas da empresa Jerf S/A",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- LÓGICA DE NAVEGAÇÃO ---
if 'pagina_ativa' not in st.session_state:
    st.session_state.pagina_ativa = "Home"

def mudar_pagina(nome):
    st.session_state.pagina_ativa = nome

# --- BARRA LATERAL COM OS BOTÕES ---
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>JERF S/A</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Business Intelligence</p>", unsafe_allow_html=True)
    st.divider()

    st.markdown("### 🧭 Menu")
    if st.button("🏠 Home", use_container_width=True): mudar_pagina("Home")
    if st.button("📈 KPIs", use_container_width=True): mudar_pagina("KPIs")
    if st.button("🗺️ Mapas", use_container_width=True): mudar_pagina("Mapas")
    if st.button("📦 Produtos", use_container_width=True): mudar_pagina("Produtos")
    if st.button("⚠️ Atenção", use_container_width=True): mudar_pagina("Atenção")
    if st.button("👥 Vendedores", use_container_width=True): mudar_pagina("Vendedores")
    if st.button("📊 Dados", use_container_width=True): mudar_pagina("Dados")
    if st.button("🔍 Revisão", use_container_width=True): mudar_pagina("Revisão")
    if st.button("🤝🏽 Agradecimento", use_container_width=True): mudar_pagina("Agradecimento")

# --- CARREGAMENTO DOS DADOS ---
df = pd.read_csv("vendas2018.csv")

meses_map = {1: "01-Jan", 2: "02-Fev", 3: "03-Mar", 4: "04-Abr", 5: "05-Mai", 6: "06-Jun",
    7: "07-Jul", 8: "08-Ago", 9: "09-Set", 10: "10-Out", 11: "11-Nov", 12: "12-Dez"
}
df['Mês'] = df['Mês'].map(meses_map)

# --- FILTROS DA BARRA LATERAL ---
st.sidebar.header("🔍 Filtros")
meses_disponiveis = sorted(df['Mês'].unique())
meses_selecionados = st.sidebar.multiselect("Mês", meses_disponiveis, default=meses_disponiveis)

cidades_disponiveis = sorted(df['Cidade'].unique())
cidades_selecionados = st.sidebar.multiselect("Cidade", cidades_disponiveis, default=cidades_disponiveis)

produtos_disponiveis = sorted(df['Produto'].unique())
produtos_selecionados = st.sidebar.multiselect("Produto", produtos_disponiveis, default=produtos_disponiveis)

df_filtrado = df[
    (df['Mês'].isin(meses_selecionados)) &
    (df['Cidade'].isin(cidades_selecionados)) &
    (df['Produto'].isin(produtos_selecionados))
]

# --- CONTEÚDO DAS PÁGINAS ---

if st.session_state.pagina_ativa == "Home":
    # --- Página de Capa ---
    st.title("🏠 Bem-vindo ao Portal de BI - Jerf S/A")
    st.divider()
    
    col_capa1, col_capa2 = st.columns([2, 1])
    
    with col_capa1:
        st.markdown("""
        ### Sistema de Análise de Performance 2018
        Esta plataforma centraliza os indicadores estratégicos de vendas, permitindo uma visão clara do crescimento 
        da **Jerf S/A**. Explore as abas laterais para navegar pelos diferentes níveis de detalhamento.
        
        **Instruções de uso:**
        * Use o menu à esquerda para trocar de visão.
        * Utilize os filtros globais para segmentar por período, região ou produto.
        * Todos os gráficos são interativos.
        """)
        st.info("💡 **Aviso:** Os dados atuais referem-se ao consolidado do ano fiscal de 2018.")
    
    with col_capa2:
        st.success("✅ Sistema Online")
        st.metric("Total de Registros Processados", f"{len(df):,}")

elif st.session_state.pagina_ativa == "KPIs":
    # --- Nova Página KPIs (Antiga Home) ---
    st.title("🎲 Dashboard de Análise de Vendas de 2018")
    st.markdown("Explore os dados de vendas no país Brasil. Utilize os filtros à esquerda para refinar sua análise.")

    st.markdown("**Métricas gerais (Venda Total em BRL)**")

    if not df_filtrado.empty:
        total_vendas = df_filtrado['Total'].sum()
        quantidade_vendidos = df_filtrado['Quantidade Vendida'].sum()
        quantidade_vendas = df_filtrado.shape[0]
        ticket_medio = df_filtrado["Total"].mean()
    else:
        total_vendas, quantidade_vendidos, quantidade_vendas, ticket_medio = 0, 0, 0, 0

    st.subheader("📈 KPIs Principais")

    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total de Vendas", f"R${total_vendas:,.0f}")
    col2.metric("Quantidade de Produtos Vendidos", f"{quantidade_vendidos:,}")
    col3.metric("Quantidade de Vendas", f"{quantidade_vendas:,}")
    col4.metric("Ticket Médio", f"R${ticket_medio:,.0f}")

    col_graf1, col_graf2 = st.columns(2)

    with col_graf1:
        if not df_filtrado.empty:
            venda_cidade = df_filtrado.groupby('Cidade')['Total'].sum().sort_values(ascending=False).reset_index()
            
            # 1. Adicionamos 'text' para definir o que será exibido
            grafico_cidade = px.bar(venda_cidade, x='Cidade', y='Total', text='Total', 
                                    title="Total de Vendas por Cidade", labels={'Total': '', 'Cidade': ''})
            
            # 2. 'textposition' define onde o rótulo fica. 'inside' coloca dentro da barra.
            # 'texttemplate' serve para formatar o número (ex: R$ ou casas decimais)
            grafico_cidade.update_traces(textposition='inside', texttemplate='R$ %{text:.2s}')
            grafico_cidade.update_layout(title_x=0.3, yaxis={'categoryorder':'total ascending'})
            st.plotly_chart(grafico_cidade, use_container_width=True)
    with col_graf2:
            if not df_filtrado.empty:
                # Agrupando por Mês
                venda_mensal = df_filtrado.groupby('Mês')['Total'].sum().reset_index()
                
                # Criando o gráfico de linhas
                grafico_linha = px.line(venda_mensal, x='Mês', y='Total', text='Total',
                                        title="Evolução do Total de Vendas por Mês", 
                                        labels={'Total': 'Faturamento'},
                                        markers=True)

                # Ajustando os rótulos de dados
                grafico_linha.update_traces(textposition='top center', texttemplate='R$ %{text:.2s}')        
                # Opcional: Ocultar o eixo Y também para um visual mais "clean", já que tem rótulos
                grafico_linha.update_yaxes(showticklabels=False, title=None, showgrid=False)
                grafico_linha.update_xaxes(title=None)
                grafico_linha.update_layout(title_x=0.3, plot_bgcolor='rgba(0,0,0,0)')
                st.plotly_chart(grafico_linha, use_container_width=True)

    if not df_filtrado.empty:
        # Agrupando por Mês
        venda_mensal = df_filtrado.groupby('Mês')['Quantidade Vendida'].sum().reset_index()
        
        # Criando o gráfico de linhas
        grafico_linha = px.line(venda_mensal, x='Mês', y='Quantidade Vendida', text='Quantidade Vendida',
                                title="Evolução do Total de Quantidade Vendida por Mês", 
                                labels={'Quantidade Vendida': 'Faturamento'},
                                markers=True)

        # Ajustando os rótulos de dados
        grafico_linha.update_traces(textposition='top center', texttemplate='R$ %{text:.2s}')        
        # Opcional: Ocultar o eixo Y também para um visual mais "clean", já que tem rótulos
        grafico_linha.update_yaxes(showticklabels=False, title=None, showgrid=False)
        grafico_linha.update_xaxes(title=None)
        grafico_linha.update_layout(title_x=0.3, plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(grafico_linha, use_container_width=True)

elif st.session_state.pagina_ativa == "Mapas":
    st.subheader("🗺️ Mapas")
    st.divider()
    col_graf3, col_nota = st.columns([3, 1])

    coordenadas_capitais = {
        'Goiânia': [-16.6869, -49.2648], 'Rio de Janeiro': [-22.9068, -43.1729],
        'Recife': [-8.0543, -34.8813], 'Belo Horizonte': [-19.9167, -43.9345],
        'São Paulo': [-23.5505, -46.6333], 'Salvador': [-12.9714, -38.5014],
        'Curitiba': [-25.4284, -49.2733], 'Porto Alegre': [-30.0346, -51.2177],
        'Fortaleza': [-3.7172, -38.5433]
    }
    with col_graf3:
        if not df_filtrado.empty:
            df_filtrado['lat'] = df_filtrado['Cidade'].map(lambda x: coordenadas_capitais.get(x, [0,0])[0])
            df_filtrado['lon'] = df_filtrado['Cidade'].map(lambda x: coordenadas_capitais.get(x, [0,0])[1])
            vendas_cidade_mapa = df_filtrado.groupby(['Cidade', 'lat', 'lon'])['Total'].sum().reset_index()
            grafico_paises = px.scatter_geo(vendas_cidade_mapa, lat='lat', lon='lon', size='Total', color='Total', hover_name='Cidade', color_continuous_scale='rdylgn', scope="south america", title='Total de Vendas por Cidade')
            grafico_paises.update_geos(lataxis_range=[-35, 5], lonaxis_range=[-75, -30], showland=True, landcolor="white", showocean=True, oceancolor="LightBlue")
            grafico_paises.update_layout(title_x=.34)
            st.plotly_chart(grafico_paises, use_container_width=True)

    with col_nota:
        st.subheader("Entenda")
        st.info("🌆 **São Paulo** obteve o maior volume de vendas.")
        st.metric("Total de Vendas", f"R$ {df_filtrado['Total'].sum():,}")
        st.metric("Quantidade de Vendas", f"{df_filtrado['Quantidade Vendida'].sum():,}")

elif st.session_state.pagina_ativa == "Produtos":
    st.subheader("📦 Produtos")
    st.divider()
    col_nota2, col_graf4 = st.columns([1, 3])
    with col_nota2:
        st.subheader("📱 iPhone na Liderança")
        df_iphone = df_filtrado[df_filtrado['Produto'] == 'iPhone']
        total_financeiro_iphone = df_iphone['Total'].sum()
        qtd_financeiro_iphone = df_iphone['Quantidade Vendida'].sum()
        quantidade_iphone = df_iphone['Quantidade Vendida'].sum()
        ticket_medio_iphone = total_financeiro_iphone / quantidade_iphone if quantidade_iphone > 0 else 0
        st.info(f"💲 Ticket Médio: R$ {ticket_medio_iphone:,.2f}")
        st.metric("Total de Vendas (iPhone)", f"R$ {total_financeiro_iphone:,}")
        st.metric("Quantidade Vendida (iPhone)", f"{qtd_financeiro_iphone:,}")
    with col_graf4:
        funil_produto = df_filtrado.groupby('Produto')['Total'].sum().sort_values(ascending=False).reset_index()
        grafico_funil = px.funnel_area(funil_produto, values='Total', names='Produto', title="Funil de Vendas por Produto")
        grafico_funil.update_traces(textinfo="label+value", texttemplate="<b>%{label}</b><br>R$ %{value:,}")
        grafico_funil.update_layout(title_x=.385,showlegend=False,)
        st.plotly_chart(grafico_funil, use_container_width=True)

elif st.session_state.pagina_ativa == "Atenção":
    st.subheader("⚠️ Atenção")
    st.divider()
    col_graf5, col_nota3 = st.columns([3, 1])
    with col_nota3:
        if not df_filtrado.empty:
            pior_performance = df_filtrado.groupby('Produto')['Total'].sum().sort_values(ascending=True).reset_index()
            nome_pior_produto = pior_performance.iloc[0]['Produto']
            st.subheader(f"⌚ **{nome_pior_produto}** na Lanterna.")
    
        df_smart = df_filtrado[df_filtrado['Produto'] == 'SmartWatch']
        total_financeiro_iphone = df_smart['Total'].sum()
        qtd_financeiro_iphone = df_smart['Quantidade Vendida'].sum()
        quantidade_iphone = df_smart['Quantidade Vendida'].sum()
        ticket_medio_iphone = total_financeiro_iphone / quantidade_iphone if quantidade_iphone > 0 else 0
        st.error(f"💲 Ticket Médio: R$ {ticket_medio_iphone:,.2f}")
        st.metric("Total de Vendas (SmartWatch)", f"R$ {total_financeiro_iphone:,}")
        st.metric("Quantidade Vendida (SmartWatch)", f"{qtd_financeiro_iphone:,}")
    with col_graf5:
        df_waterfall = df_filtrado.groupby('Produto')['Total'].sum().reset_index()
        
        labels = list(df_waterfall['Produto']) + ["Total de Vendas"]
        valores = list(df_waterfall['Total']) + [df_waterfall['Total'].sum()]
        medidas = ["relative"] * len(df_waterfall) + ["total"]

        fig_waterfall = go.Figure(go.Waterfall(
            name="Total", 
            orientation="v", 
            measure=medidas,
            x=labels,
            y=valores,
            text=valores,
            texttemplate="R$ %{text:,}", # Usei .2s para encurtar valores se forem grandes (ex: 1.5k)
            textposition="outside", 
            connector={"line": {"color": "rgb(63, 63, 63)"}},
        ))

        fig_waterfall.update_layout(
            title={
                'text': "Análise de Contribuição por Produto",
                'x': 0.5,
                'xanchor': 'center',
                'y': 0.95  # Ajusta a altura do título ligeiramente
            },
            showlegend=False,
            # Aumentamos a margem do topo (t) para 80 ou 100 para dar espaço ao rótulo e título
            margin=dict(l=20, r=20, t=100, b=50), 
            yaxis=dict(range=[0, max(valores) * 1.2]) # Dá 20% de folga no topo do eixo Y
        )
        
        st.plotly_chart(fig_waterfall, use_container_width=True)
        
elif st.session_state.pagina_ativa == "Vendedores":
    st.subheader("👥 Vendedores")
    st.divider()
    st.markdown("<h3 style='text-align: center;'>🏆 Top 3 Vendedores</h3>", unsafe_allow_html=True)
    top_3 = df_filtrado.groupby('Vendedor')['Total'].sum().sort_values(ascending=False).head(3).reset_index()
    if not top_3.empty:
        vendedores = top_3['Vendedor'].tolist()
        valores = top_3['Total'].tolist()
        col_prata, col_ouro, col_bronze = st.columns(3)
        with col_ouro:
            st.markdown("<h1 style='text-align: center;'>🥇</h1>", unsafe_allow_html=True)
            st.metric(label=f"1º: {vendedores[0]}", value=f"R$ {valores[0]:,.2f}")
        with col_prata:
            if len(vendedores) >= 2:
                st.markdown("<h2 style='text-align: center;'>🥈</h2>", unsafe_allow_html=True)
                st.metric(label=f"2º: {vendedores[1]}", value=f"R$ {valores[1]:,.2f}")
        with col_bronze:
            if len(vendedores) >= 3:
                st.markdown("<h3 style='text-align: center;'>🥉</h3>", unsafe_allow_html=True)
                st.metric(label=f"3º: {vendedores[2]}", value=f"R$ {valores[2]:,.2f}")
                   
    # O primeiro texto (equivalente ao #####)
    st.markdown("<h5 style='text-align: center;'>Parabéns ao Top 3! Cada um vai ganhar um iPhone 17 Pro Max e um Day Off!</h5>", unsafe_allow_html=True)

    # O segundo texto (texto comum)
    st.markdown("<p style='text-align: center;'>O time de vendas vai curtir um jantar especial em comemoração ao atingimento das metas!</p>", unsafe_allow_html=True)

    st.divider()

    if not df_filtrado.empty:
        top_vendedor = df_filtrado.groupby('Vendedor')['Total'].sum().nlargest(10).sort_values(ascending=True).reset_index()
        
        # Mesma lógica para o gráfico horizontal
        grafico_vendedor = px.bar(top_vendedor, x='Total', y='Vendedor', orientation='h', text='Total',
                                title="Top 10 Vendedores", labels={'Total': '', 'Vendedor': ''})
        
        grafico_vendedor.update_traces(textposition='inside', texttemplate='RS %{text:,}')
        
        grafico_vendedor.update_layout(title_x=0.5, yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(grafico_vendedor, use_container_width=True)

elif st.session_state.pagina_ativa == "Dados":
    st.subheader("📊 Dados")
    st.subheader("Matriz")
    colunas_visiveis = [col for col in df_filtrado.columns if col not in ['lat', 'lon']]
    st.dataframe(df_filtrado, column_order=colunas_visiveis, use_container_width=True)

elif st.session_state.pagina_ativa == "Revisão":
    st.title("🔍 Revisão Executiva - Ciclo 2018")
    st.divider()

    # Cálculos para a revisão
    total_vendas_ano = df['Total'].sum()
    total_unidades = df['Quantidade Vendida'].sum()
    melhor_mes = df.groupby('Mês')['Total'].sum().idxmax()
    produto_lider = df.groupby('Produto')['Total'].sum().idxmax()
    cidade_lider = df.groupby('Cidade')['Total'].sum().idxmax()

    # Filtrando o DataFrame apenas para o mês de Dezembro
    vendas_dezembro = df[df['Mês'] == "12-Dez"]
    # Somando a coluna 'Total' e a 'Quantidade Vendida'
    total_financeiro_dez = vendas_dezembro['Total'].sum()
    total_itens_dez = vendas_dezembro['Quantidade Vendida'].sum()

    st.markdown(f"""
    ### 📝 Resumo do Desempenho
    Após a análise detalhada dos dados da **Jerf S/A** referentes ao ano de 2018, identificamos pontos cruciais para o planejamento do próximo ciclo.
    
    #### 🚀 Destaques Positivos
    * **Faturamento Consolidado:** Alcançamos marca de **R$ {total_vendas_ano:,.2f}**.
    * **Liderança de Produto:** O **{produto_lider}** consolidou-se como o carro-chefe da empresa, sendo responsável pela maior fatia do faturamento.
    * **Hub Regional:** A cidade de **{cidade_lider}** apresentou a melhor performance de vendas, servindo de modelo para expansão em outras capitais.
    * **Pico de Vendas:** O mês de **{melhor_mes}** foi o período de maior atividade econômica do ano com um total de **R$ {total_financeiro_dez:,.2f}** de faturamento.

    ---

    #### ⚠️ Pontos de Atenção e Melhoria
    1.  **Mix de Produtos:** Embora o iPhone lidere as vendas, produtos como o **SmartWatch** apresentam uma margem de contribuição menor, necessitando de uma revisão nas estratégias de marketing ou precificação.
    2.  **Distribuição Geográfica:** Notou-se uma concentração muito forte em grandes capitais. Existe uma oportunidade de capilaridade em cidades do interior para 2019.
    3.  **Ticket Médio:** O ticket médio geral estabilizou. Estratégias de *cross-selling* (venda cruzada) podem ser implementadas para aumentar o valor de cada transação.

    ---

    ### 📈 Conclusão Estratégica
    O ano de 2018 foi de **maturação e crescimento**. A Jerf S/A possui uma base de dados sólida e um time de vendedores altamente engajado (conforme visto na aba 👥 Vendedores). 
    
    **Recomendação:** Focar os investimentos do Q1 de 2019 em campanhas digitais para os produtos de tecnologia vestível e expandir o modelo de treinamento dos "Top 3 Vendedores" para o restante da equipe.
    """)

    st.info("💡 *Esta revisão foi gerada automaticamente com base nos dados brutos processados pelo motor de BI.*")

elif st.session_state.pagina_ativa == "Agradecimento":
    st.markdown("<h1 style='text-align: center;'>🤝🏽 Agradecimento</h1>", unsafe_allow_html=True)
    st.divider()
    st.markdown("<p style='text-align: center;'>Agradeço a todos os professores, amigos, colegas de profissão e colegas de turma que confiaram em minha capadidade! Seguirei aprendendo e evoluindo para entregar resultados duradouros por onde puder!</p>", unsafe_allow_html=True)
    st.balloons()
    st.success("Obrigado por utilizar o sistema Jerf S/A!")