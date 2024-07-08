from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Import routes module after app initialization to avoid circular import
from app import routes
