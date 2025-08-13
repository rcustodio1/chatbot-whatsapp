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
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
bash
2. Instale as dependências:
```bash
pip install -r requirements.txt
bash
3. Configure as variáveis de ambiente (exemplo):
```bash
TWILIO_ACCOUNT_SID

TWILIO_AUTH_TOKEN

TWILIO_PHONE_NUMBER
bash
4. Execute o servidor Flask:
```bash
python app.py
bash
5. Exponha o servidor local usando ngrok (ou equivalente):
```bash
ngrok http 5000
bash
6. Configure no Twilio a URL pública gerada pelo ngrok apontando para o endpoint do webhook, por exemplo:
```bash
https://abc123.ngrok.io/webhook
bash
## Estrutura do projeto
```bash
├── app.py               # Arquivo principal do Flask
├── requirements.txt     # Dependências do projeto
├── README.md            # Este arquivo
└── .env                 # Variáveis de ambiente (não versionar)
bash
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
