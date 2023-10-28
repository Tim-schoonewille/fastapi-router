## FastAPI Router

### What is it?

This is a FastAPI router library that can automatically initialize routers from a directory. It is useful for organizing your FastAPI application into multiple routers, making it easier to maintain and scale.

### How to use it

To use the FastAPI Router library, first create an instance of the `FastAPIRouter` class. You can specify the root path of the router directory, as well as a list of folders and files to exclude.

```python
from fastapi_router import FastAPIRouter

api_router = FastAPIRouter(
    root_path="app/routers",
    exclude_folders=["__pycache__"],
    exclude_files=["__init__.py"],
)


Next, call the `init_routers()` method on the `FastAPIRouter` instance. This method will recursively scan the router directory and initialize all of the routers found within.

python
api_router.init_routers(app=app)


Finally, include the `FastAPIRouter` instance in your FastAPI application using the `app.include_router()` method.

python
app.include_router(api_router)


### Example

The following example shows how to use the FastAPI Router library to organize a FastAPI application into multiple routers:

python
# app/routers/api_router.py

from fastapi import FastAPI

router = FastAPIRouter()

@router.get("/")
async def index():
    return {"message": "Hello, world!"}


# app/routers/sub_router/sub_router.py

from fastapi import FastAPI

router = FastAPIRouter()

@router.get("/users")
async def get_users():
    return ["user1", "user2"]


# main.py

from fastapi import FastAPI
from fastapi_router import FastAPIRouter

app = FastAPI()

api_router = FastAPIRouter()
api_router.init_routers(app=app)

app.include_router(api_router)


This example will create two routers:

* `api_router`: This router will contain the main API endpoints for the application, such as the `/` endpoint that returns a greeting.
* `sub_router`: This router will contain the API endpoints for a specific feature of the application, such as the `/users` endpoint that returns a list of users.

To start the FastAPI application, run the following command:

"
uvicorn main:app --reload
"

You can then access the API endpoints at the following URLs:


http://localhost:8000/
http://localhost:8000/users


### Benefits

The FastAPI Router library provides a number of benefits, including:

* **Automatic router initialization:** The FastAPI Router library can automatically initialize routers from a directory, which saves you time and effort.
* **Organization:** The FastAPI Router library allows you to organize your FastAPI application into multiple routers, making it easier to maintain and scale.
* **Flexibility:** The FastAPI Router library is flexible enough to be used in a variety of ways. You can use it to initialize routers from a single directory, or from multiple directories. You can also use it to exclude folders and files from being scanned.

### Conclusion

The FastAPI Router library is a powerful tool that can help you to organize and manage your FastAPI applications. It is easy to use and provides a number of benefits, such as automatic router initialization and flexibility.


I hope this is helpful!
