from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'secret-key-untuk-flash'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Validasi sederhana
        if not name or not email or not message:
            flash('Semua field wajib diisi!', 'danger')
            return redirect(url_for('contact'))

        # Di sini biasanya proses simpan ke database atau kirim email
        flash('Pesan Anda telah terkirim. Terima kasih!', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)