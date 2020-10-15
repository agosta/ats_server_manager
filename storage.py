#!/usr/bin/python3
import redis
import json

path='.'

def openRedis():
  return redis.Redis()

def store(key, value):
  rj = openRedis()
  rj.set(key, json.dumps(value))

def load(key):
  rj = openRedis()
  return json.loads(rj.get(key))

def getkeys():
  rj = openRedis()
  return rj.keys()

def delkey(key):
  rj = openRedis()
  rj.delete(key)

if __name__ == "__main__" :
  store('key1', { 'id' : 'id1', 'value' : 'val1' })
  store('key2', { 'id' : 'id2', 'value' : 'val2' })
  keys=getkeys()
  print(keys)
  for k in keys : 
    print(load(k))
