from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Telegram bot tokeni (o'zingizning bot tokeningizni bu yerga yozing)
BOT_TOKEN = '7555243004:AAEKoSZAgZ53QLhRv5dnMF1c3hy8qOo-dKw'

# Admin Telegram IDlari (har bir adminning chat_id si bo'lishi kerak)
ADMINS = [
    6855997739
]

@app.route('/favicon.ico')
def favicon():
    # Hech narsa yubormaydi, lekin 200 OK javob beradi
    return '', 204

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Formadan ma'lumotlarni olish
        ismi = request.form['ismi']
        kurs = request.form['kurs']
        tel1 = request.form['tel1']
        tel2 = request.form.get('tel2', '')
        izoh = request.form.get('izoh', '')

        # Yuboriladigan xabar matni
        message = f"""
📥 <b>Yangi Ariza:</b>
👤 <b>Ismi:</b> {ismi}
📚 <b>Kurs:</b> {kurs}
📞 <b>Telefon 1:</b> {tel1}
📞 <b>Telefon 2:</b> {tel2 if tel2 else '—'}
📝 <b>Izoh:</b> {izoh if izoh else '—'}
        """

        # Har bir adminga xabar yuborish
        for admin_id in ADMINS:
            url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
            data = {
                'chat_id': admin_id,
                'text': message,
                'parse_mode': 'HTML'
            }
            try:
                requests.post(url, data=data)
            except Exception as e:
                print(f"Xatolik yuz berdi: {e}")

        return "✅ Ma'lumotlar adminlarga yuborildi!"

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
