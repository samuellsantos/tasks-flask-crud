from flask import Flask, request, jsonify
from models.task import Task

#Como criar aplicação:
#__name__ = "Main"
app  = Flask(__name__)


tasks = []
task_id_control = 1

@app.route("/tasks", methods=["POST"])
def create_task():
    global task_id_control 
    data = request.get_json()
    new_task = Task(id=task_id_control,title=data["title"], description=data.get("description", ""))
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message": "Nova tarefa criada com sucesso!"})

if __name__ == "__main__": #Garantir que só vai rodar quando executarmos ele de forma manual
#Como rodar
    app.run(debug=True) #Modo recomendando apenas para desenvolvimento local.
