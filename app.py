from flask import Flask, request
from google.cloud import firestore
from google.cloud import firestore
from google.oauth2 import service_account

# inicializujte klienta Firestore s použitím vášho vlastného projektu a kľúča pre službu
cred = service_account.Credentials.from_service_account_file('zct1-385912-c6a1e78d96c4.json')
db = firestore.Client(credentials=cred, project='zct1-385912')

app = Flask(__name__)

db = firestore.Client()

# pridajte zdroj do db
# pridajte úlohu do databázy
def add_task_to_db(task_name, task_desc):
    tasks_ref = db.collection('tasks')
    tasks_ref.document().set({
        'task_name': task_name,
        'task_desc': task_desc,
    })


@app.route('/tasks', methods=['POST'])
def add_task():
    task_name = request.json['task_name']
    task_desc = request.json['task_desc']
    add_task_to_db(task_name, task_desc)
    return 'Úloha bola pridaná do databázy.'


if __name__ == '__main__':
    app.run()
