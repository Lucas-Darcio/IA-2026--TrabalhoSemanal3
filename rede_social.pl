% Fatos de transacoes (conexoes diretas)
transacao_entre(joao, ana, 1500).
transacao_entre(ana, carlos, 800).
transacao_entre(carlos, daniel, 50).

% Historico de Inadimplencia classico
inadimplente(daniel).

% Regra de propagacao de risco por conectividade recursiva
% Caso base: O grau de risco e 1 se existe uma transacao direta.
risco_conexao(X, Y, 1) :- 
    transacao_entre(X, Y, _).

% Passo recursivo: O grau aumenta conforme a distancia na rede.
risco_conexao(X, Y, Grau) :- 
    transacao_entre(X, Z, _), 
    risco_conexao(Z, Y, GrauAnterior), 
    Grau is GrauAnterior + 1.