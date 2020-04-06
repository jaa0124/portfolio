from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name): # con esto nos ahorramos tener que crear los enlaces uno a uno
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Algo ha salido mal'

def write_to_file(data):
    with open('database.txt', mode='a') as database_txt:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        txt_file = database_txt.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database_csv:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        # col_names = [email,subject,message]

        csv_file = csv.writer(database_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_file.writerow([email, subject, message])


# @app.route('/index.html')
# def my_home_2():
#     return render_template('index.html')

# @app.route('/about.html') #añadimos un nuevo enlace
# def about():
#     return render_template('about.html')
#
# @app.route('/works.html') #añadimos un nuevo enlace
# def works():
#     return render_template('works.html')
#
# @app.route('/work.html') #añadimos un nuevo enlace
# def work():
#     return render_template('work.html')
#
# @app.route('/contact.html') #añadimos un nuevo enlace
# def contact():
#     return render_template('contact.html')
