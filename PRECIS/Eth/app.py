import json
from flask import Flask, Response, request, jsonify
from marshmallow import Schema, fields, ValidationError
from web3 import Web3
# web3.py instance
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
w3.eth.defaultAccount = w3.eth.accounts[1]
# Get stored abi and contract_address
with open("data.json", 'r') as f:
    datastore = json.load(f)
    abi = datastore["abi"]
    contract_address = datastore["contract_address"]
def check_gender(data):
    valid_list = ["male", "female"]
    if data not in valid_list:
        raise ValidationError(
            'Invalid gender. Valid choices are'+ valid_list
        )
#For api validations
class UserSchema(Schema):
    name = fields.String(required=True)
    gender = fields.String(required=True, validate=check_gender)
# Initializing flask app
app = Flask(__name__)
# api to set new user every api call
@app.route("/blockchain/user", methods=['POST'])
def user():
    # Create the contract instance with the newly-deployed address
    user = w3.eth.contract(address=contract_address, abi=abi)
    body = request.get_json()
    result, error = UserSchema().load(body)
    if error:
        return jsonify(error), 422
    tx_hash = user.functions.setUser(
        result['name'],result['gender']
    ).transact()
    # Wait for transaction to be mined...
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    user_data = user.functions.getUser().call()
    return jsonify({"data": user_data}), 200

Run below commands to start your server.
	code:

$ FLASK_APP=app.py flask run

	Call api using curl.
	Вызов api с помощью curl.

	code:

$ curl -H "Content-Type: application/json" --request POST -d '{"name":"John Doe","gender":"male"}' http://localhost:5000/blockchain/user

You can find whole code here. https://github.com/NehaGhogale/basic_user_contract
