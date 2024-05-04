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

+ Fast api function return - You can return a dict, list, singular values as str, int, etc. You can also return Pydantic models (you'll see more about that later).

+ Order of path() matters, declair plain one first and then declare path with parameters
+ Redefine path will always use first match

# declaring path as parameter
```
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
```

# diffrece between queyr parameters, path parameter
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

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, user: User):
    results = {"item_id": item_id, "item": item, "user": user}
    return results

So, it will then use the parameter names as keys (field names) in the body, and expect a body like

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

https://fastapi.tiangolo.com/tutorial/schema-extra-example/#using-the-openapi_examples-parameter

Using the openapi_examples Parameter¶
You can declare the OpenAPI-specific examples in FastAPI with the parameter openapi_examples for:

Path()
Query()
Header()
Cookie()
Body()
Form()
File()
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

