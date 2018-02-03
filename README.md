The database is horizontally fragmented according to departments maintaining student registrations  , professors' schedules and students schedules in a distributed fashion.

Application has a Oracle 11g database, Instead of creating triggers we use Django signals.py to maintain consistency. We enable Django to use the distributed database by using db_route.py.


