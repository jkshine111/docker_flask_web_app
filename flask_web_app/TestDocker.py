from flask import *

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def create_user():
    # response = 'Hello'
    # return {response}
    return jsonify({"message": 'Hello jayakumar'}), 200

if __name__ == "__main__":
    app.run(port = 5011, host='0.0.0.0', threaded=True,debug=True, use_reloader=False)
    # app.run(port = Port_Values, host='0.0.0.0', threaded=True,debug=True, use_reloader=False)


