from flask import Flask
import numpy as np
from flask import  request, render_template,send_from_directory
from flask import  redirect, url_for
import pickle
import os

  
import werkzeug 
import pandas as pd


from werkzeug.utils import secure_filename



# import logging
# from logging.config import fileConfig
# import flask_monitoringdashboard as dashboard



# logging.basicConfig(filename='demo.log', level=logging.DEBUG)
app = Flask(__name__)
app.config['SECRET_KEY'] = 'e9a9db82a3766bf6671aad9cb092097c'

UPLOAD_FOLDER = '/tmp'
ALLOWED_EXTENSIONS = {'csv'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
model = pickle.load(open('model.pkl', 'rb')) 

# dashboard.bind(app)

@app.route('/')
def Welcome():
    app.logger.info('Processing default request')
    return render_template('layout.html')

@app.route('/home')
def home():
    app.logger.info('Processing default request')
    return render_template('index.html')




@app.route('/uploads', methods=['GET', 'POST'])      
def upload_file():
    if request.method == 'POST':
    
                file = request.files['file'] 
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path) 
    return render_template('index2.html')
   
  


@app.route('/prediction', methods=['POST'])   

def prediction():
  file = request.files['file'] 
       
  filename = secure_filename(file.filename)
  file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
  file.save(file_path) 
  df = pd.read_csv(file_path)
  Event = model.predict(df)
  Event = pd.DataFrame(data=Event, columns=["EventFlag"])
 
  Final_data= pd.concat([df,  Event], axis=1) 
  Final_data.to_csv("/tmp/data2.csv")
  return send_from_directory(directory= app.config['UPLOAD_FOLDER'], filename='data2.csv',as_attachment = True)
           
  #return render_template('uf.html')



       
      
      
@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = prediction

    return render_template('index.html', prediction_text='EventFlag (It is 1 incase of an event){}'.format(output))
    

if __name__ == "__main__":
    app.run(Debug = True)
    
    
    
