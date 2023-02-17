# Zomato-clone

#Installation

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver


Now, you can run the Django server and test the API endpoints. For example, to register a user, send a POST request to http://localhost:8000/register/ with the username, email, and password in the request body. To list available foods for a restaurant, send a GET request to http://localhost:8000/restaurant/<restaurant_id>/food/ with the restaurant id as a parameter. To create an order for a user, send a POST request to http://localhost:8000/order/create/ with the user, restaurant, food, quantity, and cost in the request body.   Finally, to run the Celery beat schedule, run # celery -A Restaurant beat -l info in a separate terminal window.
