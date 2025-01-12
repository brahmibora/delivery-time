from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    data = request.get_json()

    # Assuming you have a function to calculate delivery time
    delivery_time = calculate_delivery_time(data)

    # Return the result as JSON
    return jsonify({'delivery_time': delivery_time})


def calculate_delivery_time(data):
    # Example calculation (replace with your own logic)
    age = int(data['age'])
    distance = float(data['distance'])
    ratings = int(data['ratings'])
    vehicle_type = data['vehicle_type']

    # Simple calculation for demonstration purposes
    # Modify this to fit your actual model or logic
    delivery_time = (distance / 5) * (5 - ratings) + (age / 100) * 10

    return round(delivery_time, 2)

if __name__ == '__main__':
    app.run(debug=True)
