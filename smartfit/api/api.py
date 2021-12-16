import smartfit.api.database_provider as db
import smartfit.api.controller as controller
from smartfit.api.models import FitnessProfileModel, RoutineModel, RoutineId, RoutineModelForCreation, RoutineModelForEdition, UserModel, UserModelForCreation, UserModelForEdition, WorkoutTable
from typing import Optional
from fastapi import FastAPI, Response, status, Request
from logging.config import dictConfig
import logging
from smartfit.api.config import LogConfig


app = FastAPI()

dictConfig(LogConfig().dict())
logger = logging.getLogger('smartfit')


@app.get('/')
def read_root():
    logger.info('Home Page reached')
    return {'Home Page': 'Welcome to the SmartFit API'}


# - [US.1] As a consumer user, I would like to get fit by receiving a list of
# routines according to my requirements, so I can chose one of them and do it
# - [US.4] As a consumer user, I want to receive my list of recommendation ordered
# from best suited to worst suited, so I don't waste time looking for the best myself
# since is complicated to notice it right away
# - [US.7] As a consumer user, I would like to receive the optimal recommendation based
# on a table of workload provided, so I know that routine will be the best one to do
# based on my requirements
@app.get('/routines/recommend/', status_code=status.HTTP_200_OK)
def get_recommended_routines(request: Request, response: Response):
    try:
        workout_table = request.query_params

        routines = db.get_routines()

        recommended_routines = controller.get_recommended_routines(
            workout_table, routines)

        if(recommended_routines == None):
            response.status_code = status.HTTP_400_BAD_REQUEST
            logger.error(
                'Invalid workout table. Could not get recommended routines.')

            return {'Error': 'Invalid workout table'}
    except:
        response.status_code = status.HTTP_400_BAD_REQUEST
        logger.error(
            'Invalid workout table. Could not get recommended routines.')

        return {'Error': 'Invalid workout table'}

    logger.info('Recommended routines successfully gotten.')

    return {'recommended_routines': recommended_routines}


# - [US.2] As a consumer user, I would like to know how good reviewed is a specific
# routine, so I can judge whether to do it if it has good reviews or not
# - [US.3] As a consumer user, I would like the workload of a routine for every specific
# part of the body, so I can know if I want to exercise that part or not
@app.get('/routines/', status_code=status.HTTP_200_OK)
def get_routines():
    routines = db.get_routines()

    logger.info('Routines successfully gotten.')

    return {
        'count': len(routines),
        'routines': routines
    }


@app.get('/routines/{id}', status_code=status.HTTP_200_OK)
def get_routine(response: Response, id: RoutineId):
    routine = db.get_routine(id)

    if routine == None:
        response.status_code = status.HTTP_404_NOT_FOUND
        logger.error('Routine with id {0} not found.'.format(id))

        return {'Error': 'Routine with id {0} not found.'.format(id)}

    logger.info('Routine with id {0} successfully gotten.'.format(id))

    return routine


# - [US.5] As a contributor user, I would like to upload a routine with personalized
# data, so other users could use it and review it
@app.post('/routines/', status_code=status.HTTP_201_CREATED)
def upload_routine(routine: RoutineModelForCreation, response: Response):
    result = db.add_routine(routine)

    if result == None:
        response.status_code = status.HTTP_400_BAD_REQUEST
        logger.error('Could not insert routine.')

        return {'Error': 'Could not insert routine.'}

    logger.info('Routine successfully uploaded.')

    return result


# - [US.6] As a contributor user, I would like to be able to like and review a routine
# from another user, so other users can see more information about the routine before
# deciding to do it
@app.patch('/routines/{id}', status_code=status.HTTP_200_OK)
def update_routine(id: int, routine: RoutineModelForEdition, response: Response):
    stored_routine = db.get_routine(id)

    if(stored_routine == None):
        response.status_code = status.HTTP_400_BAD_REQUEST
        logger.error('Routine with id {0} not found.'.format(id))

        return {'Error': 'Routine with id {0} not found.'.format(id)}

    try:
        update_data = routine.dict(exclude_unset=True)
        updated_routine = stored_routine.copy(update=update_data)
        db.edit_routine(id, updated_routine)
    except:
        response.status_code = status.HTTP_400_BAD_REQUEST
        logger.error('Could not edit routine.')

        return {'Error': 'Could not edit routine.'}

    logger.info('Routine successfully updated.')

    return updated_routine


# - [US.10] As a consumer, I want to see me full name in the app so I can tell if the
# current profile is mine or I have to log in with my profile instead
# - [US.11] As a consumer, I would like to check on my personal information like
# weight or height, to see if there is something outdated.
@app.get('/users/{id}', status_code=status.HTTP_200_OK)
def get_user(id: int, response: Response):
    user = db.get_user(id)

    if user == None:
        response.status_code = status.HTTP_404_NOT_FOUND
        logger.error('User with id {0} not found.'.format(id))

        return {'Error': 'User with id {0} not found.'.format(id)}

    logger.info('User successfully gotten.')

    return user


@app.post('/users/',  status_code=status.HTTP_201_CREATED)
def create_user(user: UserModelForCreation, response: Response):
    result = db.create_user(user)

    if result == None:
        response.status_code = status.HTTP_400_BAD_REQUEST
        logger.error('Could not create user.')

        return {'Error': 'Could not create user.'}

    logger.info('User successfully created.')

    return result


# - [US.12] As a consumer, I would like to be able to edit my personal information like
# weight or height to match my current status and keep the app updated
@app.patch('/users/{id}/fitness-profile', status_code=status.HTTP_200_OK)
def update_user_fitness_profile(id: int, user_fitness_profile: FitnessProfileModel, response: Response):
    stored_user = db.get_user(id)

    if(stored_user == None):
        response.status_code = status.HTTP_400_BAD_REQUEST
        logger.error('User with id {0} not found.'.format(id))

        return {'Error': 'User with id {0} not found.'.format(id)}

    try:
        update_data = user_fitness_profile.dict(exclude_unset=True)
        updated_fitness_profile = stored_user.fitness_profile_model.copy(
            update=update_data)
        updated_user = stored_user.copy(
            update={'fitness_profile_model': updated_fitness_profile})
        db.edit_user(id, updated_user)
    except:
        response.status_code = status.HTTP_400_BAD_REQUEST
        logger.error('Could not edit user.')

        return {'Error': 'Could not edit user.'}

    logger.info('User successfully edited.')

    return updated_user
