from flask import Flask, render_template,url_for,flash,redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] ='1b2d57be2ee6a3d2eb14a474eafae7b9'

posts = [ 
	{
		'author': 'Nguyen Quy Duy',
		'title': 'Blog Post 1',
		'content': 'First posted content',
		'date_posted': 'Sep 21,2018',
	},

	{
		'author':'Duy Nguyen',
		'title': 'Blog Post 2',
		'content': 'Second posted content',
		'date_posted': 'Sep 22,2018',
	}

]
@app.route("/")

@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():	
	return render_template('about.html',title='About')

@app.route("/register", methods=['GET','POST'])
def register():	
	form= RegistrationForm()
	if form.validate_on_submit(): 
		flash(f'Account created for {form.username.data}!','success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():	
	form= LoginForm()
	return render_template('login.html', title='Login', form=form)


if  __name__=='__main__' : 
	 app.run(debug=True)