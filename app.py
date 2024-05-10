from flask import Flask, render_template, request, redirect, url_for
from collections import OrderedDict

app = Flask(__name__)

# Sample to-do list (replace with database interaction for persistence)
todos = OrderedDict()

@app.route('/', methods=['GET', 'POST'])
def todo_list():
  if request.method == 'POST':
    # Add new todo
    todo = request.form['todo']
    if todo:
      todos[todo] = False  # Mark new todo as incomplete
      return redirect(url_for('todo_list'))  # Redirect to avoid form resubmission
  return render_template('todo_list.html', todos=todos)

@app.route('/completed/<todo>', methods=['GET'])
def complete(todo):
  if todo in todos:
    todos[todo] = True  # Mark todo as completed
  return redirect(url_for('todo_list'))

@app.route('/delete/<todo>', methods=['GET'])
def delete(todo):
  if todo in todos:
    del todos[todo]  # Delete todo
  return redirect(url_for('todo_list'))

if __name__ == '__main__':
  app.run(host="0.0.0.0", port="3005")
