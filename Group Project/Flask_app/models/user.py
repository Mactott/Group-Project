from Flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from server import db

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$')

class User:
    def __init__(self,data):
        self.id = data["id"]
        self.email = data["email"]
        self.password = data["password"]

    @classmethod
    def save(cls,data):
        query = """INSERT INTO user (email,password) VALUES (%(email)s,%(password)s)"""
        connectToMySQL(db).query_db(query,data)

    @classmethod
    def loggin(cls,email):
        query = """SELECT * FROM user WHERE email = %(email)s"""
        data = {"email": email}
        results = connectToMySQL(db).query_db(query,data)
        if len(results) == 0:
            return None
        else:
            return cls(results[0])

    @classmethod
    def get_all(cls):
        query = """SELECT * FROM user"""
        results = connectToMySQL(db).query_db(query)
        all_users = []
        for row in results:
            all_users.append(row)
        return all_users
    
    @classmethod
    def get_user_by_email(cls,data):
        query = """SELECT * FROM user WHERE email = %(email)s"""
        results = connectToMySQL(db).query_db(query,data)
        return(cls(results[0]))

    @staticmethod
    def valid_check(data_dic):
        is_valid = True
        if not EMAIL_REGEX.match(data_dic["email"]):
            flash("Invalid email","email")
            is_valid = False
        if not PASSWORD_REGEX.match(data_dic["password_raw"]):
            flash("Passwords are special", "password")
            is_valid = False
        return is_valid