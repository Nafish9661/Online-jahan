import requests
import json

class WhatsAppAPI:
    def __init__(self, access_token, phone_number_id):
        self.access_token = access_token
        self.phone_number_id = phone_number_id
        self.api_url = f"https://graph.facebook.com/v20.0/{self.phone_number_id}/messages"

    def send_template_message(self, to_number, template_name, language_code):
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
        data = {
            "messaging_product": "whatsapp",
            "to": to_number,
            "type": "template",
            "template": {
                "name": template_name,
                "language": {
                    "code": language_code
                }
            }
        }
        response = requests.post(self.api_url, headers=headers, data=json.dumps(data))
        return response.json()
