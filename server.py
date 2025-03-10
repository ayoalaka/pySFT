from flask import Flask, request, send_from_directory, render_template_string, redirect, url_for, flash, get_flashed_messages
import os
import datetime
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'dev_key_for_testing'
UPLOAD_FOLDER = "uploads"

# Ensure upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Simple HTML template directly in the code
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple File Manager</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        h1 { color: #333; }
        .file-list { margin-top: 20px; }
        .file-item { padding: 10px; border-bottom: 1px solid #eee; display: flex; justify-content: space-between; }
        .file-item:hover { background-color: #f9f9f9; }
        .upload-form { margin: 20px 0; padding: 15px; background-color: #f5f5f5; border-radius: 5px; }
        .btn { padding: 8px 16px; background-color: #4CAF50; color: white; border: none; cursor: pointer; }
        .btn:hover { background-color: #45a049; }
        .btn-delete { background-color: #f44336; }
        .btn-delete:hover { background-color: #d32f2f; }
        .message { padding: 10px; margin: 10px 0; border-radius: 5px; }
        .message.success { background-color: #dff0d8; color: #3c763d; }
        .message.error { background-color: #f2dede; color: #a94442; }
    </style>
</head>
<body>
    <h1>Simple File Manager</h1>
    
    {% for category, message in get_flashed_messages(with_categories=true) %}
        <div class="message {{ category }}">{{ message }}</div>
    {% endfor %}
    
    <div class="upload-form">
        <h2>Upload a File</h2>
        <form action="/upload" method="post" enctype="multipart/form-data">
            <input type="file" name="file" required>
            <button type="submit" class="btn">Upload</button>
        </form>
    </div>
    
    <div class="file-list">
        <h2>Available Files</h2>
        {% if files %}
            {% for file in files %}
                <div class="file-item">
                    <span>{{ file.name }}</span>
                    <div>
                        <a href="/download/{{ file.name }}" class="btn">Download</a>
                        <form action="/delete/{{ file.name }}" method="post" style="display: inline;">
                            <button type="submit" class="btn btn-delete" onclick="return confirm('Are you sure?')">Delete</button>
                        </form>
                    </div>
                </div>
            {% endfor %}
        {% else %}
            <p>No files uploaded yet.</p>
        {% endif %}
    </div>
</body>
</html>
"""

def get_file_info(filename):
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    stats = os.stat(filepath)
    
    return {
        "name": filename,
        "size": stats.st_size,
        "modified": datetime.datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
    }

@app.route("/")
def index():
    try:
        # Get list of files
        files = []
        for filename in os.listdir(UPLOAD_FOLDER):
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            if os.path.isfile(file_path):
                files.append(get_file_info(filename))
        
        # Render template
        return render_template_string(HTML_TEMPLATE, files=files)
    except Exception as e:
        # Print error for debugging
        print(f"Error in index route: {str(e)}")
        return f"An error occurred: {str(e)}"

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        flash("No file part", "error")
        return redirect(url_for('index'))
    
    file = request.files["file"]
    
    if file.filename == '':
        flash("No file selected", "error")
        return redirect(url_for('index'))
    
    try:
        # Secure the filename
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        
        # Save the file
        file.save(file_path)
        
        flash(f"File {filename} uploaded successfully!", "success")
    except Exception as e:
        flash(f"Error uploading file: {str(e)}", "error")
    
    return redirect(url_for('index'))

@app.route("/download/<filename>")
def download_file(filename):
    try:
        return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)
    except Exception as e:
        flash(f"Error downloading file: {str(e)}", "error")
        return redirect(url_for('index'))

@app.route("/delete/<filename>", methods=["POST"])
def delete_file(filename):
    try:
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        
        if os.path.exists(file_path):
            os.remove(file_path)
            flash(f"File {filename} deleted successfully!", "success")
        else:
            flash(f"File {filename} not found", "error")
    except Exception as e:
        flash(f"Error deleting file: {str(e)}", "error")
    
    return redirect(url_for('index'))

if __name__ == "__main__":
    print(f"Starting server. Upload directory: {os.path.abspath(UPLOAD_FOLDER)}")
    app.run(host="0.0.0.0", port=8000, debug=True)