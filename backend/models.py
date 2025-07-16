# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    status = db.Column(db.String(20), default='Open')  # Open, In Progress, Closed
    priority = db.Column(db.String(10))  # Low, Medium, High
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

class Asset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    serial_number = db.Column(db.String(100), unique=True)
    assigned_to = db.Column(db.String(100))
    status = db.Column(db.String(20))  # In Use, Available, Retired
