import requests
import json
import base64

api_key = "XXXX" # Enter your API key here
api_url = "https://api.getimg.ai/v1/stable-diffusion/text-to-image"

prompt = input("Enter a prompt for AI ArtGen: ")
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}
data = {
    "prompt": prompt,
}
response = requests.post(api_url, headers=headers, data=json.dumps(data))
if response.status_code == 200:
    image_data = response.json()
    with open("image.png", "wb") as f:
        f.write(base64.decodebytes(image_data["image"].encode()))
    print("Art saved successfully as 'image.png'!")
else:
    print(f"Error: {response.status_code}: {response.text}.")
