# API General Design

Every code related to the design of the API is inside of the directory [smartfit/api/](https://github.com/marcos-toranzo/SmartFit/tree/main/smartfit/api). Here we can find:

- `api.py`: [here](https://github.com/marcos-toranzo/SmartFit/blob/main/smartfit/api/api.py) we can find the API's main code. Here are defined the routes, as well as the functions that get triggered once those routes are reached. They are defined like below. We first create our FastAPI app:

```python
from fastapi import FastAPI

app = FastAPI(title='SmartFit')
```

and then define the different routes:

```python
@app.get('/', status_code=status.HTTP_200_OK)
def read_root():
    logger.info('Home Page reached')
    return {'Home Page': 'Welcome to the SmartFit API'}
```

Here we are defining a route `'/'` (root), with the GET Method, that return `200 OK` status code if everything goes well, as specified in the decorator on top of the function `read_root()`. We make use of the standar Python library `logger` for logging messages (configuration in the [config.py](https://github.com/marcos-toranzo/SmartFit/blob/main/smartfit/api/config.py) file). In this case we are sending an info message indicating that the Home Page (root) was reached. Finally, the function return a Python `dict` that will be serialized as a `JSON` object and returned to the request, showing us `{'Home Page': 'Welcome to the SmartFit API'}` when we access that route.

The same we defined a `GET` method, we can define:

```python
@app.post
@app.patch
@app.put
@app.delete
```

for `POST`, `PATCH`, `PUT` and `DELETE` methods, respectively.

The path params can be specified like:

```python
@app.get('/routines/{id}', status_code=status.HTTP_200_OK)
def get_routine(id: int):
  [...]
```

Here we are expecting a param of type `int` to be passed along in the path. For example, if `/routines/3` was reached, `id` would be `3`.

The query params can be specified like:

```python
@app.get("/routines/")
def read_routines(a: int = 0, b: int = 10):
  [...]
```

Where, in case of hitting the route `/routines/?a=3&b=4`, we would get `a: 3` and `b: 4`.

In the case of the body, it can be expected like:

```python
@app.post('/users/')
def create_user(user: UserModelForCreation):
  [...]
```

Where in this case we are expecting a object of type `UserModelForCreation` to be passed as body in the form of a `JSON` object. This models are created with the help of the library `pydantic` and are defined like:

```python
from pydantic import BaseModel


class FitnessProfileModel(BaseModel):
    age: Optional[int] = 20
    health_state: Optional[HealthState] = HealthState.Normal
    height: Optional[int] = 170
    physical_activity: Optional[PhysicalActivity] = PhysicalActivity.Active
    weight: Optional[int] = 70


class UserModelForCreation(BaseModel):
    name: str
    last_name: str
    fitness_profile_model: FitnessProfileModel
    rating: int
```

Here we are extending the class `BaseModel`, and specifying the fields we are expecting, for example, in this case, this `JSON` would represent a `UserModelForCreation`:

```json
  'name': 'Jane',
  'last_name': 'Smith',
  'fitness_profile_model': {
    'age': 26,
    'health_state': 'Ill',
    'height': 155,
    'physical_activity': 'Sedentary',
    'weight': 45
  },
  'rating': 0
```

This model will be serialized by the framework and given to the function as a `UserModelForCreation`. The models are defined in the [models.py](https://github.com/marcos-toranzo/SmartFit/blob/main/smartfit/api/models.py) file.

- `config.py`: [here](https://github.com/marcos-toranzo/SmartFit/blob/main/smartfit/api/config.py) we can find the configurations for the server. For example, the configuration for the logger to use, as well as the configuration of the server, like the host and port to use, getting them from the `.env` file if exists, if not, defaulting to `host: 127.0.0` and `port: 8000`.
- `controller.py`: [here](https://github.com/marcos-toranzo/SmartFit/blob/main/smartfit/api/controller.py) we store the auxiliary methods to handle and modify the information stored in order to provide the neccesary information to the user. Right now the only method there is is one that filter the stored routines for those that exercise at leats one of the body parts specified in the `workout_table` param.
- `database_provider.py`: [here](https://github.com/marcos-toranzo/SmartFit/blob/main/smartfit/api/database_provider.py) we store method to handle the communication with our database. Right now it simulates a database by keeping a list of routines and users in memory, loosing all of them on restart or reload.
- `models.py`: [here](https://github.com/marcos-toranzo/SmartFit/blob/main/smartfit/api/models.py) we define the different models to use in the API. In some cases, up to 3 different models will be created in order to separate the different situations, for example:

```python
class UserModel(BaseModel):
    id: UserId
    name: str
    last_name: str
    fitness_profile_model: FitnessProfileModel
    rating: int


class UserModelForCreation(BaseModel):
    name: str
    last_name: str
    fitness_profile_model: FitnessProfileModel
    rating: int


class UserModelForEdition(BaseModel):
    fitness_profile_model: FitnessProfileModel
```

In the first case, it is the model the `GET` functions related to `User` would return, containing the `id`, but when we need to create an user, an `id` is not needed since it will be assigned by the database on insertion, so we create the second model. The third model is when we need to update the information, and since we only allow the user to change their fitness profile, this is the only field available.

In order to run the server we need to run:

```shell
uvicorn smartfit.api.api:app --reload --host HOST --port $PORT
```

or to call `make run-server`, that will automatically use the HOST and PORT defined in the `.env` file, if any.

The design of the API was based on the [FastAPI's official documentation](https://fastapi.tiangolo.com/tutorial/).
