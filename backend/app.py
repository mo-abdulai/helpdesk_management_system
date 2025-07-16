# app.py
from flask import Flask, request, jsonify
from models import db, Ticket, Asset

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///helpdesk.db'
db.init_app(app)

@app.route('/tickets', methods=['POST'])
def create_ticket():
    data = request.get_json()
    ticket = Ticket(title=data['title'], description=data['description'], priority=data['priority'])
    db.session.add(ticket)
    db.session.commit()
    return jsonify({'message': 'Ticket created'}), 201

@app.route('/tickets', methods=['GET'])
def list_tickets():
    tickets = Ticket.query.all()
    return jsonify([{'id': t.id, 'title': t.title, 'status': t.status} for t in tickets])
