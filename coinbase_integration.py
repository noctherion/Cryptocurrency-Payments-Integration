import requests

class CoinbasePaymentGateway:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.commerce.coinbase.com"

    def create_payment(self, amount, currency, callback_url):
        # Create a payment using Coinbase Commerce API
        url = f"{self.base_url}/charges"
        headers = {
            'Content-Type': 'application/json',
            'X-CC-Api-Key': self.api_key
        }
        data = {
            'name': 'Order #123',
            'description': 'Payment for order #123',
            'local_price': {
                'amount': amount,
                'currency': currency
            },
            'pricing_type': 'fixed_price',
            'redirect_url': callback_url,
            'cancel_url': callback_url
        }
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 201:
            return response.json()['data']['hosted_url']
        else:
            print("Error creating payment:", response.text)
            return None

    def check_payment_status(self, charge_id):
        # Check the status of a payment:
        url = f"{self.base_url}/charges/{charge_id}"
        headers = {
            'X-CC-Api-Key': self.api_key
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()['data']['timeline'][0]['status']
        else:
            print("Error checking payment status:", response.text)
            return None

# Example usage:

# Set up API key from the Coinbase Commerce dashboard
api_key = "your_api_key"

# Create an instance of CoinbasePaymentGateway
payment_gateway = CoinbasePaymentGateway(api_key)

# Initiate a payment
amount = 100.0
currency = "USD"
callback_url = "https://your_platform.com/payment-callback"
hosted_url = payment_gateway.create_payment(amount, currency, callback_url)
if hosted_url:
    print("Payment initiated. Hosted URL:", hosted_url)
else:
    print("Error initiating payment.")
