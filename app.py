from flask import Flask, render_template, request, redirect

app = Flask(__name__)

estudiantes = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')
     
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = request.form['edad']
        carrera = request.form['carrera']
        estudiantes.append({'nombre': nombre, 'edad': edad, 'carrera': carrera})
        return redirect('/admin')
    return render_template('admin.html', estudiantes=estudiantes)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
