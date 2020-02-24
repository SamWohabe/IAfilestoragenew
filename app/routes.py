import os
from app import app
from flask import render_template, request, redirect

from flask_pymongo import PyMongo

from bson.objectid import ObjectId

# name of database
app.config['MONGO_DBNAME'] = 'database-name'

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://admin:hEzsvuNPe20opxCn@cluster0-js43a.mongodb.net/test?retryWrites=true&w=majority'

mongo = PyMongo(app)

# # -------------------------------------------------------------------------------------------------------------------

@app.route('/')
@app.route('/index')

def index():
    #connect to the Mongo DB
    collection = mongo.db.events
    files = list(collection.find({}))
    print(files)
    return render_template('index.html', files=files)


# ---------------------------------------------------------------------------------------------------------------------

@app.route('/results', methods = ["get", "post"])
def results():

    user_info = dict(request.form)
    print(user_info)


    clientname = user_info["clientname"]
    print("the client name is ", clientname)
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

    filename = user_info["filename"]
    print("the file name is ", filename)

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
    filelocation = user_info["filelocation"]
    print("the file location is ", filelocation)
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
    filelocation = user_info["filelocation"]
    print("the file location is ", filelocation)
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
    activity = user_info["activity"]
    print("the clients status is ", activity)
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
    creationdate = user_info["creationdate"]
    print("the file was created on ", creationdate)
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
    lawyername = user_info["lawyername"]
    print("the lawyer working on the file is ", lawyername)
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––



    collection = mongo.db.events

    collection.insert({"clientname": clientname, "filename": filename, "filelocation": filelocation, "activity": activity, "creationdate": creationdate, "lawyername": lawyername})

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

    return redirect('/index')


    collection = mongo.db.events


    return redirect('/index')

# ---------------------------------------------------------------------------------------------------------------------

@app.route('/delete')
def delete():
    collection = mongo.db.events

    collection.delete_many({})

    return redirect('/index')
# {{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}
#                                           ^^^^^^^MVP^^^^^^^
# {{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}


@app.route('/filterclientname', methods=['get', 'post'])
def filterclientname():
    collection = mongo.db.events
    files = list(collection.find({}))


    return render_template('filterclientname.html', files=files)

# ---------------------------------------------------------------------------------------------------------------------

@app.route('/clientnamedisplay', methods=['get', 'post'])
def clientnamedisplay():
    collection = mongo.db.events

# creates a variable known as user_info that is the answers to a form in my other route
    user_info=dict(request.form)



    return render_template('filterclientnamedisplay.html', files=files)

# ---------------------------------------------------------------------------------------------------------------------
@app.route('/filterfilename', methods=['get', 'post'])
def filterfilename():
    collection = mongo.db.events
    files = list(collection.find({}))


    return render_template('filterfilename.html', files=files)
# ---------------------------------------------------------------------------------------------------------------------

@app.route('/filenamedisplay', methods=['get', 'post'])
def filenamedisplay():
    collection = mongo.db.events

    user_info=dict(request.form)

    user_input=user_info["filename"]
    files=list(collection.find({"filename": user_input}))



    return render_template('filterfilenamedisplay.html', files=files)

# ---------------------------------------------------------------------------------------------------------------------
@app.route('/filterdate', methods=['get', 'post'])
def filterdate():
    collection = mongo.db.events
    files = list(collection.find({}))


    return render_template('creationdate.html', files=files)

# ---------------------------------------------------------------------------------------------------------------------

@app.route('/creationdatedisplay', methods=['get', 'post'])
def creationdatedisplay():
    collection = mongo.db.events

# creates a variable known as user_info that is the answers to a form in my other route
    user_info=dict(request.form)



    return render_template('creationdatedisplay.html', files=files)

# ---------------------------------------------------------------------------------------------------------------------

@app.route('/deleteindiv', methods=['get', 'post'])
def deleteindiv():
    collection = mongo.db.events

# creates a variable known as user_info that is the answers to a form in my other route
    user_info=dict(request.form)

    result = mongo.db.events.delete_one({'_id': ObjectId(user_info['_id'])})

    return redirect('/index')

# ---------------------------------------------------------------------------------------------------------------------

@app.route('/deleteform', methods=['get', 'post'])
def deleteform():

    collection = mongo.db.events
    files = list(collection.find({}))


    return render_template('index2.html', files=files)
