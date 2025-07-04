from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = '7555243004:AAEKoSZAgZ53QLhRv5dnMF1c3hy8qOo-dKw'
ADMIN_IDS = ['6855997739']

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def submit():
    ismi = request.form.get('ismi')
    kurs = request.form.get('kurs')
    tel1 = request.form.get('tel1')
    tel2 = request.form.get('tel2')
    izoh = request.form.get('izoh')

    message = f"""📝 <b>Yangi ro'yxatdan o'tish:</b>
👤 <b>Ismi:</b> {ismi}
📘 <b>Kursi:</b> {kurs}
📞 <b>Telefon 1:</b> {tel1}
📞 <b>Telefon 2:</b> {tel2 if tel2 else '---'}
💬 <b>Izoh:</b> {izoh if izoh else '---'}"""

    for admin_id in ADMIN_IDS:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {
            'chat_id': admin_id,
            'text': message,
            'parse_mode': 'HTML'
        }
        try:
            requests.post(url, data=payload)
        except:
            pass

    return "<h3>✅ Ma'lumot yuborildi. Tez orada siz bilan bog'lanamiz!</h3>"

@app.route('/favicon.ico')
def favicon():
    return '', 204

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
