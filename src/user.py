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

    def update_age(self, age: int):
        profile = self.user_fitness_profile

        self.user_fitness_profile = UserFitnessProfile(
            age, profile.health_state, profile.height, profile.physical_activity, profile.weight)

    def update_health_state(self, health_state: HealthState):
        profile = self.user_fitness_profile

        self.user_fitness_profile = UserFitnessProfile(
            profile.age, health_state, profile.height, profile.physical_activity, profile.weight)

    def update_height(self, height: int):
        profile = self.user_fitness_profile

        self.user_fitness_profile = UserFitnessProfile(
            profile.age, profile.health_state, height, profile.physical_activity, profile.weight)

    def update_physical_activity(self, physical_activity: PhysicalActivity):
        profile = self.user_fitness_profile

        self.user_fitness_profile = UserFitnessProfile(
            profile.age, profile.health_state, profile.height, physical_activity, profile.weight)

    def update_weight(self, weight: int):
        profile = self.user_fitness_profile

        self.user_fitness_profile = UserFitnessProfile(
            profile.age, profile.health_state, profile.height, profile.physical_activity, weight)

    def update_rating(self, rating: int):
        self.rating = rating
