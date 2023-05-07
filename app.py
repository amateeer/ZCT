from flask import Flask, request
from pymongo import MongoClient

# Pripojenie k MongoDB Atlas
connection_string = 'mongodb+srv://zctzadanie:zadanie@zadanie.twkwmzm.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(connection_string)

# Výber databázy a kolekcie
db = client['zadanie']
tasks_collection = db['task']

app = Flask(__name__)

# Pridajte úlohu do databázy
def add_task_to_db(task_name, task_desc):
    task = {
        'task_name': task_name,
        'task_desc': task_desc,
    }
    tasks_collection.insert_one(task)

@app.route('/tasks', methods=['POST'])
def add_task():
    task_name = request.json['task_name']
    task_desc = request.json['task_desc']
    add_task_to_db(task_name, task_desc)
    return 'Úloha bola pridaná do databázy.'

if __name__ == '__main__':
    app.run()
