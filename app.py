import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Configurações globais
plt.style.use('ggplot')
st.set_page_config(
    page_title="MonitorApi - Análise de Colmeias",
    page_icon="🐝",
    layout="wide"
)

# st.set_page_config(page_title="Monitoramento de Colmeias", layout="wide")

# Função: Correlação com defasagem
def plot_cross_correlation(df, var_x, var_y, max_lag=6):
    lags = range(-max_lag, max_lag + 1)
    correlations = []

    for lag in lags:
        shifted_x = df[var_x].shift(lag)
        corr = df[var_y].corr(shifted_x)
        correlations.append(corr)

    fig, ax = plt.subplots(figsize=(6, 3.5))
    ax.plot(lags, correlations, marker='o')
    ax.axvline(0, color='gray', linestyle='--')
    ax.set_xlabel("Defasagem (lags)")
    ax.set_ylabel("Correlação")
    ax.set_title(f"Correlação Cruzada: {var_y} vs {var_x}")
    ax.grid(True)
    st.pyplot(fig)

# Função: Exemplo de defasagem visual
def show_lag_demo(df, var_env, var_colmeia, lag):
    df_demo = df[[var_env, var_colmeia]].copy().head(10)
    df_demo[f"{var_env}_deslocado"] = df_demo[var_env].shift(lag)
    st.markdown(f"#### 🧪 Exemplo de Defasagem: {lag} linha(s)")
    st.dataframe(df_demo[[var_env, f"{var_env}_deslocado", var_colmeia]])

# Upload do CSV
st.sidebar.header("📂 Carregar dados")
uploaded_file = st.sidebar.file_uploader("Escolha o arquivo CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df["datetime"] = pd.to_datetime(df["data"] + " " + df["hora"])
    df.set_index("datetime", inplace=True)

    st.title("📊 Análise de Monitoramento das Colmeias")

    # Filtros por data
    st.sidebar.header("⏱️ Filtro de Período")
    start_date = st.sidebar.date_input("Data inicial", df.index.date.min())
    end_date = st.sidebar.date_input("Data final", df.index.date.max())

    mask = (df.index.date >= start_date) & (df.index.date <= end_date)
    df = df.loc[mask]

    tab9, tab10, tab11 = st.tabs(["Sensor 9", "Sensor 10", "Sensor 11"])

    sensores = {
        "Sensor 9": ("tc09", "uc09", "pc09"),
        "Sensor 10": ("tc10", "uc10", "pc10"),
        "Sensor 11": ("tc11", "uc11", "pc11")
    }

    ambiente = ("tamb", "uamb", "pamb")

    for tab, sensor_nome in zip([tab9, tab10, tab11], sensores.keys()):
        with tab:
            st.subheader(f"📈 Análise - {sensor_nome}")

            col_temp, col_umid, col_press = sensores[sensor_nome]

            # Estatísticas
            st.markdown("#### 📋 Estatísticas Descritivas")
            st.dataframe(df[[col_temp, col_umid, col_press]].describe())

            # Gráficos temporais
            st.markdown("#### 🕒 Evolução Temporal")
            fig, ax = plt.subplots(1, 1, figsize=(7, 3.5))
            ax.plot(df.index, df[col_temp], label="Temperatura")
            ax.plot(df.index, df[ambiente[0]], label="Temp. Ambiente", linestyle="--")
            ax.set_ylabel("Temperatura (°C)")
            ax.set_title("Temperatura: Sensor vs Ambiente")
            ax.legend()
            st.pyplot(fig)

            fig, ax = plt.subplots(1, 1, figsize=(7, 3.5))
            ax.plot(df.index, df[col_umid], label="Umidade")
            ax.plot(df.index, df[ambiente[1]], label="Umid. Ambiente", linestyle="--")
            ax.set_ylabel("Umidade (%)")
            ax.set_title("Umidade: Sensor vs Ambiente")
            ax.legend()
            st.pyplot(fig)

            # Correlação (Temperatura e Umidade)
            st.markdown("#### 🔗 Correlação: Temperatura e Umidade")
            cols_temp_umid = [col_temp, col_umid, ambiente[0], ambiente[1]]
            fig, ax = plt.subplots(figsize=(4, 3.5))
            sns.heatmap(df[cols_temp_umid].corr(), annot=True, cmap="coolwarm", ax=ax)
            st.pyplot(fig)

            # Correlação Cruzada
            st.markdown("### ⏳ Correlação Cruzada com Defasagem")
            st.caption("Analisa se os sensores da colmeia reagem com atraso às variações ambientais.")

            st.info("""
                **O que significa a Defasagem Máxima em linhas?**
                
                Cada linha do CSV representa um momento no tempo (ex: a cada 30 minutos).
                A defasagem indica o quanto os dados do ambiente serão deslocados no tempo
                para verificar se a colmeia reage com atraso.
                
                Por exemplo, se a umidade da colmeia responde com 2 linhas de atraso às mudanças
                da umidade ambiente, isso significa uma defasagem de 1 hora (2 x 30min).
            """)

            variaveis_colmeia = [col_temp, col_umid]
            variaveis_ambiente = [ambiente[0], ambiente[1]]

            col1, col2 = st.columns(2)
            with col1:
                var_colmeia = st.selectbox("🔽 Variável da Colmeia", variaveis_colmeia, index=1, key=sensor_nome+"_col")
            with col2:
                var_amb = st.selectbox("🌦️ Variável do Ambiente", variaveis_ambiente, index=1, key=sensor_nome+"_amb")

            max_lag = st.slider("⏲️ Defasagem Máxima (linhas)", 1, 12, 6, key=sensor_nome+"_lag")
            plot_cross_correlation(df, var_amb, var_colmeia, max_lag=max_lag)
            show_lag_demo(df, var_amb, var_colmeia, lag=2)
else:
    st.warning("Por favor, carregue um arquivo CSV com os dados de monitoramento.")

