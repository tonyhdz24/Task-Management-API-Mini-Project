from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route("/tasks", methods=['GET','POST'])
def get_tasks():
    if request.method == 'POST':
        return 'Adding a new task to the todo list'
    else:
        return jsonify(tasks)

@app.route("/")
def put_task():
    return render_template("newTask.html")

# Sample Tasks
tasks = {"Run":True,"Read 10 minutes":False,"Drink 1 Gallon of water":True,"10K Steps":True}