## Octeto misto:
* quando se divide uma mascara para rede e outra para host

## Broadcast:
* manda msg para todas as maquinas
* O numero do Broadcast é o ip da proxima rede - 1

## Para dividir redes:
* Contas:
    * 256 - 128 = 128 portas para cada
    * redes disponiveis: numero de portas -2

* 192.168.0.0 /24
    * Mascara de rede: 255.255.255.0

    * IP: 192.168.0.0
    * Intervalo: 192.168.0.1 ~~ 192.168.0.254
    * Boadcast: 192.168.0.255

* 192.168.0.0 /25
    * Se divide em 2 subRedes
    * Mascara de rede: 255.255.255.128

    * Rede 1:
        * IP: 192.168.0.0
        * Intervalo: 192.168.0.1 ~~ 192.168.0.126
        * Boadcast: 192.168.0.127

    * Rede 2:
        * IP: 192.168.0.128
        * Intervalo: 192.168.0.129 ~~ 192.168.0.254
        * Boadcast: 192.168.0.255

* 192.168.0.0 /26
    * Se divide em 4 subRedes
    * Mascara de rede: 255.255.255.192

    * Rede 1:
        * IP: 192.168.0.0
        * Intervalo: 192.168.0.1 ~~ 192.168.0.62
        * Boadcast: 192.168.0.63

    * Rede 2:
        * IP: 192.168.0.64
        * Intervalo: 192.168.0.65 ~~ 192.168.0.126
        * Boadcast: 192.168.0.127

    * Rede 3:
        * IP: 192.168.0.128
        * Intervalo: 192.168.0.129 ~~ 192.168.0.190
        * Boadcast: 192.168.0.191

    * Rede 4:
        * IP: 192.168.0.192
        * Intervalo: 192.168.0.193 ~~ 192.168.0.254
        * Boadcast: 192.168.0.255

* 192.168.0.0 /27
    * Se divide em 8 subRedes
    * Mascara de rede: 255.255.255.224

    * Rede 1:
        * IP: 192.168.0.0
        * Intervalo: 192.168.0.1 ~~ 192.168.0.30
        * Boadcast: 192.168.0.31

    * Rede 2:
        * IP: 192.168.0.32
        * Intervalo: 192.168.0.33 ~~ 192.168.0.62
        * Boadcast: 192.168.0.63

    * Rede 3:
        * IP: 192.168.0.64
        * Intervalo: 192.168.0.65 ~~ 192.168.0.94
        * Boadcast: 192.168.0.95

    * Rede 4:
        * IP: 192.168.0.96
        * Intervalo: 192.168.0.97 ~~ 192.168.0.126
        * Boadcast: 192.168.0.127

    * Rede 5:
        * IP: 192.168.0.128
        * Intervalo: 192.168.0.129 ~~ 192.168.0.158
        * Boadcast: 192.168.0.159

    * Rede 6:
        * IP: 192.168.0.160
        * Intervalo: 192.168.0.161 ~~ 192.168.0.190
        * Boadcast: 192.168.0.191

    * Rede 7:
        * IP: 192.168.0.192
        * Intervalo: 192.168.0.123 ~~ 192.168.0.222
        * Boadcast: 192.168.0.223

    * Rede 8:
        * IP: 192.168.0.224
        * Intervalo: 192.168.0.225 ~~ 192.168.0.254
        * Boadcast: 192.168.0.255
