from smartfit.entities.user import (
    HealthState,
    PhysicalActivity,
    User,
    UserFitnessProfile,
)
import pytest


@pytest.fixture
def user() -> User:
    return User(
        0,
        "First",
        "Last",
        UserFitnessProfile(20, HealthState.Healthy, 180, PhysicalActivity.Active, 80),
        100,
    )


def test_user_age(user: User):
    user.update_age(19)

    assert user.age == 19


def test_user_weight(user: User):
    user.update_weight(75)

    assert user.weight == 75


def test_user_height(user: User):
    user.update_height(175)

    assert user.height == 175


def test_user_health_state(user: User):
    user.update_health_state(HealthState.Ill)

    assert user.health_state == HealthState.Ill


def test_user_physical_activity(user: User):
    user.update_physical_activity(PhysicalActivity.SomewhatActive)

    assert user.physical_activity == PhysicalActivity.SomewhatActive


def test_user_rating(user: User):
    user.update_rating(90)

    assert user.rating == 90
