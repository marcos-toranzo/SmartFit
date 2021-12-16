
from pydantic import BaseModel
from typing import Optional, List, Mapping, NewType

from smartfit.entities.user import HealthState, PhysicalActivity

WorkoutTable = Mapping[str, int]
UserId = NewType('UserId', int)
RoutineId = NewType('RoutineId', int)


class FitnessProfileModel(BaseModel):
    age: int
    health_state: Optional[HealthState] = HealthState.Normal
    height: Optional[int] = 170
    physical_activity: Optional[PhysicalActivity] = PhysicalActivity.SomewhatActive
    weight: Optional[int] = 70


class UserModel(BaseModel):
    id: UserId
    name: str
    last_name: str
    fitness_profile_model: FitnessProfileModel
    rating: int


class UserModelForCreation(BaseModel):
    name: str
    last_name: str
    fitness_profile_model: FitnessProfileModel
    rating: int


class ExerciseStepModel(BaseModel):
    step_image_url: str
    duration_in_seconds: Optional[int] = 20


class ExerciseModel(BaseModel):
    description: Optional[str] = ''
    workout_table: Optional[WorkoutTable] = {}
    steps: List[ExerciseStepModel]


class RoutineModel(BaseModel):
    id: RoutineId
    description: Optional[str] = ''
    uploaded_by: int
    likes: Optional[int] = 0
    dislikes: Optional[int] = 0
    comments: Optional[List[str]] = []
    tags: Optional[List[str]] = []
    exercises: List[ExerciseModel]
    workout_table: Optional[WorkoutTable] = {}


class RoutineModelForCreation(BaseModel):
    description: Optional[str] = ''
    uploaded_by: int
    likes: Optional[int] = 0
    dislikes: Optional[int] = 0
    comments: Optional[List[str]] = []
    tags: Optional[List[str]] = []
    exercises: List[ExerciseModel]
