## Numero de ip:
* As 3 primeiras partes significa o numero da rede, e a ultima parte e a maquina 
  * ex: 192.168.0.1 -- ([192.168.0] rede, [1] computador )
  * Nao se deve usar o 1 nem o ultimo ip (0 e 255)
    * Nao se usa os ips 192.168.0.0 e nem o 198.168.0.255
      * 192.168.0.0 - rede
      * 198.168.0.255 - broadcast
    * No maximo se pode usar 253 computadores na mesma rede

## Mascara de rede:
* Numero que separa a parte do endereco IP e dos host em uma rede
* Maximo: 255.255.255.[numero do host]
* O endereco ip e a mascara de redes sao formados por 4 octetos (000.000.000 - define o numero da rede; .0 -- define o dispositivo)
* Os 3 primeiros octetos define o numero da rede, e o ultimo o dispositivo

## SubRede:
* E uma subdivisao de uma rede maior. 
* O uso de uma subrede permite que uma rede grande seja dividada em pedacos menores, facilitando a gestao e aumentando a eficiencia.
* Para criar uma subrede:
  * 1. Pego um binario emprestado do ultimo octeto (em bianrio: 11111111.11111111.11111111.10000000 [25 numeros 1]) -- [255.255.255.128]
    * Com isso criou as subredes subredes:
      * 192.168.0.0 -- subrede01
      * 192.168.0.1 -- primeiro IP
      * 192.168.0.126 -- ultimo IP
      * 192.168.0.127 -- broadcast <br>
      * Mascara de rede: 255.255.255.128 (125 PCs)

      * 192.168.0.128 -- subrede 02
      * 192.168.0.129 -- primeiro IP
      * 192.168.0.254 -- ultimo IP
      * 192.168.0.255 -- broadcast
      * Mascara de rede: 255.255.255.128 (125 PCs)