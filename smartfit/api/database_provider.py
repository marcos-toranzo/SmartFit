
from typing import List, Optional

from smartfit.api.models import RoutineModel, RoutineModelForCreation, UserModel, UserModelForCreation
from smartfit.entities.routine import Routine

# Temporary storage of entities. Change for real persistent storage
routines = list[RoutineModel]()
users = list[UserModel]()

# Temporary couters for entities ids
routines_counter = 0
users_counter = 0


def add_routine(routine: RoutineModelForCreation) -> Optional[RoutineModel]:
    global routines_counter

    try:
        user = get_user(routine.uploaded_by)

        if(user == None):
            return None

        workout_table = Routine.build_workout_table(routine.exercises)

        new_routine = RoutineModel(
            id=routines_counter, workout_table=workout_table, ** routine.dict())

        routines_counter += 1

        routines.append(new_routine)

        return new_routine
    except:
        return None


def get_routines() -> List[RoutineModel]:
    return routines


def get_routine(id: int) -> Optional[RoutineModel]:
    result_routines = [
        routine for routine in routines if routine.id == id]

    if len(result_routines) == 0:
        return None
    else:
        return result_routines[0]


def edit_routine(id: int, new_routine: RoutineModel):
    global routines

    routines = [routine if routine.id !=
                id else new_routine for routine in routines]


def get_user(id: int) -> Optional[UserModel]:
    result_users = [
        user for user in users if user.id == id]

    if len(result_users) == 0:
        return None
    else:
        return result_users[0]


def create_user(user: UserModelForCreation) -> Optional[UserModel]:
    global users_counter

    try:
        new_user = UserModel(id=users_counter, ** user.dict())

        users_counter += 1

        users.append(new_user)

        return new_user
    except:
        return None


def edit_user(id: int, new_user: UserModel):
    global users

    users = [user if user.id !=
             id else new_user for user in users]
