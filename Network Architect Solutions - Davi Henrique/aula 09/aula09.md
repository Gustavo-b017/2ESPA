## Comandos Cisco
- ### Duividas:
  - '?' - help da cisco (mostras os comandos principais)
    - Super admim, (enter) passa de 1 em 1, (espaco) pula para o final

- ### Caso erre um comando:
  - 'crlt + shift + 6' - cancela o loop de erro

- ### SuperUser:
  - 'enable' [ 'en' - modo abreviado {so serve para entrar no modo de acesso}] - entra no modo superUsuario
  - 'configure terminal' [ 'conf t' - modo abreviado {so serve para entrar no modo de acesso}] - entra no ultimo modo de configuracao avançada

- ### Comandos:
  - 'exit' - volta 1 nivel de acesso
  
  - #### Para configurar senha:
    - 'enable' - entra no modo admin
    - 'configure terminal' - entra no modo super admin
    - 'enable secret  >senha<' - configura a senha 

  - #### Para tirar a senha:
    - 'no enable secret' - tira a sinal

  - #### Para configurar um IP e mascara
    - enable
    - conf t
    - 'interface >nome da porta< >porta<' [ 'inter >tab< - atalho] - entra em uma placa de rede para configura-la
    - no shutdown ['no shu >tab<' - compreta o comando] - liga a porta
    - 'ip address >n do ip< >mascara de rede<' - configura o ip e a mascara de rede
  
  - #### Salva as configuracoes
    - 'enable'
    - 'copy running-config startup-config' - salva a configuracao na memoria
    - enter

- ### 'no' - serve para fazer o contrario do comando





