# 🐝 Monitoramento de Colmeias com Streamlit - Correlação Cruzada com Defasagem

Este projeto é um aplicativo interativo desenvolvido com **Streamlit** para análise de dados ambientais de colmeias de abelhas. Esta versão do app foca na análise da **influência temporal** entre variáveis, por meio da **Correlação Cruzada com Defasagem**, permitindo identificar atrasos entre sinais (por exemplo, entre ambiente e sensores da colmeia).

---

## 📂 Estrutura do Arquivo CSV

O app utiliza um arquivo `.csv` com os seguintes campos:

```csv
data,hora,tc9,uc9,pc9,tamb,uamb,pamb
2024-08-29,15:40,27.4,75.23,1018.97,21.65,59.2,1017.94
2024-08-29,16:10,29.72,70.64,1019.12,21.43,62.04,1018.13
...
```

- `tc9`, `uc9`, `pc9`: Temperatura, Umidade e Pressão da Colmeia 9
- `tamb`, `uamb`, `pamb`: Temperatura, Umidade e Pressão do Ambiente
- `data`, `hora`: combinadas para formar o índice temporal

---

## ⚙️ Funcionalidades

- Upload de CSV com dados ambientais
- Visualização da série temporal
- Análise de Correlação Cruzada com Defasagem:
  - Escolha de variável dependente (ex: temperatura colmeia)
  - Escolha de variável independente (ex: temperatura ambiente)
  - Cálculo de correlação cruzada entre os pares de variáveis
  - Identificação do **atraso (defasagem)** com maior correlação
- Visualizações de:
  - Sinais temporais
  - Curva de correlação cruzada vs defasagem

---

## 🚀 Como Executar Localmente

1. Clone o repositório:
```bash
git clone https://github.com/seuusuario/monitoramento-colmeias-defasagem.git
cd monitoramento-colmeias-defasagem
```

2. Instale os pacotes necessários:
```bash
pip install -r requirements.txt
```

3. Execute o app:
```bash
streamlit run app.py
```

---

## 🧪 Tecnologias Usadas

- Python 3
- Streamlit
- Pandas
- Numpy
- Matplotlib
- Scipy

---

## 📈 O Que é Correlação Cruzada com Defasagem?

A correlação cruzada é uma técnica para medir a **semelhança entre duas séries temporais deslocadas no tempo**. Isso ajuda a identificar se mudanças em uma variável antecedem (ou seguem) mudanças em outra.

---

## 🐝 Propósito do Projeto

Este aplicativo tem como objetivo auxiliar apicultores e pesquisadores a entenderem como fatores ambientais impactam sensores das colmeias ao longo do tempo, com foco em atrasos e dinâmicas de influência.


