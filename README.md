# enodo python

## Installation
To install packages
- Create virtual env and run
``` 
pip install Flask, jsonify, request, flask-cors, sqlalchemy
```
If the database is not set up run:
```
python populate.py
```

Start the app:
```
python app.py
```

## Assumptions

- I assumed using sqlite and not using a full postgresql db was ok. I figured the important part was using the orm.
- 

## Questions
- What changes when using actual postgresql as db
- How would putting code into production state change it?

## Possible Future States
- Would want security around the data calls
- Better success or error messages
