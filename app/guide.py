from flask import Blueprint, render_template, request, flash, jsonify, session, redirect, url_for
from app.models import *

guide = Blueprint('guide', __name__)

@guide.route('/chlorophyll_meter_SPAD502PLUS' , methods=['GET'])
def chlorophyll_meter_SPAD502PLUS():
      return render_template('guide/chlorophyll_meter_SPAD502PLUS.html')

@guide.route('/chlorophyll_meter_Spectrum' , methods=['GET'])
def chlorophyll_meter_Spectrum():
      return render_template('guide/chlorophyll_meter_Spectrum.html')

@guide.route('/Portable_Laser_Area_Meter_CI_202' , methods=['GET'])
def Portable_Laser_Area_Meter_CI_202():
      return render_template('guide/Portable_Laser_Area_Meter_CI_202.html')

@guide.route('/Portable_Leaf_Area_Meter_YMJ_B' , methods=['GET'])
def Portable_Leaf_Area_Meter_YMJ_B():
      return render_template('guide/Portable_Leaf_Area_Meter_YMJ_B.html')

@guide.route('/Gamma_Sciencetific_Spectrometter_PG200N' , methods=['GET'])
def Gamma_Sciencetific_Spectrometter_PG200N():
      return render_template('guide/Gamma_Sciencetific_Spectrometter_PG200N.html')


@guide.route('/Light_Meter_Extech_SLD400' , methods=['GET'])
def Light_Meter_Extech_SLD400():
      return render_template('guide/Light_Meter_Extech_SLD400.html')


@guide.route('/SWXB-4G-EU_BR-V2' , methods=['GET'])
def SWXB_4G_EU_BR_V2():
      return render_template('guide/SWXB-4G-EU_BR-V2.html')

@guide.route('/SWXB-W' , methods=['GET'])
def SWXB_W():
      return render_template('guide/SWXB-W.html')

@guide.route('/SEPB-W' , methods=['GET'])
def SEPB_W():
      return render_template('guide/SEPB-W.html')

@guide.route('/SAXB-W' , methods=['GET'])
def SAXB_W():
      return render_template('guide/SAXB-W.html')

@guide.route('/SAXB-802' , methods=['GET'])
def SEPB_802():
      return render_template('guide/SAXB-802.html')

@guide.route('/M4G-802-EU' , methods=['GET'])
def M4G_802_EU():
      return render_template('guide/M4G-802-EU.html')

@guide.route('/ECLIPSE_E200' , methods=['GET'])
def ECLIPSE_E200():
      return render_template('guide/ECLIPSE_E200.html')

@guide.route('/SMZ745' , methods=['GET'])
def SMZ745():
      return render_template('guide/SMZ745.html')

@guide.route('/NIS-ELEMENT-D' , methods=['GET'])
def NIS_ELEMENT_D():
      return render_template('guide/NIS-ELEMENT-D.html')

@guide.route('/BUONGSINHTRUONG' , methods=['GET'])
def BUONGSINHTRUONG():
      return render_template('guide/BUONGSINHTRUONG.html')

@guide.route('/labostar-pro-de' , methods=['GET'])
def labostar_pro_de():
      return render_template('guide/labostar-pro-de.html')

@guide.route('/Camera-camtay' , methods=['GET'])
def Camera_camtay():
      return render_template('guide/Camera-camtay.html')

@guide.route('/Mastercycler-nexus' , methods=['GET'])
def Mastercycler_nexus():
      return render_template('guide/Mastercycler-nexus.html')

@guide.route('/huongdansudung' , methods=['GET'])
def huongdan():
      return render_template('guide/guide.html')
