Q1.  Django is a python frame work that helps developers build websites and web applications.
it is describe as battries included framework because, django comes with many useful features already built in the frame work
authentication, admin interface, security feature.

b.  
Model: handles data.
View: handles request and application logic
Template: display information to the user

c.
┌──────────────┐
│   Browser    │
└──────┬───────┘
       │
       │ 1. HTTP Request
       ▼
┌──────────────┐
│    Django    │
└──────┬───────┘
       │
       │ 2. Check URL
       ▼
┌──────────────┐
│   urls.py    │
└──────┬───────┘
       │
       │ 3. Send to View
       ▼
┌──────────────┐
│    View      │
└──────┬───────┘
       │
       │ 4. Get data
       ▼
┌──────────────┐
│    Model     │
│  Database    │
└──────┬───────┘
       │
       │ 5. Data returned
       ▼
┌──────────────┐
│   Template   │
└──────┬───────┘
       │
       │ 6. Generate HTML
       ▼
┌──────────────┐
│   Browser    │
│ Page shown   │
└──────────────┘

d.
The project is the whole system, while the apps are the different parts that perform specific functions.

Q2b. 
the 2 commands are makemigrations and migrate
makemigrations: tells django to look at the model and creat instruction for the database changes.
migrate: take the migration instructions and actually apply them to the database

Q3c.
A Function-Based View (FBV) is a Django view written as a Python function. It receives an HTTP request and returns an HTTP response. An advantage is that FBVs are simple and easy to understand. A disadvantage is that complex FBVs can become long and contain repetitive code.

A Class-Based View (CBV) is a Django view written as a Python class. It can use Django's built-in generic views and inheritance to reuse common behavior. An advantage is that CBVs can reduce repetitive code and make code easier to reuse. A disadvantage is that CBVs can be more difficult for beginners to understand because they use classes, inheritance, and generic view behavior.

3d.

`{{ variable }}` is used to display the value of a variable or an object's attribute in a Django template.

Example:
django
{{ book.title }}


`{% tag %}` is used to perform actions or control the template, such as loops and conditions.

Example:
django
{% for book in books %}
    {{ book.title }}
{% endfor %}

