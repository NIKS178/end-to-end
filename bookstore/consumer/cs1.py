
import requests

value = 'Token 6f01ba9fc4cd5b3f430ab16b13a2b005d9490089'
body_val = {
    "name": "Java",
    "author": "XXX33",
    "price": 22934.3,
    "qty": 203,
    "publication": "TTTT",
    "reviews": "stars"
}
response = requests.post('http://localhost:8000/v1/book/',
                         headers={'Authorization':value},json=body_val)
print(response.status_code)
print(response.json())