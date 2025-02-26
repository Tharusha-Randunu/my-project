from flask import Flask, render_template, request, redirect, url_for, abort 

app = Flask(__name__)

tasks = [] 


@app.route('/') 
def index(): 
    return render_template('index.html', tasks=tasks) 

@app.route('/add', methods=['POST']) 
def add(): 
    name = request.form.get('name')  
    description = request.form.get('description')  
    if name and description:  
        tasks.append({"name": name, "description": description})
    return redirect(url_for('index'))

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    if id >= 0 and id < len(tasks):
        tasks.pop(id)  
    return redirect(url_for('index'))

@app.route('/delete_all', methods=['POST'])
def delete_all():
    global tasks 
    tasks = []  
    return redirect(url_for('index'))


@app.route('/task/<int:id>') 
def show(id): 
    if id >= 0 and id < len(tasks): 
       task = tasks[id]  
       return render_template('task.html', name=task["name"], description=task["description"])  
 
    else: 
        abort(404, "This task doesn't exists") 

if __name__ == '__main__':
    app.run(debug=True)
