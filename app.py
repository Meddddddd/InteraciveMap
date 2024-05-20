from flask import Flask, render_template, jsonify
from flask_leaflet import Leaflet
import firebasesdkadmin

app = Flask(__name__)

# Створення екземпляру Leaflet
leaflet = Leaflet()


app.config['STATIC_FOLDER'] = 'static'
# Ініціалізація Leaflet
app.config['LEAFLET_DEFAULT_CENTER'] = (48.625, 22.292)
app.config['LEAFLET_DEFAULT_ZOOM'] = 13


@app.route('/')
def index():
    return render_template('index.html')

# Route to get all records
@app.route('/get_all_records', methods=['GET'])
def fetch_all_records():
    all_records = firebasesdkadmin.get_all_records()
    return jsonify(all_records)

if __name__ == '__main__':
    app.run(debug=True)
