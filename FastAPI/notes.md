Other http method can be used with FastAPI
```
@app.post()
@app.put()
@app.delete()

@app.options()
@app.head()
@app.patch()
@app.trace()
```

Declaring parameter
```
# Path Parameter
item_id: Annotated[int, Path(title="The ID of the item to get", gt=0, le=1000)]

# Body Parameter
importance: Annotated[int, Body()]

# Query Parameter
q: Annotated[Union[list[str], None], Query()] = None) - Query parameter list / multiple values

# Header Parameter
user_agent: Annotated[Union[str, None], Header()] = None

# Cookie Parameter
ads_id: Annotated[Union[str, None], Cookie()] = None

# Form Parameter
username: Annotated[str, Form()]

# File Parameter
fileb: Annotated[UploadFile, File()]

```

Imports
```
from fastapi import FastAPI, Header, Cookie, Path, Query, Body, Response, status, Form, File, UploadFile, HTTPException, Request, APIRouter, Depends

from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi.testclient import TestClient


from typing import Annotated, Union
from pydantic import BaseModel, Field, HttpUrl, EmailStr


from enum import Enum


app.include_router(users.router)

client = TestClient(app)

```

parameter of query
```
            alias="item-query",
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            pattern="^fixedquery$",
            deprecated=True,
```



+ Fast api function return - You can return a dict, list, singular values as str, int, etc. You can also return Pydantic models.

+ Order of path() matters, declair plain one first and then declare path with parameters
+ Redefine path will always use first match

# Declaring Path as Parameter
```
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
```

# Diffrece Between Query Parameters, Path Parameter
You can declare multiple path parameters and query parameters at the same time, FastAPI knows which is which. query parameter are optional so we need to provide default values for them, but we can make them required by not providing values for it.

```
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    pass
```
The function parameters will be recognized as follows:

+ If the parameter is also declared in the path, it will be used as a path parameter.
+ If the parameter is of a singular type (like int, float, str, bool, etc) it will be interpreted as a query parameter.
+ If the parameter is declared to be of the type of a Pydantic model, it will be interpreted as a request body.


If you want single body parameter, you can declare it inside function signature along with other parameter like below
```
    importance: Annotated[int, Body(gt=0)],
```

# embad single body parameter
If you want it to expect a JSON with a key item and inside of it the model contents, as it does when you declare extra body parameters, you can use the special Body parameter embed

```
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results
```
Than body will be
```
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    }
}
```

quary paramter lenght validation added, add below in function defination parameter
```
from fastapi import Query
Query(max_length=50)
```

q: Annotated[str | None, Query(max_length=50)] = None - quary parameter can be strng or None, but if it present it's length can' be more than 50, It is optional, as if not provided by default it will be taken as None

q: str | None = Query(default=None)

q: Annotated[str, Query(default="rick")] = "morty" - can't declare this way, can specified default value on only one place



Using Annotated is recommended instead of the default value in function parameters, it is better for multiple reasons.
Annotated can have more than one metadata annotation

q: Annotated[str | None, Query(min_length=3, max_length=50)] = None,

q: Annotated[
        str | None, Query(min_length=3, max_length=50, pattern="^fixedquery$")
    ] = None - add regular expression

q: Annotated[str, Query(min_length=3)] = ... - required with elipsis (...)


There's an alternative way to explicitly declare that a value is required. You can set the default to the literal value ...:

You can declare that a parameter can accept None, but that it's still required. This would force clients to send a value, even if the value is None.

q: Annotated[Union[list[str], None], Query()] = None) - Query parameter list / multiple values


we can add title, description
    q: Annotated[
        str | None,
        Query(
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
        ),
    ] = None,

q: Annotated[str | None, Query(alias="item-query") - alias parameter

explore query parameters
deprecated = True - to show that that parameter will be depricated
include_in_schema=False - To exclude a query parameter from the generated OpenAPI schema (and thus, from the automatic documentation systems)



Python won't do anything with that *, but it will know that all the following parameters should be called as keyword arguments (key-value pairs), also known as kwargs. Even if they don't have a default value.


```
from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(*, item_id: int = Path(title="The ID of the item to get"), q: str):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
```



gt: greater than

le: less than or equal


item_id: Annotated[int, Path(title="The ID of the item to get", gt=0, le=1000)]

But you can also declare multiple body parameters, e.g. item and user:
```
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, user: User):
    results = {"item_id": item_id, "item": item, "user": user}
    return results
```

So, it will then use the parameter names as keys (field names) in the body, and expect a body like

```
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    }
}
```

```
@app.put("/items/{item_id}")
async def update_item(
    item_id: int, item: Item, user: User, importance: Annotated[int, Body()]
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results
```
In this case, FastAPI will expect a body like:

```
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    },
    "importance
```

The same way you can declare additional validation and metadata in path operation function parameters with Query, Path and Body, you can declare validation and metadata inside of Pydantic models using Pydantic's Field.

```
from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(embed=True)):
    results = {"item_id": item_id, "item": item}
    return results
```

Field works the same way as Query, Path and Body, it has all the same parameters, etc.

Remember that when you import Query, Path, and others from fastapi, those are actually functions that return special classes.

You can use Pydantic's Field to declare extra validations and metadata for model attributes


We can declare and use nested Model using Pydentic, we can have in depth nesting of model  

When using Field() with Pydantic models, you can also declare additional examples:
```
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str = Field(examples=["Foo"])
    description: str | None = Field(default=None, examples=["A very nice Item"])
    price: float = Field(examples=[35.4])
    tax: float | None = Field(default=None, examples=[3.2])


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
```

examples in JSON Schema - OpenAPI¶
When using any of:

Path()
Query()
Header()
Cookie()
Body()
Form()
File()

you can also declare a group of examples with additional information that will be added to their JSON Schemas inside of OpenAPI.

Body with examples
```
@app.put("/items/{item_id}")
async def update_item(
    item_id: int,
    item: Annotated[
        Item,
        Body(
            examples=[
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ],
        ),
    ],
):
    results = {"item_id": item_id, "item": item}
    return results
```
https://fastapi.tiangolo.com/tutorial/schema-extra-example/#using-the-openapi_examples-parameter

Using the openapi_examples Parameter

You can declare the OpenAPI-specific examples in FastAPI with the parameter openapi_examples for:

```
Path()
Query()
Header()
Cookie()
Body()
Form()
File()
```

The keys of the dict identify each example, and each value is another dict.

Each specific example dict in the examples can contain:

summary: Short description for the example.
description: A long description that can contain Markdown text.
value: This is the actual example shown, e.g. a dict.
externalValue: alternative to value, a URL pointing to the example. Although this might not be supported by as many tools as value.
```
from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Annotated[
        Item,
        Body(
            openapi_examples={
                "normal": {
                    "summary": "A normal example",
                    "description": "A **normal** item works correctly.",
                    "value": {
                        "name": "Foo",
                        "description": "A very nice Item",
                        "price": 35.4,
                        "tax": 3.2,
                    },
                },
                "converted": {
                    "summary": "An example with converted data",
                    "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                    "value": {
                        "name": "Bar",
                        "price": "35.4",
                    },
                },
                "invalid": {
                    "summary": "Invalid data is rejected with an error",
                    "value": {
                        "name": "Baz",
                        "price": "thirty five point four",
                    },
                },
            },
        ),
    ],
):
    results = {"item_id": item_id, "item": item}
    return results
```

# Response Status code
```
@app.post("/items/", status_code=201)

# usage
from fastapi import status

status.HTTP_201_CREATED
```

# Form data
When you need to receive form fields instead of JSON, you can use Form, we can declare it the same way we do Body parameter

```
from fastapi import Form
# usage
username: Annotated[str, Form()]
```

### extra
Data from forms is normally encoded using the "media type" application/x-www-form-urlencoded.

But when the form includes files, it is encoded as multipart/form-data.

# Request files
The files will be uploaded as "form data".

If you declare the type of your path operation function parameter as bytes, FastAPI will read the file for you and you will receive the contents as bytes.

Keep in mind that this means that the whole contents will be stored in memory. This will work well for small files.

But there are several cases in which you might benefit from using UploadFile.

```
@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}
```

Using UploadFile has several advantages over bytes:
- It uses a "spooled" file:
    A file stored in memory up to a maximum size limit, and after passing this limit it will be stored in disk.
- This means that it will work well for large files like images, videos, large binaries, etc. without consuming all the memory.
- You can get metadata from the uploaded file.
- It has a file-like async interface.
- It exposes an actual Python SpooledTemporaryFile object that you can pass directly to other libraries that expect a file-like object.

Attributes
- filename 
- content_type
- file

Methods
- write(data): Writes data (str or bytes) to the file.
- read(size): Reads size (int) bytes/characters of the file.
- seek(offset): Goes to the byte position offset (int) in the file.
    E.g., await myfile.seek(0) would go to the start of the file.
    This is especially useful if you run await myfile.read() once and then need to read the contents again.
- close(): Closes the file.

As all these methods are async methods, you need to "await" them.

For example, inside of an async path operation function you can get the contents with:


contents = await myfile.read()
If you are inside of a normal def path operation function, you can access the UploadFile.file directly, for example:


contents = myfile.file.read()


=> Making file optional
```
file: Annotated[Union[bytes, None], File()] = None)
file: Union[UploadFile, None] = None
```
=> Multiple File Uploads with metadata
```
from typing import Annotated

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.post("/files/")
async def create_files(
    files: Annotated[list[bytes], File(description="Multiple files as bytes")],
):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfiles/")
async def create_upload_files(
    files: Annotated[
        list[UploadFile], File(description="Multiple files as UploadFile")
    ],
):
    return {"filenames": [file.filename for file in files]}


@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)



@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}
```

# Request Forms and Files
To receive uploaded files and/or form data, first install python-multipart.
You can define files and form fields at the same time using File and Form.

```
from typing import Annotated

from fastapi import FastAPI, File, Form, UploadFile

app = FastAPI()


@app.post("/files/")
async def create_file(
    file: Annotated[bytes, File()],
    fileb: Annotated[UploadFile, File()],
    token: Annotated[str, Form()],
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }
```

# Handling Errors
```
from fastapi import HTTPException

raise HTTPException(
    staus_code=404, 
    detail="text message,
    headers={"X-Error": "There goes my error"}, # add custom headers
    )
```

=> custom exception handler
```
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


app = FastAPI()


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )


@app.get("/unicorns/{name}")
async def read_unicorn(name: str):
    if name == "yolo":
        raise UnicornException(name=name)
    return {"unicorn_name": name}
```

=> Override request validation exceptions

```
from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id == 3:
        raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
    return {"item_id": item_id}
```


# Path Operation Configuration
@app.post("/items/", response_model=Item) - is called path operation decorator


There are several parameters that you can pass to your path operation decorator to configure it.

- status_code
- tags - it can be used in OpenAPI Documentation (Swagger UI) (Enums can be used)
- summary -
- description - 
    other than parameter, You can write Markdown in the docstring, it will be interpreted and displayed correctly (taking into account docstring indentation)
- response_description - o, if you don't provide one, FastAPI will automatically generate one of "Successful response".
- deprecated - True (for deprecating path without removing it)

# Response Type
You can declare below parameter in path operation decorator
- response_model - to declare return type pydentic model
- response_model_exclude_set=True - will only include values specified by user, default values not included
- response_model_exclude_defaults -
- response_model_exclude_none - 
- respones_model_include - 
- response_model_exclude - 
- response_model_by_alias - 

FastAPI uses Pydentic model ot serialize and deserialize as we use serializers in DRF

Recommended way is to use multiple class rather than using include/exclude, one of reason is schema still show all data in docs

```
user_in = UserIn(username='jhon', password='secret')
user_dict = user_in.model_dump() # .dict() for pydantic v1

UserInDB(**user_dict)  # same as UserInDB(username='jhon', password='secret')
```

- Use inheritance to avoid data duplication in model
- If you want to use one of two model (OR) in response_model, You has to use Union.If you want multiple object of data type use can use List.



# Practical
store hashed password in db


# JSON Compitable Converter
There are some cases where you might need to convert a data type (like a Pydantic model) to something compatible with JSON (like a dict, list, etc)

```
from fastapi.encoders import jsonable_encoder

# convert complex data type to dict
json_compatible_item_data = jsonable_encoder(item)

# above can be be converted into json 
json.dumps()

```

# Body - Updates
item.model_dump(exclude_unset=True) - That would generate a dict with only the data that was set when creating the item model, excluding default values.

ou can create a copy of the existing model using .model_copy(), and pass the update parameter with a dict containing the data to update. we can do put like we done patch below

```
@app.patch("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    stored_item_data = items[item_id]
    stored_item_model = Item(**stored_item_data)
    update_data = item.dict(exclude_unset=True)
    updated_item = stored_item_model.copy(update=update_data)
    items[item_id] = jsonable_encoder(updated_item)
    return updated_item
```

# Middleware
A "middleware" is a function that works with every request before it is processed by any specific path operation. And also with every response before returning it.

A "middleware" is a function that works with every request before it is processed by any specific path operation. And also with every response before returning it.

Example
```
import time

from fastapi import FastAPI, Request

app = FastAPI()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request) # generate response
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
```


# CORS (Cross-Origin Resource Sharing)
An origin is the combination of protocol (http, https), domain (myapp.com, localhost, localhost.tiangolo.com), and port (80, 443, 8080).

So, all these are different origins:

- http://localhost
- https://localhost
- http://localhost:8080

The browser will send an HTTP OPTIONS request to the backend, and if the backend sends the appropriate headers authorizing the communication from this different origin (http://localhost:8080) then the browser will let the JavaScript in the frontend send its request to the backend.


wildcard = "*" # to allow all host


=> Use CORS Middleware
```
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return {"message": "Hello World"}
```


max_age - Sets a maximum time in seconds for browsers to cache CORS responses. Defaults to 600.


# Background Task
```
from fastapi import BackgroundTasks, FastAPI

app = FastAPI()


def write_notification(email: str, message=""):
    with open("log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)


@app.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message="some notification")
    return {"message": "Notification sent in the background"}
```


If we need to do heavy computation or complex task we can also use celery


# Testing
```
from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
```

# Debugging (Runing with uvcorn)
```
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    a = "a"
    b = "b" + a
    return {"hello world": b}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```


# need to read code and do practical
SQL (Relational) Databases
Bigger Applications - Multiple Files


# remained
dependency
security
