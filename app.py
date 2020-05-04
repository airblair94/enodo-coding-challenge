from flask import Flask, jsonify, request
from flask_cors import CORS
from sqlalchemy import create_engine, and_
from sqlalchemy.types import (Integer, VARCHAR, String)
from sqlalchemy.orm import sessionmaker
from database_setup import Property, Base
import json
import csv
from datetime import datetime

#configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

#Connect to Database and create database session
engine = create_engine('sqlite:///enodo-collection.db', connect_args={'check_same_thread': False})
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

def get_distinct(colName):
    distinct_vals = []
    for value in session.query(getattr(Property, colName)).distinct():
        distinct_vals.append(value[0])
    return distinct_vals

# route returns all properties using orm
@app.route('/properties', methods=['GET', 'POST'])
def get_properties():
    # If post we add each filter and then query
    if request.method == 'POST':
        post_data = request.get_json()
        filters = []
        for key, value in post_data.items():
            if value['type'] == 'VARCHAR(250)' or value['type'] == 'DATE':
                filters.append(Property.__table__.c[value['name']] == value['value'])
            else:
                if (value['min']):
                    filters.append(Property.__table__.c[value['name']] > value['min'])
                if (value['max']):
                    filters.append(Property.__table__.c[value['name']] < value['max'])
        query = Property.__table__.select().where(and_(*filters))
        response = session.execute(query).fetchall()
        return json.dumps( [dict(ix) for ix in response], default = str)
    else:
        properties = session.query(Property).all()
        return json.dumps(Property.serialize_list(properties), default = str)

# optional route to get data without using database
# less useful in the long run as the database allows us 
# column data and easy filtering information
@app.route('/properties-no-db', methods=['GET'])
def get_properties_no_db():
    data = []
    with open('./Enodo_Skills_Assessment_Data_File.csv') as csvFile:
        reader = csv.DictReader(csvFile)
        for rows in reader:
            next
            data.append(rows)
    
    return json.dumps(data, indent=4)

# Filters goes through all column defs and if type is string or date
# We return each column with its name a string representation of type
# and if it is not numerical we return all distinct values in column
@app.route('/filters', methods=['GET'])
def get_filters():
    columns = []
    table = Property.__table__
    for column in table.columns:
        columnDef = {}
        columnDef['name'] = column.name
        columnDef['type'] = str(column.type)
        if str(column.type) == 'VARCHAR(250)' or str(column.type) == 'DATE':
            columnDef['optionsList'] = get_distinct(str(column.name))
        columns.append(columnDef)
    return json.dumps(columns, default = str)

if __name__ == '__main__':
    app.run()