
from typing import List, Optional

from smartfit.api.models import RoutineModel, RoutineModelForCreation, UserModel, UserModelForCreation
from smartfit.entities.routine import Routine

# Temporary storage of entities. Change for real persistent storage
__routines = list[RoutineModel]()
__users = list[UserModel]()

# Temporary couters for entities ids
__routines_counter = 0
__users_counter = 0


def add_routine(routine: RoutineModelForCreation) -> Optional[RoutineModel]:
    global __routines_counter

    try:
        user = get_user(routine.uploaded_by)

        if(user == None):
            return None

        workout_table = Routine.build_workout_table(routine.exercises)

        new_routine = RoutineModel(
            id=__routines_counter, workout_table=workout_table, ** routine.dict())

        __routines_counter += 1

        __routines.append(new_routine)

        return new_routine
    except:
        return None


def get_routines() -> List[RoutineModel]:
    return __routines


def get_routine(id: int) -> Optional[RoutineModel]:
    result_routines = [
        routine for routine in __routines if routine.id == id]

    if len(result_routines) == 0:
        return None
    else:
        return result_routines[0]


def get_user(id: int) -> Optional[UserModel]:
    result_users = [
        user for user in __users if user.id == id]

    if len(result_users) == 0:
        return None
    else:
        return result_users[0]


def create_user(user: UserModelForCreation) -> Optional[UserModel]:
    global __users_counter

    try:
        new_user = UserModel(id=__users_counter, ** user.dict())

        __users_counter += 1

        __users.append(new_user)

        return new_user
    except:
        return None
