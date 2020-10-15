#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_cors import CORS
from uuid import uuid1 as uuid
from storage import store, load, getkeys, delkey
import json

app = Flask(__name__)
CORS(app)

threshold = 3

def search(data, value):
  from random import randint
  return randint(1,10)

@app.route('/search')
def get():
  data = request.json
  keys=getkeys()
  results = []
  for k in keys : 
    value = load(k)
    match = search(data, value)
    if match > threshold : 
      results.append((value, match))
  result = jsonify({'data': [ i[0] for i in sorted(results, key=lambda tup : tup[-1]) ]})
  print(result.data)
  return result

@app.route('/list')
def getall():
  data = request.json
  keys=getkeys()
  results = { k : load(k) for k in keys }
  for k in results : 
    results[k]['key']=k
  results = { 'data' : [ results[k] for k in results ] }
  return jsonify(results)


@app.route('/add', methods=['GET', 'POST'])
def add():
  key = str(uuid())
  data=json.loads(request.get_data())
  print(request.get_data())
  store(key, data)
  return '', 200

@app.route('/delete')
def remove():
  app.logger.info(request.form)
  key = request.args.get('key')
  print(key)
  delkey(key)
  return '', 200
