from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulated storage (in-memory list)
files = []

@app.route('/')
def index():
    return render_template('index.html', files=files)

@app.route('/upload', methods=['POST'])
def upload():
    filename = request.form['filename']
    if filename and filename not in files:
        files.append(filename)
    return redirect(url_for('index'))

@app.route('/update/<old_name>', methods=['POST'])
def update(old_name):
    new_name = request.form['new_name']
    if old_name in files and new_name not in files:
        files[files.index(old_name)] = new_name
    return redirect(url_for('index'))

@app.route('/delete/<filename>')
def delete(filename):
    if filename in files:
        files.remove(filename)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
