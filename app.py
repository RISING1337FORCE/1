import os
from flask import Flask, send_from_directory

app = Flask(__name__)

# Set the path to the folder that contains your .exe file
EXE_FOLDER = os.path.join(os.getcwd(), 'NEWNEW')  # Correct folder path for your .exe file
app.config['EXE_FOLDER'] = EXE_FOLDER

@app.route('/')
def index():
    # HTML content with a professional design and better CSS
    return '''
        <html>
            <head>
                <style>
                    * {
                        margin: 0;
                        padding: 0;
                        box-sizing: border-box;
                    }
                    body {
                        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                        background-color: #f7f9fc;
                        color: #333;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        min-height: 100vh;
                        margin: 0;
                    }
                    .container {
                        background-color: #fff;
                        border-radius: 10px;
                        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                        padding: 30px;
                        width: 80%;
                        max-width: 500px;
                        text-align: center;
                    }
                    h1 {
                        color: #2c3e50;
                        font-size: 2.5em;
                        margin-bottom: 20px;
                        font-weight: 600;
                    }
                    p {
                        font-size: 1.2em;
                        color: #7f8c8d;
                        margin-bottom: 20px;
                    }
                    .button-container {
                        display: flex;
                        justify-content: center;
                        align-items: center;
                    }
                    button {
                        padding: 15px 30px;
                        font-size: 1.2em;
                        color: #fff;
                        background-color: #3498db;
                        border: none;
                        border-radius: 5px;
                        cursor: pointer;
                        transition: all 0.3s ease-in-out;
                        width: 200px;
                    }
                    button:hover {
                        background-color: #2980b9;
                        transform: scale(1.05);
                    }
                    button:focus {
                        outline: none;
                    }
                    .footer {
                        margin-top: 20px;
                        font-size: 0.9em;
                        color: #bdc3c7;
                    }
                    .footer a {
                        color: #3498db;
                        text-decoration: none;
                    }
                    .footer a:hover {
                        text-decoration: underline;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>Download My Python App</h1>
                    <p>Click the button below to download the app.</p>
                    <div class="button-container">
                        <a href="/download/steganography_custom.exe">
                            <button>Download Now</button>
                        </a>
                    </div>
                    <div class="footer">
                        <p>© 2025 YourAppName | <a href="https://yourwebsite.com">Visit our website</a></p>
                    </div>
                </div>
            </body>
        </html>
    '''

@app.route('/download/<filename>')
def download_file(filename):
    # Debugging: Print the requested filename to check if it's being passed correctly
    print(f"Requested file: {filename}")

    # Check if the file exists in the 'NEWNEW' folder
    file_path = os.path.join(app.config['EXE_FOLDER'], filename)
    if not os.path.exists(file_path):
        # Log an error if the file does not exist
        print(f"Error: The file '{filename}' does not exist in the 'NEWNEW' folder.")
        return "File not found", 404

    # If file exists, serve it
    return send_from_directory(app.config['EXE_FOLDER'], filename)

if __name__ == '__main__':
    # Run Flask with debug=False for better stability during testing
    app.run(debug=True)
