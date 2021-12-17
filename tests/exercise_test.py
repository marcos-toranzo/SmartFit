from smartfit.entities.exercise import BodyPart, Exercise, ExerciseStep
import pytest


@pytest.fixture
def exercise():
    description = "My exercise"
    workout_table = {BodyPart.Abdomen: 10, BodyPart.Neck: 20}
    steps = [ExerciseStep("", 2)]

    return Exercise(description, workout_table, steps)


def test_exercise_description(exercise: Exercise):
    assert exercise.description == "My exercise"


def test_exercise_workout_table(exercise: Exercise):
    workout_table = {BodyPart.Abdomen: 10, BodyPart.Neck: 20}

    assert exercise.workout_table == workout_table


def test_exercise_steps(exercise: Exercise):
    assert len(exercise.steps) == 1
