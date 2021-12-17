[![Build Status](https://app.travis-ci.com/marcos-toranzo/SmartFit.svg?branch=main)](https://app.travis-ci.com/marcos-toranzo/SmartFit)

# SmartFit

This project tries to facilitate the users the way they stay fit by balancing the amount and type of exercise done during the whole day, not just during the short sessions dedicated specifically to the physical excercise.

Project for the Cloud Computing course of the Computer Engineering Master at University of Granada.

# Getting started

## Requirements

- `make`
- `python3`
- `pip3`

## Tasks

The tasks related to the project are implemented in the [Makefile](https://github.com/marcos-toranzo/SmartFit/blob/main/Makefile) in directory root. Here you can run:

- **test**: will run every test in the [tests](https://github.com/marcos-toranzo/SmartFit/tree/main/tests) folder. Uses `pytest`.
- **check**: checks for compilation and sintactic errors.
- **install**: install dependencies of the project.
- **container-test**: run tests in docker container.
- **run-server**: run the API server.

You can read more about the choice of [task manager](docs/task_manager.md).

## Dotenv

The project uses the configuration set in the `.env` file in the root directory. Right now, only the `HOST` and `PORT` configuarion for the API server is used. This file is ignored by git since it can contain sensitive informatios like credentials and secret keys we don't want to make public.

In case of not having specified `HOST`, the default value will be `127.0.0.1`. In the case of the `PORT` it will be `8000`.

# Documentation

You can read a [more detailed description](docs/description.md) of the problem been solved.

You can consult the [business logic](docs/business_logic.md) for the project.

You can read all about the [user journeys](docs/user_journeys.md), where possible flows and situations are described, as well as the user roles.

You can check the [milestones](docs/milestones.md) for the project, where each one defines a MVP to achieve when finished.

You can read the [user stories](docs/user_stories.md) that define the functioning of the app.

You can learn about the [testing libraries and framework](docs/testing_framework.md) used in the project, and why we chose them.

In order to run the tests in a controlled and secure environment, [docker containers](docs/container.md) were used.

Information about the [continuous integration](docs/ci.md) implemented in the project.

You can read about the [API services](docs/api.md) implemented, the process of testing them and how they comply with the user stories.

# Initial configuration

Go [here](docs/initial_configuration.md) to see the steps taken for the initial configuration.
