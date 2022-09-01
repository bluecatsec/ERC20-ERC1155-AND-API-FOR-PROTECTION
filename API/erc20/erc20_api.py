from flask import Flask,request,abort
import time
from web3 import Web3, HTTPProvider
import contract_abi

contract_address     = ""
wallet_private_key   = ""
wallet_address       = ""

w3 = Web3(HTTPProvider("http://0.0.0.0:7656/"))
contract = w3.eth.contract(address = contract_address, abi = contract_abi.abi)

app = Flask(__name__)
@app.route('/')
def hello():
    return 'hello,world'

@app.route("/testGet", methods=['GET'])
def testGet():
    name = request.args.get('name','')
    age = request.args.get('age','')
    return {'name':name,'age':age}

@app.route("/balance", methods=['GET'])
def balanceget():
    address = request.args.get('address','')
    balance = contract.caller.balanceOf(address)
    return {'address':address,'balance':balance}


@app.route("/owner", methods=['GET'])
def owner():
    owner = contract.caller.owner()
    return {"owner":owner}

@app.route("/totalsupply", methods=['GET'])
def total():
    total = contract.caller.totalSupply()
    return {"totalsupply":total}

@app.route("/contractname",methods=['GET'])
def name():
    name = contract.caller.name()
    return {"contractname":name}

@app.route("/symbol",methods=['GET'])
def symbol():
    symbol = contract.caller.symbol()
    return {'symbol':symbol}

@app.route('/decimals',methods=['GET'])
def decimals():
    decimals = contract.caller.decimals()
    return {'decimals':decimals}
@app.route('/usertoken',methods=['GET'])
def usertoken():
    userId = request.args.get('userId','')
    userId = str(userId)
    usertoken1 = contract.functions.userToken(userId).call()
    return {'userid':userId,'usertoken':usertoken1}

@app.route('/transfer',methods=['GET'])
def erc20_transfer():   
    toaddress = request.args.get('toaddress','')   
    value = request.args.get('value','') 
    tx_hash = contract.functions.transfer(toaddress, int(value)).transact({'from': wallet_address})
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return {'toaadress':toaddress,'value':value}

@app.route('/addtoken',methods=['GET'])
def erc20_addtoken():
    userid = request.args.get('userid','')
    value = request.args.get('value','')
    userId = str(userid)
    tx_hash = contract.functions.AddToken(userId, int(value)).transact({'from': wallet_address})
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return {'userid':userid,'value':value}

@app.route('/subtoken',methods=['GET'])
def erc20_subtoken():
    userid = request.args.get('userid','')
    value = request.args.get('value','')
    userId = str(userid)
    tx_hash = contract.functions.SubToken(userId, int(value)).transact({'from': wallet_address})
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return {'userid':userid,'value':value}

@app.route('/tokenzero',methods=['GET'])
def erc20_tokenzero():
    userid = request.args.get('userid','')
    userId = str(userid)
    tx_hash = contract.functions.TokenZere(userId).transact({'from': wallet_address})
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return {'userid':userid}

@app.route('/transfertouser',methods=['GET'])
def erc20_transfertouser():
    userida = request.args.get('userida','')
    useridb = request.args.get('useridb','')
    value = request.args.get('value','')
    useridA = str(userida)
    useridB = str(useridb)
    Value = int(value)
    tx_hash = contract.functions.TransferToUser(useridA,useridB,Value).transact({'from': wallet_address})
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return {'userida':userida,'useridb':useridb,'value':value}

@app.route('/withdrawtoaddress',methods=['GET'])
def erc20_withdrawtoaddress():
    userid = request.args.get('userid','')
    useraddresss = request.args.get('useraddresss','')
    value = request.args.get('value','')
    userId = str(userid)
    Value = int(value)
    tx_hash = contract.functions.WithdrawToAddress(userId,useraddresss,Value).transact({'from': wallet_address})
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return {'userid':userId,'useraddress':useraddresss,'value':Value}

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=82)