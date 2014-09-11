FlaskDataTables
===============

A straight-forward datatables integration for flask

# Installation 

Simply copy datatables.py to your flask project and import it.

# Usage

The module consists of two classes. One is Collection which is responsible for converting your data to JSON string, and DataTables which is responsible for rendering the Datatable HTML and Javascript.

~~~
# app.py
from flask import Flask, Response, render_template
from modules.datatables import Collections, DataTables
app = Flask(__name__)

# This is where we render the table
@app.route("/")
def index():
    dataTables = DataTables(source="/data")
    dataTables.setColumns([{"param":"Parameters"},{"val":"Value"}])
    return render_template('index.html', table=dataTables.render())

# This is where we create the JSON for our response to DataTable's AJAX Request
@app.route("/data")
def data():
    list = [
        {'param': 'foo', 'val': 2},
        {'param': 'bar', 'val': 10}
    ]
    collection = Collections(list)
    return Response(collection.respond(), mimetype="application/json")

if __name__ == "__main__":
    app.run(debug=True)
~~~

## templates/index.html
~~~
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <!-- MAKE SURE YOU CHANGE THE JS AND CSS URLS -->
    <link rel="stylesheet" href="dataTables.min.css">
    <script type="text/javascript" src="jquery.min.js"></script>
    <script type="text/javascript" src="jquery.dataTables.min.js"></script>
</head>
<body>
{{ table|safe }}
</body>
</html>
~~~

##TODO

fix incoming bugs
code documentaion
Features
Ability To Add Action Buttons (THE CRUD BUTTONS)



