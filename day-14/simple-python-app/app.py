from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def hello():
    # Simple HTML with CSS for an attractive look
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Flask App</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f0f4f8;
                    color: #333;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }
                .container {
                    text-align: center;
                    background-color: #fff;
                    padding: 40px;
                    border-radius: 8px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                }
                h1 {
                    color: #4CAF50;
                    font-size: 2.5em;
                }
                p {
                    font-size: 1.2em;
                    color: #555;
                }
                .footer {
                    margin-top: 20px;
                    font-size: 0.9em;
                    color: #888;
                }
                .footer a {
                    color: #4CAF50;
                    text-decoration: none;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Hello, World!</h1>
                <p>This is a live update of the Flask app. It's now more visually attractive!</p>
                <div class="footer">
                    <p>Created by MOHD SHUAIB</p>
                    <p>Thank you for visiting my website ❤️ </p>
                    <p>Visit <a href="https://www.palletsprojects.com/p/flask/" target="_blank">Flask Documentation</a> for more info.</p>
                </div>
            </div>
        </body>
        </html>
    ''')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Listen on all IPs
