import os
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__, static_folder="static", template_folder="templates")

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
    return jsonify({"success": True, "files": files})

@app.route('/update/<old_name>', methods=['POST'])
def update(old_name):
    new_name = request.form.get('new_name')
    if old_name in files and new_name and new_name not in files:
        files[files.index(old_name)] = new_name
        return jsonify({"success": True, "files": files})
    return jsonify({"success": False, "error": "Invalid update"}), 400

@app.route('/delete/<filename>', methods=['POST'])
def delete(filename):
    if filename in files:
        files.remove(filename)
        return jsonify({"success": True, "files": files})
    return jsonify({"success": False, "error": "File not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)