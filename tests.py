from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]
@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})
@app.route('/todo/standinstatus', methods=['GET'])
def get_tasks1():
    return jsonify({'standinactiv': '0'})

@app.route('/todo/weather/now', methods=['GET'])
def get_weather_now():
    return 'температура воздуха сейчас +8, кратковременный дождь'
@app.route('/todo/weather/today', methods=['GET'])
def get_weather_today():
    return 'температура воздуха завтра +12, облачно'
if __name__ == '__main__':
    app.run(debug=True)
