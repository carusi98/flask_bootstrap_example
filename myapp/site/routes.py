from flask import Blueprint, render_template
import time

#from profession_calculations import GPIO,


site = Blueprint('site',
    __name__,
    static_folder = "static",
    template_folder = "templates")

@site.route('/')
def index():
    #pull API
    #page_content = GPIO()
    
    page_content = {'Temp': '87', 'LED_on':'', 'LED_off':'active', 'NIGHT_on':'active', 'NIGHT_off':'',
     'HEAT_on':'', 'HEAT_off':'active'}
    return render_template('index.html',page_content=page_content)



