from enum import Enum


class BodyPart(Enum):
    Neck = 1
    Shoulders = 2
    Biceps = 3
    Triceps = 4
    Forearms = 5
    Back = 6
    LowerBack = 7
    Abdomen = 8
    Hip = 9
    Quadriceps = 10
    Calfs = 11
    Legs = 12
    Ankles = 13


class ExerciseStep():
    def __init__(self, step_image_url: str, duration_in_seconds: int):
        '''
        Initializes a new instance of ExerciseStep that defines the step to do and the time it
        needs to be done in.

        ### Parameters
            step_image_url: ULR to the image showing the physical action.
            duration_in_seconds: seconds the step should take to complete.
        '''
        self._step_image_url = step_image_url
        self._duration_in_seconds = duration_in_seconds

    @property
    def step_image_url(self) -> str:
        return self._step_image_url

    @property
    def duration_in_seconds(self) -> int:
        return self._duration_in_seconds


class Exercise():
    def __init__(self, description: str, workout_table: map, steps: list):
        '''
        Initializes a new instance of Exercise that defines the series of steps to follow,
        as well as the workout load table indicating the parts of the body that get exercised.

        ### Parameters
            description: short description about the exercise.
            workout_table: the workout load table. The keys must be [BodyPart]s, and the values must be [int] from 0 to 100, both included.
            steps: steps to follow to complete the exercise. Must be a [list] of [ExerciseStep].
        '''
        self._description = description
        self._workout_table = workout_table
        self._steps = steps

    @property
    def description(self) -> str:
        return self._description

    @property
    def workout_table(self) -> map:
        return self._workout_table

    @property
    def steps(self) -> list:
        return self._steps
