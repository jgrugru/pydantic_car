# import datetime
# from typing import Optional

# from pydantic import EmailStr

# from redis_om import HashModel, Migrator, Field


# class Customer(HashModel):
#     first_name: str
#     last_name: str = Field(index=True)
#     email: EmailStr
#     join_date: datetime.date
#     age: int = Field(index=True)
#     bio: Optional[str]


# # Now, if we use this model with a Redis deployment that has the
# # RediSearch module installed, we can run queries like the following.

# # Before running queries, we need to run migrations to set up the
# # indexes that Redis OM will use. You can also use the `migrate`
# # CLI tool for this!
# # Migrator().run()

# andrew = Customer(
#     first_name="Andrew",
#     last_name="Brookins",
#     email="andrew.brookins@example.com",
#     join_date=datetime.date.today(),
#     age=38,
#     bio="Python developer, works at Redis, Inc."
# )
# andrew.save()

# # Find all customers with the last name "Brookins"
# Customer.find(Customer.last_name == "Brookins").all()

# # Find all customers that do NOT have the last name "Brookins"
# # Customer.find(Customer.last_name != "Brookins").all()

# # Find all customers whose last name is "Brookins" OR whose age is
# # 100 AND whose last name is "Smith"
# # Customer.find((Customer.last_name == "Brookins") | (
# #         Customer.age == 100
# # ) & (Customer.last_name == "Smith")).all()


#!/usr/bin/env python3

# step 1: import the redis-py client package
import redis

# step 2: define our connection information for Redis
# Replaces with your configuration information
redis_host = "localhost"
redis_port = 6379
redis_password = ""


def hello_redis() -> None:
    """Example Hello Redis Program"""

    # step 3: create the Redis Connection object
    try:

        # The decode_repsonses flag here directs the client to convert the responses from Redis into Python strings
        # using the default encoding utf-8.  This is client specific.
        r = redis.StrictRedis(
            host=redis_host,
            port=redis_port,
            password=redis_password,
            decode_responses=True,
        )

        # step 4: Set the hello message in Redis
        r.set("msg:hello", "Hello Redis!!!")

        # step 5: Retrieve the hello message from Redis
        msg = r.get("msg:hello")
        print(msg)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    hello_redis()
