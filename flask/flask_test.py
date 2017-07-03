import requests

r = requests.get('http://127.0.0.1:5000/api/v1/sms', data = {'key':'value'})
# r = requests.get('http://127.0.0.1:5000')
print(str(r))