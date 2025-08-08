from flask import Flask, jsonify
from flask_cors import CORS
import time
import threading

app = Flask(__name__)
CORS(app)  # allow cross-origin requests from frontend

simulation_data = {
    'bg': 100,
    'temp_basal': 0.0,
    'last_updated': time.time()
}

def simulation_loop():
    while True:
        # simulate BG changes (placeholder logic)
        simulation_data['bg'] += 1
        simulation_data['last_updated'] = time.time()
        time.sleep(300)  # update every 5 minutes

threading.Thread(target=simulation_loop, daemon=True).start()

@app.route('/status')
def status():
    return jsonify(simulation_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
