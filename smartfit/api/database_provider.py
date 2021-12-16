
from typing import List, Optional

from smartfit.api.models import RoutineModel, RoutineModelForCreation, UserModel, UserModelForCreation
from smartfit.entities.routine import Routine

# Temporary storage of entities. Change for real persistent storage
__routines = list[RoutineModel]()
__users = list[UserModel]()

# Hold this data accross reloads. Remove this before merging into production
__users = [
    UserModel(**{
        "id": 0,
        "name": "Marcos",
        "last_name": "Toranzo",
        "fitness_profile_model": {
            "age": 25,
            "health_state": "Normal",
            "height": 178,
            "physical_activity": "SomewhatActive",
            "weight": 60
        },
        "rating": 0
    }),
    UserModel(**{
        "id": 1,
        "name": "Eliane",
        "last_name": "Puerta",
        "fitness_profile_model": {
            "age": 26,
            "health_state": "Ill",
            "height": 155,
            "physical_activity": "Sedentary",
            "weight": 45
        },
        "rating": 0
    })
]

__routines = [
    RoutineModel(**{
        "id": 0,
        "description": "Test description",
        "uploaded_by": 0,
        "likes": 1,
        "dislikes": 5,
        "comments": [
            "comm1",
            "comm2"
        ],
        "tags": [
            "tag1",
            "tag2",
            "tag3"
        ],
        "exercises": [
            {
                "description": "Ex1",
                "workout_table": {
                    "Neck": 20,
                    "Legs": 50
                },
                "steps": [
                    {
                        "step_image_url": "url1",
                        "duration_in_seconds": 20
                    },
                    {
                        "step_image_url": "url2",
                        "duration_in_seconds": 10
                    },
                    {
                        "step_image_url": "url3",
                        "duration_in_seconds": 15
                    }
                ]
            },
            {
                "description": "Ex2",
                "workout_table": {
                    "Neck": 40,
                    "Abdomen": 60
                },
                "steps": [
                    {
                        "step_image_url": "url4",
                        "duration_in_seconds": 11
                    },
                    {
                        "step_image_url": "url5",
                        "duration_in_seconds": 7
                    },
                    {
                        "step_image_url": "url6",
                        "duration_in_seconds": 5
                    }
                ]
            }
        ],
        "workout_table": {
            "Neck": 40,
            "Legs": 50,
            "Abdomen": 60
        }}
    ),
    RoutineModel(**{
        "id": 1,
        "description": "Test description2",
        "uploaded_by": 0,
        "likes": 1,
        "dislikes": 5,
        "comments": [],
        "tags": [],
        "exercises": [
            {
                "description": "Ex1",
                "workout_table": {
                    "Neck": 20,
                    "Legs": 50
                },
                "steps": [
                    {
                        "step_image_url": "url1",
                        "duration_in_seconds": 20
                    },
                    {
                        "step_image_url": "url2",
                        "duration_in_seconds": 10
                    },
                    {
                        "step_image_url": "url3",
                        "duration_in_seconds": 15
                    }
                ]
            }
        ],
        "workout_table": {
            "Neck": 20,
            "Legs": 50
        }
    }),
    RoutineModel(**{
        "id": 2,
        "description": "Test description3",
        "uploaded_by": 1,
        "likes": 10,
        "dislikes": 2,
        "comments": [],
        "tags": [],
        "exercises": [
            {
                "description": "Ex1",
                "workout_table": {
                    "Neck": 10,
                    "Legs": 10
                },
                "steps": [
                    {
                        "step_image_url": "url1",
                        "duration_in_seconds": 20
                    }
                ]
            }
        ],
        "workout_table": {
            "Neck": 10,
            "Legs": 10
        }
    }),
]

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


def edit_routine(id: int, new_routine: RoutineModel):
    global __routines

    print('ROUTINES --------------------------------------')
    print(__routines)
    print('-----------------------------------------------')
    print('NEW_ROUTINE -----------------------------------')
    print(new_routine)
    print('-----------------------------------------------')

    __routines = [routine if routine.id !=
                  id else new_routine for routine in __routines]


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


def edit_user(id: int, new_user: UserModel):
    global __users

    __users = [user if user.id !=
               id else new_user for user in __users]
