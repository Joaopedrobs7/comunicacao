# Cliente-Servidor com Sockets

Este é um projeto de aplicação cliente-servidor utilizando sockets TCP (AF_INET, SOCK_STREAM), operando em um servidor local. A aplicação foi projetada para consultar o valor de mercado de criptomoedas em tempo real usando a API da Coingecko.

## Protocolos de Confiabilidade

Para garantir a transferência confiável de dados, a aplicação utiliza os seguintes mecanismos:

- **Checksum**: Para verificar a integridade dos dados.
- **Timer**: Para controlar o tempo de espera por uma resposta.
- **Sequence Numbers**: Para ordenar as mensagens enviadas e recebidas.
- **Ack/Nack**: Para confirmar recebimentos de mensagens.

## Como Usar

### Pré-requisitos

Certifique-se de ter o Python e o pip instalados em sua máquina antes de continuar.

### Instalação

1. Clone o repositório para sua máquina local:
   ```bash
   git clone https://github.com/Joaopedrobs7/comunicacao.git
2. Navegue até o diretório do projeto e instale as dependências:
   ```bash
	pip install -r requirements.txt
   
### Execução

1. Abra dois terminais: um para o servidor e outro para o cliente.
2. No terminal do servidor, inicie o servidor com o comando adequado
   ```bash
   python3 servidor.py
4. No terminal do cliente, inicie o cliente com o comando adequado
   ```bash
   python3 cliente.py
6. Digite o nome de uma criptomoeda no terminal do cliente para consultar seu valor.

### Fluxo de Comunicação

- **Recebimento e Teste de Integridade**: Se a mensagem for recebida corretamente, o servidor enviará um Ack (confirmação) ou Nack (erro) com um número de identificação.
- **Consulta à API**: Se a moeda existir, o servidor retornará o valor atualizado da Coingecko. Caso contrário, informará que a moeda não foi encontrada.
- **Falhas de Comunicação**: Se um Nack for recebido, o cliente deve retransmitir a mensagem.

### Encerrando a Aplicação

Para encerrar a aplicação, o cliente pode enviar o comando `exit`. Isso não passará por testes de integridade, o cliente em questao sera desconectado. E o servidor continuara escutando conexões.
