# Celery Example

Most basic example.

Workflow:

Scheduler -> Redis -> Workers


Scheduler puts a task in redis every 5 seconds and the worker executes it. They both rely on the same docker
container...

To run this example:

1. docker-compose build
2. docker-compose up

Then watch the worker do its thing...
