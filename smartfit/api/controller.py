from smartfit.api.models import RoutineModel, WorkoutTable
from typing import List


def get_recommended_routines(workout_table: WorkoutTable, routines: List[RoutineModel]):
    result_routines = []
    body_parts = workout_table.keys()

    for routine in routines:
        intersection = [
            body_part
            for body_part in body_parts
            if body_part in routine.workout_table.keys()
        ]
        if len(intersection) > 0:
            result_routines.append(routine)

    return result_routines
