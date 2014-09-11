from flask import Flask, Response, render_template
from modules.datatables import Collections, DataTables
app = Flask(__name__)

@app.route("/")
def index():
    dataTables = DataTables(source="/data")
    dataTables.setColumns([{"param":"Parameters"},{"val":"Value"}])
    return render_template('index.html', table=dataTables.render())

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
