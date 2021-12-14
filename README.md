# Transactions API

To start app with docker-compose:
```
docker-compose -f docker-compose.yml up --build
```

To run tests (after building on previous step):
```
docker run -v $(pwd)/.:/usr/srv transactions bash -c "python manage.py test"
```

echo '{"username":"bob_doe","name": "Jane Doe", "first_name":"Jane","email": "bob@email.com"}' | http --verbose :8000/users

echo '[{"reference": "000051", "account": 1, "date": "2020-01-13", "amount": "51.13", "type": "outflow", "category": "groceries", "user": 2},{"reference": "000052", "account": 1, "date": "2020-01-13", "amount": "51.13", "type": "outflow", "category": "groceries", "user": 2},{"reference": "000053", "account": 1, "date": "2020-01-13", "amount": "-51.13", "type": "outflow", "category": "groceries", "user": 2}]' | http --verbose :8000/transactions/

## Expectations

- Can you highlight the parts of the application that are likely to be performance bottlenecks when the user base
grows to, say, 10 million users? How would you solve them (you don’t need to solve them in code, just outlining
and explaining the strategy to solve them is sufficient).