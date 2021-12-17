# Web framework selection

In order to interact with the data of our app we need to stablished a interface. In this case the architecture RESTful was used for the benefits that it brings, such as flexibility and extensibility.

Since the project is implemented in Python, it was decided to follow this idea and focus in a framework that uses Python as the main developing language of the tool. The correct framework to go with would be a micro-framework since this is a small app, but other option were kept in mind in order to find the best candidate.

## Django

The first framework that comes to mind when working with Python is [Django](https://www.djangoproject.com/). It is one the most popular and powerful. The documentation a support is great. It contains a huge amount of functionalities for many different scenarios. This makes it a little bit big in terms of number of files and size, as well as in resources that are not going to be needed nor used. Its initial configuration can be cumbersome and we are going to find a lot of code that is there just to make the tool work since we won't be able to fully use it. On top of all of this we find that the learning curve for this tool is a bit steep, frecuent in this cases. Since we are not looking nor the app needs a huge framework, this idea was eliminated from using it in the project.

## Flask

[Flask](https://flask.palletsprojects.com/en/2.0.x/) is another popular framework. Is ideal for our app in the sense that is light, minimalistic and fast. Develop an app using this tool is extremely fast and using just a few lines of code. Although, it presents some issues. First, the user is going to need a bit more about technical content that with the rest, needing to know more details that really needed in order to build an app. Also, it contains almost no library, what force us to install a lot of external libraries in order to do basic things.

## FastAPI

In this case we get the best from a lot of sides. First, [FastAPI](https://fastapi.tiangolo.com/) is crazy fast (one of the fastest) and light, easy to understand and maintain. Supports both synchronous and asynchronous code by simply using the keywork `async`, uses native python patterns and styles. Its documentation is great and its support is even better. It is built over two great libraries: [Starlette](https://www.starlette.io/) for managing the web work, and [pydantic](https://pydantic-docs.helpmanual.io/) for the data modeling and validation. Includes its own testing library through a `TestClient`. The implementation of these tests allows us to use `pytest` just the same way we've been using it for the rest of the code, eliminating the necesity of having to modify some of the continuous integration features we have implemented. Heavily based on the [testing official documentation](https://fastapi.tiangolo.com/tutorial/testing/).

For these reasons it was decided to use FastAPI for the development of the API. You can check the [general design](api_design.md) of the API for more information, or how the [endpoints](api_endpoints.md) are related to the User Stories.
