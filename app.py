from flask import Flask, render_template, request, redirect, url_for
from collections import OrderedDict

# Sample to-do list (consider database integration for persistence)
todos = OrderedDict()

app = Flask(__name__)

# Enhanced error handling for user input (optional)
def validate_todo(todo):
    if not todo or len(todo.strip()) == 0:
        return False  # Handle empty or whitespace-only input
    return True

@app.route('/', methods=['GET', 'POST'])
def todo_list():
    if request.method == 'POST':
        todo = request.form['todo']
        if validate_todo(todo):  # Optional validation
            todos[todo] = False  # Mark new todo as incomplete
            return redirect(url_for('todo_list'))  # Redirect to avoid resubmission
        else:
            # Display an error message (optional)
            error_message = "Please enter a valid todo item."
            return render_template('todo_list.html', todos=todos, error_message=error_message)
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
    app.run(debug=True)  # Set debug=False for production deployments


if __name__ == '__main__':
  app.run(host="0.0.0.0", port="3005")
