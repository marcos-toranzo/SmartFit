from enum import Enum


class HealthState(str, Enum):
    Ill = 'Ill'
    Limited = 'Limited'
    Normal = 'Normal'
    Healthy = 'Healthy'
    Optimal = 'Optimal'


class PhysicalActivity(str, Enum):
    Sedentary = 'Sedentary'
    SomewhatActive = 'SomewhatActive'
    Active = 'Active'
    VeryActive = 'VeryActive'


class UserFitnessProfile():
    def __init__(self, age: int, health_state: HealthState, height: int, physical_activity: PhysicalActivity, weight: int):
        '''
        Initializes a new instance of UserFitnessProfile that handles the user's physical fitness information.

        ### Parameters
            age: user's age in years.
            health_state: the general health state of the user.
            physical_activity: how physically active the user is.
            height: user's height in centimeters.
            weight: user's weight in kilograms.
        '''
        self.age = age
        self.health_state = health_state
        self.height = height
        self.physical_activity = physical_activity
        self.weight = weight


class User():
    def __init__(self, first_name: str, last_name:  str, user_fitness_profile: UserFitnessProfile, rating: int):
        self._first_name = first_name
        self._last_name = last_name
        self._user_fitness_profile = user_fitness_profile
        self._rating = rating

    @property
    def first_name(self) -> str:
        return self._first_name

    @property
    def last_name(self) -> str:
        return self._last_name

    @property
    def user_fitness_profile(self) -> UserFitnessProfile:
        return self._user_fitness_profile

    @property
    def rating(self) -> int:
        return self._rating

    @property
    def age(self) -> int:
        return self.user_fitness_profile.age

    @property
    def weight(self) -> int:
        return self.user_fitness_profile.weight

    @property
    def height(self) -> int:
        return self.user_fitness_profile.height

    @property
    def health_state(self) -> HealthState:
        return self.user_fitness_profile.health_state

    @property
    def physical_activity(self) -> PhysicalActivity:
        return self.user_fitness_profile.physical_activity

    def update_age(self, age: int):
        profile = self._user_fitness_profile

        self._user_fitness_profile = UserFitnessProfile(
            age, profile.health_state, profile.height, profile.physical_activity, profile.weight)

    def update_health_state(self, health_state: HealthState):
        profile = self._user_fitness_profile

        self._user_fitness_profile = UserFitnessProfile(
            profile.age, health_state, profile.height, profile.physical_activity, profile.weight)

    def update_height(self, height: int):
        profile = self._user_fitness_profile

        self._user_fitness_profile = UserFitnessProfile(
            profile.age, profile.health_state, height, profile.physical_activity, profile.weight)

    def update_physical_activity(self, physical_activity: PhysicalActivity):
        profile = self._user_fitness_profile

        self._user_fitness_profile = UserFitnessProfile(
            profile.age, profile.health_state, profile.height, physical_activity, profile.weight)

    def update_weight(self, weight: int):
        profile = self._user_fitness_profile

        self._user_fitness_profile = UserFitnessProfile(
            profile.age, profile.health_state, profile.height, profile.physical_activity, weight)

    def update_rating(self, rating: int):
        self._rating = rating
