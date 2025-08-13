from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/', methods=['POST'])
def whatsapp_bot():
    msg = request.form.get('Body', '').strip()
    sender = request.form.get('From', '')

    response = MessagingResponse()
    reply = response.message()

    if not msg:
        reply.body("Mensagem vazia recebida. Envie 'Oi' para começar.")
    elif msg.lower() == "oi":
        reply.body("Olá! Quer agendar um horário? Me diga o dia (ex: 28/07)")
    elif "/" in msg:
        reply.body("Estes são os horários disponíveis:\n- 14h\n- 15h\n- 17h\nQual você escolhe?")
    elif msg in ["14", "15", "17"]:
        reply.body(f"Agendamento confirmado para {msg}h ✅")
    else:
        reply.body("Desculpe, não entendi. Envie 'Oi' para começar.")

    return str(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
