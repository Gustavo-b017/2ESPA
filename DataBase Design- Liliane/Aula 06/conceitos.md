## Cardinalidade minima e maxima:
    * (cardMin, CardMax) = (X,Y)
      * maxima: numero maximo de ocorrencia em uma entidade
      * minimo: numero maximo de ocorrencias
    * Possiveis cardinalidades:
      * (1, 1) - no minimo 1 e nao mais que isso
      * (1, N) - Pelo menos um e no maximo varios
      * (0, 1) - Pode estar vazio ou no maximo 1
      * (0, N) - Pode estar vazio ou no maximo varios
      * (N, N) - Sempre muitos
    * Ex:
      * 1:1 -> homem(0,1)  -- casar -- mulher(0,1)
      * 1:N -> Empregado(1,1)  -- possui -- Dependente(0,N)
      * N:N -> Medico(1,N) -- consulta -- Pacinte(N,N)