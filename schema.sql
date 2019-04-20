DROP TABLE IF EXISTS dog;

CREATE TABLE dog (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    owner TEXT NOT NULL,
    notes TEXT
);

Your assignment is to create a RESTful API to track important information about our office dogs. 
A dog’s schema should contain a unique ID, the dog’s name, the dog’s owner’s name, 
and notes about the dog. The methods and endpoints should be:

GET /dogs - List all dogs
POST /dogs - Add a new dog 😄
GET /dogs/:id - Get details for one dog
PUT /dogs/:id - Update details for one dog
DELETE /dogs/:id - Remove a dog ☹️