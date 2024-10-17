from flask import Flask, render_template, jsonify, request

app = Flask(__name__, static_url_path='/model', static_folder='model')

# Route to serve the main HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Route to receive pose data (if needed)
@app.route('/pose-data', methods=['POST'])
def receive_pose_data():
    data = request.json
    print(f"Received Pose Data: {data}")
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
                                                                                                                        