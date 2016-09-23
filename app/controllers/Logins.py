from system.core.controller import *
import math

class Logins(Controller):
	def __init__(self, action):
		super(Logins, self).__init__(action)
		# Note that we have to load the model before using it
		self.load_model('Login') #this is the model name

	def index(self):
		return self.load_view('/login/index.html')

	def welcome(self):
		return self.load_view('/login/welcome.html')

	def add(self):
		user_details = {
			'first_name': request.form['first_name'],
			'last_name': request.form['last_name'],
			'email': request.form['email'],
			"password" : request.form['password'],
			"cPassword" : request.form['cPassword']
		}
		create_user = self.models['Login'].add_user(user_details)#this is referring to the
		print create_user
		if type(create_user) is list:
			displayErrors = create_user
			flash(create_user)
			return redirect('/')
		else:
			return redirect('/logins/welcome')

	def sign(self, email):

		check = self.models['Login'].login_user(email)



		'''

			

		
		if create_user != []
			for message in create_user['errors']:
				flash(message, 'regis_errors')
			return redirect('/login/index.html')
			print create_user # either its gonna return the errors or its the success message. First find out what create_user returns, then decide what is the next fork
		# if create_user gives me the errors, then display the errors, if create_user gives me (sth that is not errors, it should lead me to the success html)
		else:
			return redirect('login/welcome.html')



		#if create_user['status'] == True; #what is this status?
			#session['first_name'] = create_user['login']['first_name']#why need to add to session?
			#session['last_name'] = create_user['login']['last_name']
			#session['email'] = create_user['login']['email']
   

	def welcome(self):
		return self.load_view('login/welcome.html')




	This is how a method with a route parameter that provides the id would work
	We would set up a GET route for this method
	def show_1(self, id):
		# Note how we access the model using self.models
		course = self.models['Login'].display_1_by_id(id)
		return self.load_view('show.html')
'''






