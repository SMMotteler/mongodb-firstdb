# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template, redirect
from flask import request
from flask_pymongo import PyMongo
import os
from bson.objectid import ObjectId


# -- Initialization section --
app = Flask(__name__)

# events = [
#         {"event":"First Day of Classes", "date":"2019-08-21"},
#         {"event":"Winter Break", "date":"2019-12-20"},
#         {"event":"Finals Begin", "date":"2019-12-01"}
#     ]

app.config['MONGO_DBNAME'] = os.getenv('DBNAME')
DBNAME = app.config['MONGO_DBNAME']    
app.config['USER'] = os.getenv('DBUSER')
USER = app.config['USER']    
app.config['MONGO_PWD'] = os.getenv('DBPWD')   
PWD = app.config['MONGO_PWD']    
# URI of database   
app.config['MONGO_URI'] = f"mongodb+srv://{USER}:{PWD}@cluster0.seola.mongodb.net/{DBNAME}?retryWrites=true&w=majority"

mongo = PyMongo(app)

# -- Routes section --
# INDEX

@app.route('/')
@app.route('/index')

def index():
    collection = mongo.db.my_First_Collection
    events = collection.find({})
    return render_template('index.html', events = events)


@app.route('/displayform')
def display_form():
    return render_template('form.html')

@app.route('/events/new', methods=['GET', 'POST'])
def new_event():
   if request.method == "GET":
       return render_template('new_event.html')
   else:
       print(request.form)
       event_name = request.form['event_name']
       event_date = request.form['event_date']
       user_name = request.form['user_name']
 
       # get the collection you want to use
       collection = mongo.db.my_First_Collection
 
       # insert the new data
       collection.insert({'event': event_name, 'date': event_date, 'user': user_name})
       
       #redirect sends you to the route in the parenthesis
       return redirect('/')