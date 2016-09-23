from system.core.model import *
import os, sys
import re

class Login(Model):
    def __init__(self):
        super(Login, self).__init__()


        
    def add_user(self, info):
      EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
      errors = []
      hashed_pw = self.bcrypt.generate_password_hash(info['password'])
      if not info['first_name']:
        errors.append('Please provide a First Name ')
      elif len(info['first_name']) < 2:
        errors.append('First Name must at least 2 characters long ')
      if not info['last_name']:
        errors.append('Please provide a Last Name ')
      elif len(info['last_name']) < 2:
        errors.append('Last Name must be at least 2 characters long ')
      if not info['email']:
        errors.append('Please provide an email ')
      elif not EMAIL_REGEX.match(info['email']):
        errors.append('Invalid email ')
      if not info['password']:
        erros.append('Please provide a password ')
      elif len(info['password']) < 8:
        errors.append('Password must be at least 8 characters long ')
      elif info['password'] != info['cPassword']:
        errors.append('Passwords do not match ')
      if errors == []:
        query = "INSERT INTO login(first_name, last_name, email, password) VALUES (:first_name, :last_name, :email, :hashed_pw)"
        user_details = { 'first_name': info['first_name'], 'last_name': info['last_name'], 'email': info['email'], 'hashed_pw': hashed_pw}
        result = self.db.query_db(query, user_details)
        return result
      else:
        return errors

    def login_user(self, info):
      password = info['password']
      query = "SELECT * FROM login WHERE email = :email LIMIT 1"
      user_data = {'email': info['email']}
      # same as query_db() but returns one result
      user = self.db.get_one(query, user_data)
      if user:
      # check_password_hash() compares encrypted password in DB to one provided by user logging in
        if self.bcrypt.check_password_hash(user.pw_hash, password):
          return user
        # Whether we did not find the email, or if the password did not match, either way return False
          return False










    def display_1_by_id(self, id):
      query = "SELECT * FROM login WHERE id = :id"
      data = { 'id': id} #?
      return self.db.query_db(query, data)

    def display_all_login(self):
      return self.db.query_db("SELECT * FROM login")