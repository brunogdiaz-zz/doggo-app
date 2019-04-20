# Doggo-App

A RESTful API to track important information about office dogs. 

Dog’s schema contains
```
unique ID
the dog’s name
the dog’s owner’s name
notes about the dog
```

The methods and endpoints should be:
```
GET /dogs - List all dogs
POST /dogs - Add a new dog 😄
GET /dogs/:id - Get details for one dog
PUT /dogs/:id - Update details for one dog
DELETE /dogs/:id - Remove a dog ☹️
```

## How to Run

```python
git clone https://github.com/brunogdiaz/doggo-app.git
cd doggo-app
pip install -r requirements.txt
flask run
```