from pymongo import MongoClient
from flask import Blueprint, render_template, request, flash, jsonify, session, redirect, url_for
import json
from bson.json_util import dumps, loads
URI = "mongodb://127.0.0.1:27017"
try:
    client = MongoClient(URI)
    Database =  client['Weather_station']
    print("connected to db")
except:
    print("connecting to db fail")

class JsonEncoder():
    def encode( o):
        if '_id' in o:
            o['_id'] = str(o['_id'])
        return o

def get_allUser():
    user_col = Database['user']
    allUser = user_col.find_one()
    allUser = JsonEncoder.encode(allUser)
    allUser = json.dumps(allUser, indent = 4)
    return allUser

def get_userByUserName(username):
    user_col = Database['user']
    user = user_col.find({ 'username' : username})
    return list(user)

def insert_user(username, password):
    user_col = Database["user"]
    user_col.insert(
        {
            "username": username,
            "password": password
        }
    )

def find_one():
    user_col = Database['user']
    user = user_col.find({"$query": {}, "$orderby": {"$natural" : -1}}).limit(1)
    print(type(user))
    return list(user)

def get_pest_in_farm(farm_name):
    farm_col = Database[farm_name]
    # counting_pest = farm_col.find({"$query": {}, "$orderby": {"$natural" : -1}}).limit(1)
    get_pest = farm_col.find_one()
    # get_pest = list(counting_pest)
    # get_pest = dumps(get_pest, indent= 2)
    # get_pest = get_pest['data']['pest']
    get_pest = JsonEncoder.encode(get_pest)
    get_pest = json.dumps(get_pest, indent = 5)
    return get_pest

def get_data_with_hour():
    farm_col = Database['Farm_1']
    data =  farm_col.find(
        {"data.update":
            {"$gte" : "2021-10-13T16:00:00.000+00:00"
           }
        }
    )
    # data = JsonEncoder.encode(data)
    # data = json.dumps(data, indent = 5)
    return data

for x in get_data_with_hour():
  print(x)
# get_data_with_hour()