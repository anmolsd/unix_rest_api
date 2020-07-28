#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 02:57:29 2020

@author: anmolsingh
"""
from datetime import datetime as dt
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import extract, func
from indexPageSource import indexPageSource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

db = SQLAlchemy(app)

possibleFields = {'amount': 'float', 'date': 'dt.fromisoformat', 'id': 'int', 'purpose': 'str', 'vendor': 'str', 'location': 'str'}
possibleFieldsStringDataTypes = {'amount': 'float e.g. 29.95', 'date': 'hyphen separated string YYYY-MM-DD', 'id': 'int e.g. 1', 'purpose': 'string e.g. coffee', 'vendor': 'string e.g. Starbucks 6th Street', 'location': 'string of the form "City, State Abbrev, Country Abbrev", e.g. San Francisco, CA, USA'} 

class Transaction(db.Model):
    __tablename__ = "unixTransactions"
    transaction_id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.DateTime, unique = True)
    amount = db.Column(db.Float)
    purpose = db.Column(db.String)
    vendor = db.Column(db.String)
    location = db.Column(db.String)
    
def getDataFromFilteredObject(objectX):  
    result = {}
    for row in objectX:
        result[len(result) + 1] = {
            "ID": row.transaction_id,
            "Date": str(row.date),
            "Amount": row.amount,
            "Purpose": row.purpose,
            "Vendor": row.vendor,
            "Location": row.location,
        }
    return jsonify(result)

def dataTypesCheck():
    for i in request.args.keys():
        if i not in possibleFields:
            return """<h1> Invalid arguments! Only possibilities are: <br><br> amount, date, id, purpose, vendor, location </h1>"""
        else:
            try:
                eval(possibleFields[i] + '("' + (request.args[i]) + '")')
            except:
                return "<h1> Type Error! " + i + " must be " + possibleFieldsStringDataTypes[i] + "</h1>"
    else:
        return True

def getTidbit(arg):
    return '' if arg not in request.args else request.args[arg]

@app.route('/', methods = ['GET'])
def home():
    return indexPageSource

@app.route('/get', methods = ['GET'])
def get():
    if dataTypesCheck() != True:
        return dataTypesCheck()
    if len(request.args) == 0:
        allData = db.session.query(Transaction).filter(True)
        return getDataFromFilteredObject(allData)
    try:
        t_id_cond = Transaction.transaction_id == (request.args['id'])
    except:
        t_id_cond = True
    try:
        date_to_find = fromisoformat(request.args['date'])
        date_cond = extract('day', Transaction.date) == date_to_find.day and extract('month', Transaction.date) == date_to_find.month and extract('year', Transaction.date) == date_to_find.year
    except:
        date_cond = True
    try:
        amount_cond = Transaction.amount == request.args['amount']
    except:
        amount_cond = True
    try:
        purpose_cond = func.lower(request.args['purpose']) == func.lower(Transaction.purpose)
    except:
        purpose_cond = True
    try:
        vendor_cond = func.lower(request.args['vendor']) == func.lower(Transaction.vendor)
    except:
        vendor_cond = True
    try:
        location_cond = func.lower(request.args['location']) == func.lower(Transaction.location)
    except:
        location_cond = True
    row = db.session.query(Transaction).filter(t_id_cond, date_cond, amount_cond, purpose_cond, vendor_cond,location_cond)
    if row.first() == None:
        return {"NotFoundError": True}
    else:
        return getDataFromFilteredObject(row)
    
@app.route('/post', methods = ['GET', 'POST'])
def post():
    if dataTypesCheck() != True:
        return dataTypesCheck()
    try:
        assert 'id' in request.args.keys() and 'amount' in request.args.keys() and 'date' not in request.args.keys() and db.session.query(Transaction).filter(Transaction.transaction_id == int(request.args['id'])).first() == None
    except:
        return "<h1> Invalid POST Request. You must provide a unique integer id and an amount, and must not have a date"
    entry = Transaction(transaction_id = int(request.args['id']), amount = float(request.args['amount']), date = dt.now().isoformat(), purpose = getTidbit('purpose'), vendor = getTidbit('vendor'), location = getTidbit('location'))
    db.session.add(entry)
    db.session.commit()
    return "<h1> Successfully added entry to Database! </h1>"

@app.route('/put', methods = ['GET', 'PUT'])
def put():
    if dataTypesCheck() != True:
        return dataTypesCheck()
    try:
        assert 'id' in request.args.keys() and 'date' not in request.args.keys() and db.session.query(Transaction).filter(Transaction.transaction_id == int(request.args['id'])).first() is not None
    except:
        return "<h1> Invalid PUT request. ID not supplied, or it does not exist. Date can not be modified. </h1>"
    row = db.session.query(Transaction).filter(Transaction.transaction_id == int(request.args['id'])).first()
    row.amount = row.amount if getTidbit('amount') == '' else getTidbit('amount')
    row.vendor = row.vendor if getTidbit('vendor') == '' else getTidbit('vendor')
    row.purpose = row.purpose if getTidbit('purpose') == '' else getTidbit('purpose')
    row.location = row.location if getTidbit('location') == '' else getTidbit('location')
    db.session.commit()
    return "<h1> Update Successful! </h1>"

@app.route('/delete', methods = ['GET', 'DELETE'])
def delete():
    if dataTypesCheck() != True:
        return dataTypesCheck()
    try:
        row = db.session.query(Transaction).filter(Transaction.transaction_id == int(request.args['id'])).first()
        assert 'id' in request.args.keys() and row is not None
    except:
        return "<h1> Only 1 argument is considered for deletions - the unique ID - and it must exist </h1>"
    db.session.delete(row)
    db.session.commit()
    return '<h1> Successfully deleted given transaction </h1>'
    

    
if __name__ == "__main__":
    app.run(debug = True)
