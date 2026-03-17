from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/tasks", methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route("/")
def put_task():
    return render_template("newTask.html")

# Sample Tasks
tasks = {"Run":True,"Read 10 minutes":False,"Drink 1 Gallon of water":True,"10K Steps":True}