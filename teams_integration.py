import requests
import json
import os

teams_webhook_url = "https://saultcollege.webhook.office.com/webhookb2/fb537891-ce63-42c0-bfed-d421f000bec8@9c61dd9d-3b29-4f6d-b3b1-f212de3c25da/IncomingWebhook/81847ecf776b4a10b1833db6bb6f86f4/0e2c46fe-b623-4565-8334-35f430d06c0b"

headers = {"Content-Type": "application/json"}

payload = {
		"summary": "workshop",
		"title": "Test Message",
		"sections": [
			{
				"markdown": "false",
				"text": "This message was sent by Grace"
			}
		]
}

requests.post(teams_webhook_url, headers=headers, data=json.dumps(payload))


