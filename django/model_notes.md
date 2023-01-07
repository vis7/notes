abstract inheritance - do not create table of parent class. used to reuse the code to multiple child classes

multitable inheritance - create seprate table of parent class.

# proxy inheritance
In Django, a proxy model is a special type of model that doesn't have its own database table, but rather "proxies" or "forwards" all operations to a parent model. This allows you to create a model that behaves the same as an existing model, but with additional or modified behavior.

Proxy models can be useful in a variety of situations. For example, you might use a proxy model to add custom methods to an existing model, or to override the default behavior of an existing model in a specific context.

usage
- To add custom managers to an existing model
- To override the default __str__ method of an existing model:
- To modify the default ordering of an existing model
- To add a custom field to an existing model

