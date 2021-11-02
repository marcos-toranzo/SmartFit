from src.entities.user import User


class Comment():
    def __init__(self, text: str, user: User):
        self.text = text
        self.user = user


class Routine():
    def __init__(self, description: str, uploaded_by: User, likes: int, dislikes: int, comments: list, tags: list, exercises: list):
        '''
        Initializes a new instance of Routine that contains the [Exercise]s to do. Also contains the total workout table
        based on the individual workout tables from the exercises.

        ### Parameters
            description: short description about the routine.
            uploaded_by: [User] that uploaded the routine.
            likes: likes the routines has had so far. Must be an [int].
            dislikes: dislikes the routines has had so far. Must be an [int].
            comments: comments and feedbacks from users. Must be a [list] of [Comment]s.
            tags: tags related to the routine. Must be a [list] of [str]s.
            exercises: exercises that comprehen the routines. Must be a [list] of [Exercise]s.
        '''
        self._description = description
        self._uploaded_by = uploaded_by
        self._likes = likes
        self._dislikes = dislikes
        self._comments = comments
        self._tags = tags
        self._exercises = exercises

        self._workout_table = self._build_workout_table()

    @property
    def description(self) -> str:
        return self._description

    @property
    def uploaded_by(self) -> User:
        return self._uploaded_by

    @property
    def likes(self) -> int:
        return self._likes

    @property
    def dislikes(self) -> int:
        return self._dislikes

    @property
    def comments(self) -> list:
        return self._comments

    @property
    def tags(self) -> list:
        return self._tags

    @property
    def exercises(self) -> list:
        return self._exercises

    @property
    def workout_table(self) -> list:
        return self._workout_table

    def _build_workout_table(self) -> map:
        '''
        Calculates the general workout table. Takes the maximum of each body part.
        '''
        total_workout_table = {}

        tables = [exercise.workout_table for exercise in self._exercises]

        for table in tables:
            for body_part, workout in table.items():
                previous_value = 0 if body_part not in total_workout_table else total_workout_table[
                    body_part]
                total_workout_table[body_part] = max(previous_value, workout)

        return total_workout_table

    def add_comment(self, comment: Comment):
        self._comments.append(comment)

    def like(self):
        self._likes += 1

    def dislike(self):
        self._dislikes += 1

    def unlike(self):
        self._likes = max(0, self._likes - 1)

    def undislike(self):
        self._dislikes = max(0, self._dislikes - 1)
