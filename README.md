## 🧬 Preditor de Diabetes para mulheres 

### 📌 Visão Geral
Aplicação de machine learning para predição de diabetes baseada em dados clínicos, com interface amigável e visualização intuitiva dos resultados.

### 📌 Funcionalidades
🔍 Predição de risco de diabetes com probabilidade percentual\
📈 Classificação automática em níveis de risco\
💡 Recomendações personalizadas baseadas no resultado\
🎨 Interface moderna com feedback visual intuitivo\
📊 Dashboard de resultados com gráficos e cores condicionais

### 🛠️ Tecnologias Utilizadas

Python v(3.11.9)
Scikit-learn (RandomForestClassifier)
Pandas (manipulação de dados)
Tkinter (interface gráfica)
Joblib (serialização do modelo)

### 📂 Estrutura do Projeto

diabetes-prediction/\
├── dados/\
│   └── diabetes.csv.......................#Dataset original\
├── modelos/\
│   └── modelo_diabetes.pkl...........# Modelo treinado\
├── interface.py.............................# Aplicação gráfica\
├── treino_modelo.py....................# Script de treinamento\
├── utils.py....................................# Funções auxiliares\
└── README.md..........................# Documentação\

### 🧠 Sobre o Modelo
Algoritmo: Random Forest Classifier\
Acurácia: ~78% (varia com os dados de treino)\
Features utilizadas:\
Número de gestações\
Nível de glicose\
Pressão sanguínea\
Espessura da pele\
Insulina\
Historico familiar\
IMC\
Idade

### 📝 Manual do Usuário
Preencha os campos com valores médicos reais\
Clique em "Realizar Predição"\
Interprete os resultados:\
🟢 <30%: Risco muito baixo\
🟡 30-70%: Risco moderado\
🔴 >70%: Alto risco\
Siga as recomendações exibidas na tela de resultados

### 📊 Exemplo de Entrada
Campo.........................................Valor Exemplo\
Nº de gestações...................................2\
Glicose (mg/dL)................................120\
Pressão sanguínea (mmHg)..............70\
Espessura da pele (mm)....................30\
Insulina (µU/mL)...............................100\
IMC (kg/m²)......................................30.5\
Função Pedigree Diabetes................0.5\
Idade (anos).......................................35


### 🚀 Como rodar o projeto

1. Clone ou baixe este repositório
2. Crie e ative um ambiente virtual no PyCharm
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt

Aplicação em Python com interface gráfica usando `Tkinter`, que prevê o risco de diabetes com base em dados clínicos.

### Como usar

1. Execute `src/treino_modelo.py` para treinar o modelo
2. Execute `src/interface.py` para abrir a interface
3. Preencha os dados e clique em **Prever**

Coloque o arquivo diabetes.csv em dados/
Dataset disponível em: https://www.kaggle.com/datasets/mathchi/diabetes-data-set



📌 Resultado
Exibe a probabilidade de diagnóstico de diabetes com base nos dados inseridos.

### Exemplos dos casos:

🔴 Caso de Alto Risco (Probabilidade > 70%)\
Nº de gestações:.................................8\
Glicose (mg/dL):..............................180\
Pressão sanguínea (mmHg):............90\
Espessura da pele (mm):..................35\
Insulina (µU/mL):.............................600\
IMC (kg/m²):....................................42.0\
Função Pedigree Diabetes:..............1.2\
Idade (anos):......................................50\
📌Características típicas:\
Glicose muito elevada (>160)\
IMC na faixa de obesidade\
Histórico familiar forte (pedigree alto)\
Idade mais avançada


🟡 Caso de Risco Moderado (40-70%)\
Nº de gestações:.................................3\
Glicose (mg/dL):..............................120\
Pressão sanguínea (mmHg):............85\
Espessura da pele (mm):..................25\
Insulina (µU/mL):.............................150\
IMC (kg/m²):....................................32.0\
Função Pedigree Diabetes:..............0.6\
Idade (anos):......................................45\
📌Características típicas:\
Glicose levemente elevada\
Pré-obesidade (IMC 30-35)\
Algum histórico familiar\
Idade intermediária

🟢 Caso de Baixo Risco (<40%)\
Nº de gestações:................................0\
Glicose (mg/dL):...............................90\
Pressão sanguínea (mmHg):............70\
Espessura da pele (mm):..................20\
Insulina (µU/mL):...............................80\
IMC (kg/m²):....................................22.0\
Função Pedigree Diabetes:..............0.2\
Idade (anos):......................................25\
📌Características típicas:\
Glicose normal\
IMC saudável\
Sem histórico familiar relevante\
Paciente jovem


### Para entrar em Contato:
Esmeralda Abtibol - esmeraldaabtibol@gmail.com
Manoel Leão - manoelarthur063@gmail.com
