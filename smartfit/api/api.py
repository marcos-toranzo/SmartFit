from fastapi import FastAPI, Response, status
from typing import Optional, List

from smartfit.api.models import RoutineModel, RoutineId, UserModel

app = FastAPI()

# Temporal storage of entities. Change for real persistent storage
__routines = list[RoutineModel]()
__users = list[UserModel]()


@app.get("/")
def read_root():
    return {"Home Page": "Wellcome to the SmartFit API"}


@app.get("/routines/", status_code=200)
def get_routine(response: Response, id: Optional[RoutineId] = None):
    result_routines = list[RoutineModel]()

    if id == None:
        result_routines = __routines
    else:
        result_routines = [
            routine for routine in __routines if routine.id == id]

        if len(result_routines) == 0:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {'Error': 'Routine with id {0} not found.'.format(id)}

    return {'routines': result_routines}
