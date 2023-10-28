## FastAPI Router

### What is it?

This is a FastAPI router library that can automatically initialize routers from a directory. It is useful for organizing your FastAPI application into multiple routers, making it easier to maintain and scale.

### How to use it

To use the FastAPI Router library, first create an instance of the `FastAPIRouter` class. You can specify the root path of the router directory, as well as a list of folders and files to exclude.

Next, call the `init_routers()` method on the `FastAPIRouter` instance. This method will recursively scan the router directory and initialize all of the routers found within.

Finally, include the `FastAPIRouter` instance in your FastAPI application using the `app.include_router()` method.

### Example

```python
from fastapi_router import FastAPIRouter
app = FastAPI()
api_router = FastAPIRouter()


api_router.init_routers(app=app)




### Benefits

* **Automatic router initialization:** The FastAPI Router library can automatically initialize routers from a directory, which saves you time and effort.
* **Organization:** The FastAPI Router library allows you to organize your FastAPI application into multiple routers, making it easier to maintain and scale.
* **Flexibility:** The FastAPI Router library is flexible enough to be used in a variety of ways. You can use it to initialize routers from a single directory, or from multiple directories. You can also use it to exclude folders and files from being scanned.

### Usage

#### Installation


pip install fastapi-router


### Usage

from fastapi_router import FastAPIRouter
app = FastAPI()
api_router = FastAPIRouter()


api_router.init_routers(app=app)




#### Router directory structure

The FastAPI Router library will automatically initialize all of the routers found in the `root_path` directory. The directory structure can be as follows:


app/routers/
├── api_router.py
└── sub_router/
    ├── __init__.py
    └── sub_router.py


The `api_router.py` file will contain the main router for your application. The `sub_router/` directory will contain a sub-router for a specific feature of your application.

#### Router files

Each router file should contain a `router` variable. The `router` variable should be an instance of the `FastAPIRouter` class.

python
# api_router.py

from fastapi import FastAPI

router = FastAPIRouter()

@router.get("/")
async def index():
    return {"message": "Hello, world!"}

## Including routers in your FastAPI application
To include a router in your FastAPI application, call the app.include_router() method.


# main.py

from fastapi import FastAPI
from fastapi_router import FastAPIRouter

app = FastAPI()
api_router = FastAPIRouter()


api_router.init_routers(app=app)

### Conclusion

The FastAPI Router library is a powerful tool that can help you to organize and manage your FastAPI applications. It is easy to use and provides a number of benefits, such as automatic router initialization and flexibility.
