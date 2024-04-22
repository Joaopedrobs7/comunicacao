## Grupo: Gabriel Reis; João Pedro Batista; João Pedro Nóbrega; Mathews Ivo; Théo Moura.
## Nossa aplicação cliente servidor, via sockets, cuja confiabilidade é atestada pelo protocolo TCP(AF_INET, SOCK_STREAM), rodando em servidor local, intitula receber o nome de uma criptomoeda, registradas na Coingecko, e retornar o valor de mercado dela, em tempo real. 
### Para tal, uma série de protocolos que pretendem viabilizar o transporte confiável de dados foram aplicados:
```
Checksum;
Timer;
Sequence Numbers;
Ack/Nack;
```
### Uso:

 clone o repositório em sua máquina local;
 ```
  git clone  https://github.com/Joaopedrobs7/comunicacao.git
```
Instale o arquivo de requirements com o comando:
```
 pip install requirements.txt
```
```
Abra dois terminais, um para o servidor e um para o cliente, em ordem: para o cliente acessar o servidor, este precisa estar “rodando”.
Digite o nome de uma criptomoeda no terminal do cliente;
```
Se a mensagem for recebida e passar pelo teste de integridade, o servidor devolverá um Ack ou Nack e número de identificação para o cliente,  que saberá que sua mensagem foi recebida.

Caso um ack tenha sido recebido, o servidor operará de duas formas: 

Caso Moeda Existente -> O servidor devolverá o valor da moeda informada, registrada no Coingecko, através do uso de sua API;
Caso Moeda Inexistente -> O servidor informa que a moeda não foi encontrada e impele ao cliente um novo input;
	
Caso um Nack seja recebido, significa que a comunicação foi estabelecida, mas não foi aprovado no teste de integridade e solicita uma retransmissão com o cliente.

	
Para o caso do cliente dar o comando exit, não acontecerá teste de integridade, meramente deixando a aplicação e fechado o servidor de imediato.  
