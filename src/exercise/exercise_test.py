from exercise import BodyPart, Exercise, ExerciseStep


def test_exercise_constructor():
    description = 'My exercise'
    workout_table = {BodyPart.Abdomen: 10, BodyPart.Neck: 20}
    steps = [ExerciseStep()]

    exercise = Exercise(description, workout_table, steps)

    assert exercise.description == description
    assert exercise.workout_table[BodyPart.Abdomen] == workout_table[BodyPart.Abdomen]
    assert exercise.workout_table[BodyPart.Neck] == workout_table[BodyPart.Neck]
    assert len(exercise.steps) == 1
