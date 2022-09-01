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

@app.route("/owner", methods=['GET'])
def owner():
    owner = contract.caller.owner()
    return {"owner":owner}    

@app.route("/videoinfo",methods=['GET'])
def videoinfo():
    id = request.args.get('id','')
    id = str(id)
    info = contract.functions.Video_info(id).call()
    return {'userId':info[0],'createtime':info[1],'vlogId':info[2]}

@app.route('/videotort',methods=['GET'])
def videotort():
    id = request.args.get('id','')
    id = str(id)
    info = contract.functions.Video_tort(id).call()
    return {'userId':info[0],'createtime':info[1],'vlogId':info[2]}

@app.route('/illeglevideo',methods=['GET'])
def illeglevideo():
    id = request.args.get('id','')
    id = str(id)
    info = contract.functions.Illegle_video(id).call()
    return {'userId':info[0],'kind':info[1],'createtime':info[2],'vlogId':info[3]}

@app.route('/balance',methods=['GET'])
def balance():
    createtime = request.args.get('createtime','')
    createtime = int(createtime)
    balance = contract.caller.balanceOf("0xe87Ed10b8422C67bC9Cf134925ECAf6f125EEb0e",createtime)
    return {'createtime':createtime,'balance':balance}

@app.route('/addvideo',methods=['GET'])
def addvideo():
    userid = request.args.get('userid','')
    vlogid = request.args.get('vlogid','')
    userId=str(userid)
    vlogId=str(vlogid)
    tx_hash = contract.functions.AddVideo(userId, vlogId).transact({'from': wallet_address})
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return {'userid':userId,'vlogid':vlogId}

@app.route('/addtort',methods=['GET'])
def addtort():
    userid = request.args.get('userid','')
    vlogid = request.args.get('vlogid','')
    userId=str(userid)
    vlogId=str(vlogid)
    tx_hash = contract.functions.AddTort(userId, vlogId).transact({'from': wallet_address})
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return {'userid':userId,'vlogid':vlogId}

@app.route('/addillegle',methods=['GET'])
def AddIllegle():
    userid = request.args.get('userid','')
    vlogid = request.args.get('vlogid','')
    kind = request.args.get('kind','')
    userId=str(userid)
    vlogId=str(vlogid)
    Kind = str(kind)
    tx_hash = contract.functions.AddIllegle(userId, vlogId,Kind).transact({'from': wallet_address})
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return {'userid':userId,'vlogid':vlogId,'kind':Kind}


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=82)