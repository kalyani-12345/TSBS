from flask import Flask, send_from_directory

app = Flask(__name__)

#@app.route('/')
#def home():
   # return send_from_directory('.', 'index.html')  # Serve homepage

@app.route('/menu')
def menu():
    return send_from_directory('.', 'mm.html')  # Serve menu page

@app.route('/<page>')
def serve_html(page):
    return send_from_directory('Frontend', f'{page}.html')


# Serve individual CSS files manually
@app.route('/cartcss.css')
def serve_cartcss():
    return send_from_directory('Frontend', 'cartcss.css')

@app.route('/css.css')
def serve_css():
    return send_from_directory('Frontend', 'css.css')

@app.route('/digibill.css')
def serve_digibill():
    return send_from_directory('Frontend', 'digibill.css')


# Serve individual CSS files manually
@app.route('/indexstyle.css')
def serve_indexstyle():
    return send_from_directory('Frontend', 'indexstyle.css')

@app.route('/menustyles.css')
def serve_menustyles():
    return send_from_directory('Frontend', 'menustyles.css')

@app.route('/odconform.css')
def serve_odconform():
    return send_from_directory('Frontend', 'odconform.css')


@app.route('/Oscss.css')
def serve_Oscss():
    return send_from_directory('Frontend', 'Oscss.css')


# Serve images from the 'image' folder
@app.route('/image/<filename>')
def serve_image(filename):
    return send_from_directory('image', filename)

# Serve images from the 'coffee' folder
@app.route('/coffee/<filename>')
def serve_coffee(filename):
    return send_from_directory('coffee', filename)

# Serve images from the 'stater' folder
@app.route('/stater/<filename>')
def serve_stater(filename):
    return send_from_directory('stater', filename)

# Serve images from the 'Pizza' folder
@app.route('/Pizza/<filename>')
def serve_pizza(filename):
    return send_from_directory('Pizza', filename)

# Serve images from the 'B' (Burger) folder
@app.route('/B/<filename>')
def serve_burger(filename):
    return send_from_directory('B', filename)

# Serve images from the 'd' (Desserts) folder
@app.route('/d/<filename>')
def serve_desserts(filename):
    return send_from_directory('d', filename)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
