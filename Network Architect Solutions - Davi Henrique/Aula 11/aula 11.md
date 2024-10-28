## roteador - 2621XM
* desliga o router
* coloca o drive WIC-1T
* liga o router
* cabo vermelho com relogio (seriel DCE)
* liga na porta serial 0/0 (usado para conectar 2 ruters)


# Configurar o reouter:
* en
* conf t
* interface serial 0/0 (int s0/0)
* ip address 10.0.0.1 255.255.255.252
* clock rate 64000 - define a velocidade da rede
* no shu
* end
* --------
* conf t
* interface fastEthernet 0/0 (int f0/0)
* ip address 192.168.0.1 255.255.255.0
* n sh
* end
* wr -para salvar as conf no router
* -----------
* router ospf 1 - um dos protocolos de redes (abilita o protocolo de roteamento)
  * network 10.0.0.0 {0.0.0.3 (mascara coringa)} area 0 - define a rede do roteador que ele precisa conhecer
  * network 192.168.0.0 0.0.0.255 area 0- define a rede do sistema de sp que ele precisa conhecer
  * diz que essas redes podem conversar
* end
* wr
* ---------
* show ip route - conferir se ta tudo conectado
* show ip ospf neighbor - mostra as redes que ele esta conversando