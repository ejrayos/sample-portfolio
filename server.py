from flask import Flask, render_template, url_for, request, redirect
from data_controller import write_to_file, write_to_csv
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
# print(url_for('static', filename='rice.ico')) #file location


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(f'{page_name}.html')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()  # for retrieving data sent by the form
            write_to_csv(data)
            return render_template('thankyou.html', data=data)
        except:
            return 'did not save to the DB'
    else:
        return 'something went wrong'

# non-dynamic
# @app.route('/works')
# def works():
#     return render_template('works.html')

# @app.route('/<username>/<int:post_id>')  # inserting parameters
# def index_user(username=None, post_id=None):
#     return render_template('index.html', name=username, post_id=post_id)
