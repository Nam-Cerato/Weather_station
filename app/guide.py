from flask import Blueprint, render_template, request, flash, jsonify, session, redirect, url_for
from app.models import *

guide = Blueprint('guide', __name__)

@guide.route('/chlorophyll_meter_SPAD502PLUS' , methods=['GET'])
def chlorophyll_meter_SPAD502PLUS():
      return render_template('guide/chlorophyll_meter_SPAD502PLUS.html')

@guide.route('/chlorophyll_meter_Spectrum' , methods=['GET'])
def chlorophyll_meter_Spectrum():
      return render_template('guide/chlorophyll_meter_Spectrum.html')

@guide.route('/huongdansudung' , methods=['GET'])
def huongdan():
      return render_template('guide/guide.html')
