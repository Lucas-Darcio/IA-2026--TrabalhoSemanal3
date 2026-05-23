# IA-2026--TrabalhoSemanal3

## Análise de Risco de Crédito Híbrido em Redes Sociais

Este projeto implementa uma arquitetura híbrida de Inteligência Artificial que une Aprendizado Relacional Simbólico (Prolog) e Incerteza Probabilística (Machine Learning via Python/Scikit-Learn).

## How to

### Pré-requisitos

- _Python 3.9 or later_

- _SWI-Prolog 8.4.2_

### Passos

1. Clone o repositório (SSH):

```
git clone git@github.com:Lucas-Darcio/IA-2026--TrabalhoSemanal3.git
```

2. Instale o pyswip, pandas e scikit-learn:

```
pip install pyswip pandas scikit-learn
```

3. Abra o diretório da atividade:

```
cd IA-2026--TrabalhoSemanal3
```

4. Para rodar o código da atividade:

```
python main.py
```

## Análise Crítica e XAI (Explainable AI)

Em modelos puramente estatísticos, como redes neurais tradicionais, o processo de tomada de decisão é muitas vezes uma caixa-preta. O uso da Lógica de Primeira Ordem, nesse caso usando Prolog, integrada à Estatística (SRL) resolve esse problema tornando o sistema:

1. Explicável e Auditável: Sabemos exatamente por que um usuário recebeu uma penalidade em sua análise de risco. A regra lógica risco_conexao nos mostra o caminho exato no grafo social (ex: João transferiu para Ana, que transferiu para Carlos, que transferiu para o inadimplente Daniel).

2. Justo: Em vez de assumir certezas absolutas e penalizar alguém apenas por uma conexão distante em uma rede de transações, a Regressão Logística calibra o "peso" dessa variável.

3. Híbrido: O Prolog estrutura os dados complexos, modelando a realidade relacional, enquanto o Python lida com os ruídos e a incerteza do mundo real calculando as probabilidades

## Resultado:

```
Dados enriquecidos com Prolog:
  cliente_id  renda_mensal  score_classico  inadimplente_historico  grau_risco_rede
0       joao          5200             750                       0                3
1        ana          3100             610                       0                2
2     carlos          1800             420                       1                1
------------------------------
Coeficientes Aprendidos: [[-1.69430254e-02 -2.47733394e-03 -1.19686393e-05]]
------------------------------
Saída Relacional Estatística:
0.00 :: risco(joao) :- conectado_a(joao, daniel, 3)

```

O Prolog calculou que Carlos tem grau 1 (transfere direto para Daniel), Ana tem grau 2 (transfere para Carlos), e João tem grau 3.

O código tenta prever a probabilidade de João se tornar inadimplente, e deu 0%, o que parece suspeito, mas o perfil de joão é da pessoa que mais ganha, tem o melhor score, e é mais distante do foco de "infecção" financeira, que é o Daniel. Para o algoritmo ele é o mais seguro possível, além disso o modelo foi alimentado com pouquissímos dados, somente 3 linhas.
