from pyswip import Prolog
import pandas as pd
from sklearn.linear_model import LogisticRegression

# Instanciando e consultando a base lógica
prolog = Prolog()
prolog.consult("rede_social.pl")

# Carregando os dados tradicionais
df = pd.read_csv("dados_financeiros.csv")

# Função para extrair features lógicas com pyswip
def obter_grau_risco(nome):
    # Consulta a regra de risco recursivo no Prolog
    query = list(prolog.query(f"risco_conexao({nome}, daniel, Grau)"))
    if query:
        return query[0]["Grau"] # Retorna o grau numerico
    return 999 # Valor arbitrário para quem não tem conexão identificada

# Aplica a função no DataFrame
df['grau_risco_rede'] = df['cliente_id'].apply(obter_grau_risco)
print("Dados enriquecidos com Prolog:")
print(df)
print("-" * 30)

# Treinando o Classificador Estatístico
# Features: Renda, Score e o Grau de Risco calculado pelo Prolog
X = df[['renda_mensal', 'score_classico', 'grau_risco_rede']]
y = df['inadimplente_historico']

modelo = LogisticRegression()
modelo.fit(X, y)

print("Coeficientes Aprendidos:", modelo.coef_)
print("-" * 30)

# Teoria Neuro-Simbólica: Expressando Regras Estilo ProbLog
# Vamos calcular a probabilidade de risco para o cliente 'joao'
cliente_novo_X = X.iloc[[0]]
prob = modelo.predict_proba(cliente_novo_X)[0][1]

grau_joao = df.loc[df['cliente_id'] == 'joao', 'grau_risco_rede'].values[0]

print("Saída Relacional Estatística:")
print(f"{prob:.2f} :: risco(joao) :- conectado_a(joao, daniel, {grau_joao})")