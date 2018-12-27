from flask import Flask, render_template, request
import riot_api
import numpy as np
import pickle


my_flask_app = Flask(__name__)


@my_flask_app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@my_flask_app.route('/search/', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        user_name = request.form["user_name"]
        server = request.form["server"]
    print('I work')
    user = request.args.get('user_name', default=None, type=str)
    serv = request.args.get('server', default='*', type=str)
    print(user, serv)
    uid = riot_api.get_acc_by_name(serv, user)
    matchid = riot_api.get_match_by_acc(serv, uid)
    match = riot_api.match_data_by_id(serv, matchid)
    pred_data = riot_api.match_info(match, uid)

    model = pickle.load(open("model.pkl", "rb"))
    result = pred_data[1]

    predictors = pred_data[0]
    predictors = np.array(predictors)
    predictors = predictors.reshape(1, -1)
    prediction = model.predict(predictors)
    prediction = prediction[0]
    prediction = np.asscalar(prediction)

    res = riot_api.prediction_result(prediction, result)

    print(res)
#    res = test.prediction_result(1, 1)
    return render_template('search.html', value=res)


if __name__ == "__main__":
    my_flask_app.run(debug=True)
