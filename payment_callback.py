from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/payment-callback', methods=['POST'])
def payment_callback():
    # Handle payment callback from Coinbase Commerce:
    data = request.json
    charge_id = data['event']['data']['id']
    status = data['event']['data']['timeline'][0]['status']

    # Update the payment status in your platform's database
    # Example: update_payment_status_in_database(charge_id, status)

    return jsonify({'message': 'Payment callback received successfully'})

if __name__ == '__main__':
    app.run(debug=True)
