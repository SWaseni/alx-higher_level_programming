Object-relational mapping
It's all about linking  two amazing worlds: Databases and Python!
In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

In the second part,Use the module SQLAlchemy an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM,the biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, My code won’t be “storage type” dependent. I will be able to change my storage easily without re-writing my entire project.

Without ORM:
