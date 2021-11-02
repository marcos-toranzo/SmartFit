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
        self.description = description
        self.uploaded_by = uploaded_by
        self.likes = likes
        self.dislikes = dislikes
        self.comments = comments
        self.tags = tags
        self.exercises = exercises

        self.workout_table = self._build_workout_table()

    def _build_workout_table(self) -> map:
        '''
        Calculates the general workout table. Takes the maximum of each body part.
        '''
        total_workout_table = {}

        tables = [exercise.workout_table for exercise in self.exercises]

        for table in tables:
            for body_part, workout in table.items():
                previous_value = 0 if body_part not in total_workout_table else total_workout_table[
                    body_part]
                total_workout_table[body_part] = max(previous_value, workout)

        return total_workout_table

    def add_comment(self, comment: Comment):
        self.comments.append(comment)

    def like(self):
        self.likes += 1

    def dislike(self):
        self.dislikes += 1

    def unlike(self):
        self.likes = max(0, self.likes - 1)

    def undislike(self):
        self.dislikes = max(0, self.dislikes - 1)
