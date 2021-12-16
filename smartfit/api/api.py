from fastapi import FastAPI, Response, status, Request
from typing import Optional

from smartfit.api.models import RoutineModel, RoutineId, UserModel, WorkoutTable
from smartfit.api.controller import get_recommended_routines

app = FastAPI()

# Temporal storage of entities. Change for real persistent storage
__routines = list[RoutineModel]()
__users = list[UserModel]()


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
    workout_table = request.query_params

    recommended_routines = get_recommended_routines(workout_table, __routines)

    if(recommended_routines == None):
        response.status_code = status.HTTP_400_BAD_REQUEST

        return {'Error': 'Invalid workout table'}

    return {'recommended_routines': recommended_routines}


# [US.2] As a consumer user, I would like to know how good reviewed is a specific
# routine, so I can judge whether to do it if it has good reviews or not
# [US.3] As a consumer user, I would like the workload of a routine for every specific
# part of the body, so I can know if I want to exercise that part or not
@app.get("/routines/", status_code=status.HTTP_200_OK)
def get_routine():
    return {'routines': __routines}


@app.get("/routines/{id}", status_code=status.HTTP_200_OK)
def get_routine(response: Response, id: RoutineId):

    result_routines = [
        routine for routine in __routines if routine.id == id]

    if len(result_routines) == 0:
        response.status_code = status.HTTP_404_NOT_FOUND

        return {'Error': 'Routine with id {0} not found.'.format(id)}

    return {'routines': result_routines}
