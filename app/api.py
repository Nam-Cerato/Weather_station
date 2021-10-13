from flask import Blueprint, render_template, request, flash, jsonify, session, redirect, url_for
import json
from app.models import *

api = Blueprint('api', __name__)

@api.route('/getAllUser' , methods=['GET'])
def getAllUser():
    # message = json(get_allUser())
    resp = get_allUser()
    return resp

@api.route('/getPestFarm1', methods=['GET', 'POST'])
def getPestFarm1():
    couting_pest = get_pest_in_farm("Farm_1")
    return couting_pest
