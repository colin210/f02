from flask import Flask,render_template
from flask_bootstrap  import  Bootstrap
from nameForm import NameForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'colin'
bootstrap = Bootstrap(app)


@app.route('/',  methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('user.html', form=form, name=name)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)

if __name__ == '__main__':
    app.run(debug=True)
