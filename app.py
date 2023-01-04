# from flask import Flask, render_template, request, redirect, url_for
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Test123!@localhost/users'
# db = SQLAlchemy(app)

# if __name__ == "__main__":
#     app.run(host="localhost", port=5006, debug=True)
    
from App import app

if __name__ == "__main__":
    app.run(host="localhost", port=5001, debug=True)