from enum import Enum


class HealthState(Enum):
    Ill = 1
    Limited = 2
    Normal = 3
    Healthy = 4
    Optimal = 5


class PhysicalActivity(Enum):
    Sedentary = 1
    SomewhatActive = 2
    Active = 3
    VeryActive = 4


class UserFitnessProfile():
    def __init__(self, age: int, health_state: HealthState, height: int, physical_activity: PhysicalActivity, weight: int):
        '''
        Initializes a new instance of UserFitnessProfile that handles the user's physical fitness information.

        ### Parameters
            age: user's age in years.
            health_state: the general health state of the user.
            physical_activity: how physically active the user is.
            height: user's height in centimeters.
        '''
        self.age = age
        self.health_state = health_state
        self.height = height
        self.physical_activity = physical_activity
        self.weight = weight


class User():
    def __init__(self, first_name: str, last_name:  str, user_fitness_profile: UserFitnessProfile, rating: int):
        self.first_name = first_name
        self.last_name = last_name
        self.user_fitness_profile = user_fitness_profile
        self.rating = rating