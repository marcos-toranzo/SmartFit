from smartfit.entities.exercise import BodyPart, Exercise, ExerciseStep
from smartfit.entities.user import HealthState, PhysicalActivity, User, UserFitnessProfile
from smartfit.entities.routine import Comment, Routine
import pytest


@pytest.fixture
def routine():
    fitness_profile = UserFitnessProfile(
        20,
        HealthState.Healthy,
        180,
        PhysicalActivity.Active,
        80
    )

    user = User('First', 'Last', fitness_profile, 100)

    user_comment_1 = User('First1', 'Last1', UserFitnessProfile(
        20, HealthState.Healthy, 180, PhysicalActivity.Active, weight=80), 100)

    user_comment_2 = User('First2', 'Last2', UserFitnessProfile(
        20, HealthState.Healthy, 180, PhysicalActivity.Active, weight=80), 100)

    comments = [
        Comment('Comment 1', user_comment_1),
        Comment('Comment 2', user_comment_2)
    ]

    tags = [
        'Tag 1',
        'Tag 2',
        'Tag 3'
    ]

    exercises = [
        Exercise('Exercise 1', {BodyPart.Abdomen: 15,
                 BodyPart.Back: 30}, [ExerciseStep('', 2)]),
        Exercise('Exercise 2', {BodyPart.Abdomen: 10,
                 BodyPart.Neck: 20}, [ExerciseStep('', 2), ExerciseStep('', 2)])
    ]

    return Routine('Routine', user, 100, 20, comments, tags, exercises)


def test_routine_like(routine: Routine):
    previous_likes = routine.likes

    routine.like()

    assert routine.likes == previous_likes + 1


def test_routine_dislike(routine: Routine):
    previous_dislikes = routine.dislikes

    routine.dislike()

    assert routine.dislikes == previous_dislikes + 1


def test_routine_unlike(routine: Routine):
    previous_likes = routine.likes

    routine.like()

    routine.unlike()

    assert routine.likes == previous_likes


def test_routine_undislike(routine: Routine):
    previous_dislikes = routine.dislikes

    routine.dislike()

    routine.undislike()

    assert routine.dislikes == previous_dislikes


def test_add_comment_to_routine(routine: Routine):
    comments_length = len(routine.comments)

    user = User('F', 'L', UserFitnessProfile(
        21,
        HealthState.Limited,
        181,
        PhysicalActivity.Sedentary,
        81
    ), 200)

    new_comment = Comment('New Comment', user)

    routine.add_comment(new_comment)

    assert comments_length == len(routine.comments) - 1

    last_comment = routine.comments[-1]

    assert new_comment.text == last_comment.text
    assert new_comment.user == last_comment.user


def test_total_table(routine: Routine):
    total_table = {
        BodyPart.Abdomen: 15,
        BodyPart.Back: 30,
        BodyPart.Neck: 20
    }

    assert routine.workout_table == total_table
