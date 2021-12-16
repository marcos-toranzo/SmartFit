from typing import Optional
from fastapi import FastAPI, Response, status, Request

from smartfit.api.models import RoutineModel, RoutineId, RoutineModelForCreation, UserModel, UserModelForCreation, WorkoutTable
import smartfit.api.controller as controller
import smartfit.api.database_provider as db

app = FastAPI()


@app.get("/")
def read_root():
    return {"Home Page": "Wellcome to the SmartFit API"}


# [US.1] As a consumer user, I would like to get fit by receiving a list of
# routines according to my requirements, so I can chose one of them and do it
# [US.4] As a consumer user, I want to receive my list of recommendation ordered
# from best suited to worst suited, so I don't waste time looking for the best myself
# since is complicated to notice it right away
@app.get("/routines/recommend/", status_code=status.HTTP_200_OK)
def get_recommended_routines(request: Request, response: Response):
    try:
        workout_table = request.query_params

        routines = db.get_routines()

        recommended_routines = controller.get_recommended_routines(
            workout_table, routines)

        if(recommended_routines == None):
            response.status_code = status.HTTP_400_BAD_REQUEST

            return {'Error': 'Invalid workout table'}
    except:
        response.status_code = status.HTTP_400_BAD_REQUEST

        return {'Error': 'Invalid workout table'}

    return {'recommended_routines': recommended_routines}


# [US.2] As a consumer user, I would like to know how good reviewed is a specific
# routine, so I can judge whether to do it if it has good reviews or not
# [US.3] As a consumer user, I would like the workload of a routine for every specific
# part of the body, so I can know if I want to exercise that part or not
@app.get("/routines/", status_code=status.HTTP_200_OK)
def get_routines():
    routines = db.get_routines()

    return {'routines': routines}


@app.get("/routines/{id}", status_code=status.HTTP_200_OK)
def get_routine(response: Response, id: RoutineId):
    routine = db.get_routine(id)

    if routine == None:
        response.status_code = status.HTTP_404_NOT_FOUND

        return {'Error': 'Routine with id {0} not found.'.format(id)}

    return routine


# [US.5] As a contributor user, I would like to upload a routine with personalized
# data, so other users could use it and review it
@app.post("/routines/", status_code=status.HTTP_201_CREATED)
def upload_routine(routine: RoutineModelForCreation, response: Response):
    result = db.add_routine(routine)

    if result == None:
        response.status_code = status.HTTP_400_BAD_REQUEST

        return {'Error': 'Could not insert routine.'}

    return result


@app.get("/users/{id}", status_code=status.HTTP_200_OK)
def get_user(id: int, response: Response):
    user = db.get_user(id)

    print(user)
    if user == None:
        response.status_code = status.HTTP_404_NOT_FOUND

        return {'Error': 'User with id {0} not found.'.format(id)}

    return user


@app.post("/users/",  status_code=status.HTTP_201_CREATED)
def create_user(user: UserModelForCreation, response: Response):
    result = db.create_user(user)

    if result == None:
        response.status_code = status.HTTP_400_BAD_REQUEST

        return {'Error': 'Could not create user.'}

    return result
