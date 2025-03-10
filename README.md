### pySFT - Simple Python File Transfer

pySFT is a lightweight web-based file management system built with Flask. It allows users to upload, download, preview, and delete files through an intuitive web interface.





## Features

- **File Upload**: Easily upload files through the web interface
- **File Download**: Download any uploaded file with a single click
- **File Management**: Delete files you no longer need
- **Simple Interface**: Clean, responsive design that works on desktop and mobile
- **Error Handling**: Informative error messages and success notifications
- **Security**: Basic security features including filename sanitization


## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)


### Setup

1. Clone the repository:


```shellscript
git clone https://github.com/ayoalaka/pySFT.git
cd pysft
```

2. Install the required dependencies:


```shellscript
pip install requirements
```

3. Run the application:


```shellscript
python server.py
```

4. Open your web browser and navigate to:


```plaintext
http://localhost:8000
```

## Usage

### Uploading Files

1. Click the "Choose File" button in the upload section
2. Select a file from your computer
3. Click the "Upload" button
4. You'll see a success message when the upload is complete


### Downloading Files

1. Navigate to the "Available Files" section
2. Click the "Download" button next to the file you want to download


### Deleting Files

1. Navigate to the "Available Files" section
2. Click the "Delete" button next to the file you want to remove
3. Confirm the deletion when prompted


## Configuration

You can customize the following settings in the `server.py` file:

- `UPLOAD_FOLDER`: The directory where uploaded files are stored (default: "uploads")
- `app.secret_key`: Secret key for session management (change this in production)
- Port number: Change the port in the `app.run()` call (default: 8000)


## Project Structure

```plaintext
pysft/
├── server.py                  # Basic implementation
├── uploads/                   # Directory for uploaded files
├── templates/                 # HTML templates (created automatically)
│   ├── index.html             # Main page template
│   └── preview.html           # File preview template
└── README.md                  # This documentation
```

## Security Considerations

This application implements basic security measures:

- Filename sanitization to prevent path traversal attacks
- File size limits to prevent server overload
- Input validation


However, for production use, consider implementing:

- User authentication
- HTTPS
- More robust input validation
- Rate limiting


## Contributing

Contributions are welcome! Here's how you can contribute:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request


## License

This project is licensed under the GNU General Public License v3.0 - see the LICENSE file for details.

## Acknowledgments

- Flask web framework
- Werkzeug utilities
- Bootstrap (for the improved version)


---

## API Documentation

### Routes

#### `GET /`

- **Description**: Main page that displays the file manager interface
- **Response**: HTML page with file listing and upload form


#### `POST /upload`

- **Description**: Handles file uploads
- **Parameters**:

- `file` (form-data): The file to upload



- **Response**: Redirects to the main page with a success/error message


#### `GET /download/<filename>`

- **Description**: Downloads a specific file
- **Parameters**:

- `filename` (path): Name of the file to download



- **Response**: File download response


#### `POST /delete/<filename>`

- **Description**: Deletes a specific file
- **Parameters**:

- `filename` (path): Name of the file to delete



- **Response**: Redirects to the main page with a success/error message


### Advanced Version Additional Routes

#### `GET /preview/<filename>`

- **Description**: Previews a specific file (images, text, PDF)
- **Parameters**:

- `filename` (path): Name of the file to preview



- **Response**: HTML preview page


#### `GET /search`

- **Description**: Searches for files by name
- **Parameters**:

- `query` (query string): Search term



- **Response**: HTML page with filtered file listing


---

## Troubleshooting

### Common Issues

1. **Empty page when accessing the application**

   Make sure the server is running without errors.
   
   Check console output for any Python exceptions.
   
   Verify that you're using the correct URL ([http://localhost:8000](http://localhost:8000)).



3. **Upload errors**

   Ensure the uploads directory exists and has write permissions.
   
   Check if the file size exceeds the limit.
   
   Verify that the file name doesn't contain invalid characters.



5. **Download issues**

   Confirm that the file exists in the uploads directory.
   
   Check if the file name is correctly URL-encoded.



7. **Unicode/Encoding errors**

   Use the simple version which avoids emoji characters.
   
   Ensure your terminal/console supports UTF-8.



For any other issues, please open an issue on GitHub with detailed information about the problem.

## GNU GPL v3 License Notice

pySFT - Simple Python File Transfer
Copyright ©️ 2025

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see `<https://www.gnu.org/licenses/>`.
