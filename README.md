# 🐝 Monitoramento de Colmeias com Streamlit

Este projeto é um aplicativo desenvolvido em **Python** com **Streamlit** para análise de dados ambientais de colmeias de abelhas, focando especialmente na comparação entre sensores de colmeias e o ambiente externo utilizando **Análise de Variância (ANOVA)**.

---

## 📂 Formato dos Dados

O app espera um arquivo CSV com o seguinte formato:

```csv
data,hora,tc9,uc9,pc9,tamb,uamb,pamb
2024-08-29,15:40,27.4,75.23,1018.97,21.65,59.2,1017.94
2024-08-29,16:10,29.72,70.64,1019.12,21.43,62.04,1018.13
...
```

- `tc9`, `uc9`, `pc9`: Temperatura, Umidade e Pressão da Colmeia 9
- `tamb`, `uamb`, `pamb`: Temperatura, Umidade e Pressão do Ambiente
- `data`, `hora`: serão combinados em um índice `datetime`

---

## ⚙️ Funcionalidades

- Upload de CSV
- Visualização de dados
- Comparações com **ANOVA** (teste `f_oneway`)
- Visualizações com boxplots
- Identificação de diferenças estatisticamente significativas

---

## 🚀 Como Executar Localmente

1. Clone o repositório:
```bash
git clone https://github.com/seuusuario/nome-do-repositorio.git
cd nome-do-repositorio
```

2. Instale as dependências:
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
- Seaborn
- Matplotlib
- Scipy

---

## 📌 Observações

- Para rodar o app, basta subir um CSV no formato indicado
- O teste ANOVA compara as médias das variáveis selecionadas para identificar diferenças estatísticas

---

## 🐝 Sobre

Este projeto foi desenvolvido para auxiliar apicultores e pesquisadores no monitoramento ambiental de colmeias, promovendo decisões baseadas em dados.


