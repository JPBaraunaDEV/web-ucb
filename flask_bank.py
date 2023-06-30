from flask import Flask, render_template, url_for, flash, redirect
from forms import RegisterForm, LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'd2a2820f06c09fce64f9185bbc553c49'

transacoes = [
    {
        'usuario':'Joao',
        'conta':'1',
        'valor': 'R$100',
        'date_transferencia':'Jun 21, 2023'
    }, 
    {
        'usuario':'Ana',
        'conta':'2',
        'valor': 'R$1100',
        'data_transferencia':'Jun 22, 2023'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html', title='Sobre')

@app.route("/conta")
def conta():
    return render_template('conta.html', transacoes=transacoes)

@app.route("/registrar", methods=['GET', 'POST'])
def registrar():
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'Conta criada com sucesso {form.usuario.data}!', 'success')
        return redirect(url_for('conta'))
    return render_template('registrar.html', title='Registrar', form=form)


@app.route("/login",  methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@barabank.com' and form.senha.data == '123':
            flash('Log In Efetuado!', 'success')
            return redirect(url_for('conta'))
        else:
            flash('Autenticação inválida!', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)