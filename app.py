from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Loads templates/index.html

if __name__ == '__main__':
    app.run(debug=True)
    
# from flask import Flask, render_template

# app = Flask(
#     __name__,
#     template_folder='frontend',       # Your HTML files
#     static_folder='frontend',         # Your CSS/JS/images
#     static_url_path='/static'         # URL path to access static files
# )

# @app.route('/')
# def index():
#     return render_template('index.html')  # Make sure frontend/index.html exists

# if __name__ == '__main__':
#     app.run(debug=True)
