from flask import Flask, render_template,url_for,request,redirect
# Importing csv  (excel sheet)
import csv

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


# To display pages dynamicaly 
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


# To write the data collected to a file(persist the data of the user)
def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

# Writing to data from the webapp to  csv file using the csv module
def write_to_csv(data):
    with open('database.csv', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database, delimeter=',', newline='',quotechar='|', quoting= csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

# To collect Data eg:sub_form 
@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # print(data)
            write_to_file(data)
            # redirecting to another page after completion
            return redirect('thankyou_contact.html')
        except:
            return 'did not save to database'
    else:
        return 'Oops something wewnt wrong. Try again later!'

