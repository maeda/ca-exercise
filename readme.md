# Assumptions

- I'm assuming the database backend is more robust than sqlite (ex.: postgres or even mysql), 
so that the race conditions problems for inserts will be handled by database backend.
- In addition to that, I'm assuming that database backend support read committed transactions, so it won't face
read locking while inserts are happening since read committed transactions returns already committed data.
- I didn't implement access control assuming that an api gateway is responsible by it.
- Since it's an endpoint api, I'm assuming that it will accept HTTPS connections only even it is behind by api gateway.
- As applications are responsible for generate session id, I'm assuming that an external service is generating these
session ids and returning ids which application can get.


# Decisions

- I have made the solutions as simples as possible
- I tried to use libraries mostly to avoid reinvent the wheel
- There is no admin section configured since it was not scope of this specifications
- I'm using django and django-rest-framework as a base of this solution due the out-of-the-box solutions their offer.

# Conclusions 
All requirements has been implemented like:
- Queryies for data & analytics team (session, category and time range)
- Logging for requests
- Timestamp validation
- Query response time for read endpoints
- Concurrent requiriments (if we consider a good database as a backend)

I decided do not use celery to avoid, even though it is a great solution for message system, to avoid adding a 
accidental complexity since it is a simple solution. If it is the case and since this solution is simple, I believe
it's not big deal to add message system via celery.
