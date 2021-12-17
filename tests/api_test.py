from fastapi.testclient import TestClient
from smartfit.api.api import app
from smartfit.api.models import UserModel, RoutineModel
import pytest
import smartfit.api.database_provider as db
from smartfit.entities.routine import Routine
from smartfit.entities.exercise import Exercise, ExerciseStep

client = TestClient(app)


@pytest.fixture
def data():
    userJohn = UserModel(
        **{
            "id": 0,
            "name": "John",
            "last_name": "Smith",
            "fitness_profile_model": {
                "age": 25,
                "health_state": "Normal",
                "height": 178,
                "physical_activity": "SomewhatActive",
                "weight": 60,
            },
            "rating": 0,
        }
    )

    userJane = UserModel(
        **{
            "id": 1,
            "name": "Jane",
            "last_name": "Smith",
            "fitness_profile_model": {
                "age": 26,
                "health_state": "Ill",
                "height": 155,
                "physical_activity": "Sedentary",
                "weight": 45,
            },
            "rating": 0,
        }
    )

    routineNeckLegsAbdomen = RoutineModel(
        **{
            "id": 0,
            "description": "Neck, Legs and Abdomen",
            "uploaded_by": 0,
            "likes": 1,
            "dislikes": 5,
            "comments": ["comm1", "comm2"],
            "tags": ["tag1", "tag2", "tag3"],
            "exercises": [
                {
                    "description": "Ex1",
                    "workout_table": {"Neck": 20, "Legs": 50},
                    "steps": [
                        {"step_image_url": "url1", "duration_in_seconds": 20},
                        {"step_image_url": "url2", "duration_in_seconds": 10},
                        {"step_image_url": "url3", "duration_in_seconds": 15},
                    ],
                },
                {
                    "description": "Ex2",
                    "workout_table": {"Neck": 40, "Abdomen": 60},
                    "steps": [
                        {"step_image_url": "url4", "duration_in_seconds": 11},
                        {"step_image_url": "url5", "duration_in_seconds": 7},
                        {"step_image_url": "url6", "duration_in_seconds": 5},
                    ],
                },
            ],
            "workout_table": {"Neck": 40, "Legs": 50, "Abdomen": 60},
        }
    )

    routineNeckBack = RoutineModel(
        **{
            "id": 1,
            "description": "Neck and Back",
            "uploaded_by": 0,
            "likes": 1,
            "dislikes": 5,
            "comments": [],
            "tags": [],
            "exercises": [
                {
                    "description": "Ex1",
                    "workout_table": {"Neck": 20, "Back": 50},
                    "steps": [
                        {"step_image_url": "url1", "duration_in_seconds": 20},
                        {"step_image_url": "url2", "duration_in_seconds": 10},
                        {"step_image_url": "url3", "duration_in_seconds": 15},
                    ],
                }
            ],
            "workout_table": {"Neck": 20, "Back": 50},
        }
    )

    routineNeckLegs = RoutineModel(
        **{
            "id": 2,
            "description": "Neck and Legs",
            "uploaded_by": 1,
            "likes": 10,
            "dislikes": 2,
            "comments": [],
            "tags": [],
            "exercises": [
                {
                    "description": "Ex1",
                    "workout_table": {"Neck": 10, "Legs": 10},
                    "steps": [{"step_image_url": "url1", "duration_in_seconds": 20}],
                }
            ],
            "workout_table": {"Neck": 10, "Legs": 10},
        }
    )

    users = [userJohn, userJane]

    routines = [routineNeckLegsAbdomen, routineNeckBack, routineNeckLegs]

    db.routines = routines
    db.users = users
    db.routines_counter = 3
    db.users_counter = 2

    return {
        "users": users,
        "routines": routines,
        "userJohn": userJohn,
        "userJane": userJane,
        "routineNeckLegsAbdomen": routineNeckLegsAbdomen,
        "routineNeckBack": routineNeckBack,
        "routineNeckLegs": routineNeckLegs,
    }


def test_home_page(data: dict):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"Home Page": "Welcome to the SmartFit API"}


def test_get_recommended_routines(data: dict):
    # Test without workout table. Should return none
    response = client.get("/routines/recommend/")

    assert response.status_code == 200
    assert response.json() == {"count": 0, "recommended_routines": []}

    # Test with only Abdomen in the workout table.
    # Should return only 1
    response = client.get("/routines/recommend/?Abdomen=10")

    assert response.status_code == 200
    assert response.json() == {
        "count": 1,
        "recommended_routines": [data["routineNeckLegsAbdomen"]],
    }

    # Test with Abdomen and Back in the workout table.
    # Should return 2
    response = client.get("/routines/recommend/?Abdomen=10&Back=10")

    assert response.status_code == 200
    assert response.json() == {
        "count": 2,
        "recommended_routines": [
            data["routineNeckLegsAbdomen"],
            data["routineNeckBack"],
        ],
    }

    # Test with Abdomen, Back and Legs in the workout table.
    # Should return all three
    response = client.get("/routines/recommend/?Abdomen=10&Back=10&Legs=10")

    assert response.status_code == 200
    assert response.json() == {"count": 3, "recommended_routines": data["routines"]}


def test_get_routines(data: dict):
    routines = data["routines"]

    response = client.get("/routines/")

    assert response.status_code == 200
    assert response.json() == {"count": len(routines), "routines": routines}


def test_get_routine(data: dict):
    routine = data["routineNeckLegsAbdomen"]

    # Test with an existing one
    response = client.get("/routines/{0}".format(routine.id))

    assert response.status_code == 200
    assert response.json() == routine

    # Test with a non-existing one
    response = client.get("/routines/3")

    assert response.status_code == 404
    assert response.json() == {"Error": "Routine with id 3 not found."}


def test_upload_routine(data: dict):
    userJohn = data["userJohn"]

    new_routine_exercises = [
        Exercise(
            description="Ex1",
            workout_table={"Neck": 15, "Legs": 12},
            steps=[ExerciseStep(step_image_url="url", duration_in_seconds=20)],
        ),
        Exercise(
            description="Ex2",
            workout_table={"Neck": 15, "Back": 10},
            steps=[ExerciseStep(step_image_url="url2", duration_in_seconds=20)],
        ),
    ]

    new_routine_exercises_data = [
        {
            "description": "Ex1",
            "workout_table": {"Neck": 15, "Legs": 12},
            "steps": [{"step_image_url": "url", "duration_in_seconds": 10}],
        },
        {
            "description": "Ex2",
            "workout_table": {"Neck": 15, "Back": 10},
            "steps": [{"step_image_url": "url2", "duration_in_seconds": 20}],
        },
    ]

    new_routine_data = {
        "description": "New Routine",
        "uploaded_by": userJohn.id,
        "likes": 2,
        "dislikes": 5,
        "comments": ["com"],
        "tags": ["tag"],
        "exercises": new_routine_exercises_data,
    }

    routine = RoutineModel(
        id=3,
        workout_table=Routine.build_workout_table(new_routine_exercises),
        **new_routine_data
    )

    response = client.post("/routines/", json=new_routine_data)

    assert response.status_code == 201
    assert response.json() == routine

    new_routine = db.get_routine(routine.id)

    assert new_routine == routine

    # Try with an invalid user id
    new_routine_data_invalid_user = {
        "uploaded_by": 3,
        "exercises": new_routine_exercises_data,
    }

    response = client.post("/routines/", json=new_routine_data_invalid_user)

    assert response.status_code == 400
    assert response.json() == {"Error": "Could not upload routine."}


def test_patch_routine(data: dict):
    # Try patching an unexisting routine
    response = client.patch("/routines/3", json={})

    assert response.status_code == 400
    assert response.json() == {"Error": "Routine with id 3 not found."}

    # Try a valid one
    routine = data["routineNeckLegsAbdomen"]

    data_to_edit = {"description": "New Description", "dislikes": 10}

    response = client.patch("/routines/{0}".format(routine.id), json=data_to_edit)

    # edited_routine = RoutineModel(
    #     description='New Description', dislikes=10, **routine.json())

    edited_routine = routine.copy(update=data_to_edit)

    assert response.status_code == 200
    assert response.json() == edited_routine

    modified_routine = db.get_routine(routine.id)

    assert modified_routine == edited_routine


def test_get_user(data: dict):
    user = data["userJohn"]

    # Test with an existing one
    response = client.get("/users/{0}".format(user.id))

    assert response.status_code == 200
    assert response.json() == user

    # Test with a non-existing one
    response = client.get("/users/3")

    assert response.status_code == 404
    assert response.json() == {"Error": "User with id 3 not found."}


def test_create_user(data: dict):
    new_user_data = {
        "name": "Mike",
        "last_name": "Johnson",
        "fitness_profile_model": {
            "age": 20,
            "health_state": "Healthy",
            "height": 180,
            "physical_activity": "Active",
            "weight": 85,
        },
        "rating": 10,
    }

    response = client.post("/users/", json=new_user_data)

    new_user = UserModel(id=2, **new_user_data)

    assert response.status_code == 201
    assert response.json() == new_user

    db_user = db.get_user(new_user.id)

    assert db_user == new_user

    # Try with incorrect data
    bad_user_data = {
        "name": "Mike",
        "last_name": "Johnson",
        "fitness_profile_model": {
            "age": 20,
            "health_state": "Invalid",
            "height": 180,
            "physical_activity": "Active",
            "weight": 85,
        },
        "rating": 10,
    }

    response = client.post("/users/", json=bad_user_data)

    assert response.status_code == 422


def test_edit_user_fitness_profile(data: dict):
    user = data["userJane"]

    new_fitness_profile = {
        "age": 32,
        "health_state": "Healthy",
    }

    response = client.patch(
        "/users/{0}/fitness-profile".format(user.id), json=new_fitness_profile
    )

    updated_fitness_profile = user.fitness_profile_model.copy(
        update=new_fitness_profile
    )

    updated_user = user.copy(update={"fitness_profile_model": updated_fitness_profile})

    assert response.status_code == 200
    assert response.json() == updated_user

    modified_user = db.get_user(user.id)

    assert modified_user == updated_user
