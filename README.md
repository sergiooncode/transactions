# Transactions API

To start app with docker-compose:
```
docker-compose -f docker-compose.yml up --build
```

To run tests (after building on previous step):
```
docker run -v $(pwd)/.:/usr/srv transactions bash -c "python manage.py test"
```

# How to use the API

- Create a user
```
curl -v http://localhost:8000/users/create/ -H 'Content-Type: application/json' -d '{"name": "Bob Doe", "email": "bob@email.com","age":"37"}'
```

- Create an account for that user
```
curl -v http://localhost:8000/accounts/ -H 'Content-Type: application/json' -d '{"username": "bob_doe", "account_number":"S00098"}'
```

- Create a few transactions
```
curl -v http://localhost:8000/transactions/ -H 'Content-Type: application/json' -d '[{"reference": "000051", "account": 1, "date": "2020-01-13", "amount": "2500.13", "type": "inflow", "category": "salary"}, {"reference": "000052", "account": 1, "date": "2020-01-13", "amount": "-500.13", "type": "outflow", "category": "rent"}]'
```

- Get the summary by account for a given username
```
curl -v http://localhost:8000/summary/bob_doe/account/
```
```
[{"account": "1", "total_inflow": "2500.13", "total_outflow": "-500.13", "balance": "2000.00"}]
```

- Get the summary by category for a given username
```
curl -v http://localhost:8000/summary/bob_doe/category/
```
```
{"inflow": {"salary": "2500.13"}, "outflow": {"rent": "-500.13"}}
```

# Development
- Three apps were created for this project: users, accounts and transactions. The reason for this is to make each app
self-contained which as a beneficial side-effect makes that the models of each app can evolve independently
- The package rest_framework_bulk was used for bulk transaction creation
- Files are formatted using Black.

# Considerations
- The username is not required as part of the endpoint to create users
however is convenient to use the username as the lookup field instead of
a primary key, along that line a username is generated from the name provided
and used in the creation of the user

## Expectations

- Can you highlight the parts of the application that are likely to be performance bottlenecks when the user base
grows to, say, 10 million users? How would you solve them (you don’t need to solve them in code, just outlining
and explaining the strategy to solve them is sufficient).

Answer: The transaction table in the transactions app could grow extremely large if the user base grows into the millions
considering also that a user can have more than one account. Doing on-the-fly aggregations against that table can
become extremely costly. A couple of ways to solve that could be: 1) datamart approach, running the needed aggregations
with certain frequency so they are relevant timewise for a user and storing them in a different table of the database,
or 2) partitioning approach, in the  current table we have transactions for all account of all users, that table could
partitioned such that the transactions of users 1 to 1000 are in partition A, of users 1001 to 2001 are in partition B,
etc. This approach 2 is implemented by the main RDBMS vendors MySQL
(https://dev.mysql.com/doc/refman/5.7/en/mysql-cluster-nodes-groups.html), PostreSQL
(https://www.postgresql.org/docs/10/ddl-partitioning.html), among others