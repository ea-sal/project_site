from flask import Flask, render_template, request


my_flask_app = Flask(__name__)


@my_flask_app.route('/', methods=['POST', 'GET'])
def index():
    default_name = '0'
    user_name = request.form.get('field_one', default_name)
    print(user_name)
    print(request.data)
#    for k, v in request.form.items():
#        print(k, '|', v)
    return render_template('index.html')


@my_flask_app.route('/search/', methods=['POST', 'GET'])
def search():
#    user_name = request.form['inputForm']
#    region = request.form['serv']
#    print(user_name)
    return render_template('search.html')


if __name__ == "__main__":
    my_flask_app.run(debug=True)
