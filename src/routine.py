from user import *


class Comment():
    def __init__(self, text: str, user: User):
        self.text = text
        self.user = user


class Routine():
    def __init__(self, description: str, uploaded_by: User, likes: int, comments: list, tags: list, exercises: list):
        '''
        Initializes a new instance of Routine that contains the [Exercise]s to do. Also contains the total workout table
        based on the individual workout tables from the exercises.

        ### Parameters
            description: short description about the routine.
            uploaded_by: [User] that uploaded the routine.
            likes: likes the routines has had so far. Must be an [int].
            comments: comments and feedbacks from users. Must be a [list] of [Comment]s.
            tags: tags related to the routine. Must be a [list] of [str]s.
            exercises: exercises that comprehen the routines. Must be a [list] of [Exercise]s.
        '''
        self.description = description
        self.uploaded_by = uploaded_by
        self.likes = likes
        self.comments = comments
        self.tags = tags
        self.exercises = exercises

        self.workout_table = self._build_workout_table()

    def _build_workout_table(self) -> map:
        pass