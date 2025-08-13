# Chatbot WhatsApp com Flask e Twilio

## Descrição

Este projeto é um chatbot para WhatsApp desenvolvido em Python utilizando o framework Flask para o backend e a API do Twilio para integração com o WhatsApp. O bot responde automaticamente às mensagens recebidas.

---

## Tecnologias usadas

- Python 3.13.5
- Flask  
- Twilio API para WhatsApp  
- ngrok (para expor localmente o servidor)

---

## Como rodar o projeto

1. Clone o repositório:

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

2. Instale as dependências:

pip install -r requirements.txt

3. Configure as variáveis de ambiente (exemplo):

TWILIO_ACCOUNT_SID

TWILIO_AUTH_TOKEN

TWILIO_PHONE_NUMBER

4. Execute o servidor Flask:

python app.py

5. Exponha o servidor local usando ngrok (ou equivalente):

ngrok http 5000

6. Configure no Twilio a URL pública gerada pelo ngrok apontando para o endpoint do webhook, por exemplo:

https://abc123.ngrok.io/webhook

## Estrutura do projeto

├── app.py               # Arquivo principal do Flask
├── requirements.txt     # Dependências do projeto
├── README.md            # Este arquivo
└── .env                 # Variáveis de ambiente (não versionar)

## Como usar

Envie uma mensagem para o número WhatsApp configurado no Twilio.

O chatbot responderá automaticamente conforme programado no webhook Flask.

## Melhorias futuras

Adicionar processamento de linguagem natural (NLP)

Salvar histórico de conversas

Implementar comandos personalizados

Criar interface administrativa para gerenciar respostas

## Autor

Rafael Custódio

## Licença

Este projeto está licenciado sob a MIT License.
