# Testing framework

In this project, the language used was `Python3`, so we focused on tools for this one in specific. We chose TDD over BDD, mostly in the early stages of the development. Even though BDD is most of the time easier to understand, describe and develop, TDD ensures us a safer code and a stronger foundation for our code in order to reduce possible issues and bugs, writing the test along with the code in order to maintain the integrity, while we move on to other functionalities of our project trusting that the rest is sound.

Python, as well as many other languages, comes packed with some features for testing code, like built-in assertions through the keyword assert or using libraries like `unittest`, which also includes its own framework. In order to choose the tool to use for testing, we considered the next options:

## unittest

### Pros:

- Comes included right out-of-the-box since Python 2.1, so no external library or dependency needs to be installed or managed.
- Fast and simple way to write the tests.
- Fast and good reporting of results.

### Cons:

- Needs a lot of boilerplate code.
- It can get a little unclear understanding the code since it support abstraction.
- Its syntax does not follow the snake_case used in Python, instead uses camelCase.

## nose2:

### Pros:

- Can use the same tests written for `unittest`, and being this one built-in, it gives it leverage.
- It's basically written on top of `unittest`, which gives the developer confidence and familiarity but also adds support for test execution, test discovery, decorators, fixtures, and parameterization.
- Can identify tests automatically if you follow the rules.

### Cons:

- Lacks feedback and support from the community, which includes documentation.

## Pytest

### Pros:

- Tests are written really simple and fast.
- Eliminates a lot of boilerplate code.
- Supports parallel execution.
- Large community and great feedback.
- Supports fixtures, giving the possibility to reuse code and create and manage context better in tests.
- Highly extensible with plugins.

### Cons:

- Uses unique routines, making compatibility difficult or impossible.

Having analyzed these frameworks, we got to the conclusion that the best would be `Pytest`. In order to create tests for the first 2, we would have to import a specific class `TestCase` from the `unittest` library, create a class that inherits this class, and then write the tests inside this class definition, making us use their own assertion methods written in camelCase like `assertEqual`, that belong to the own TestCase class. This creates an overhead in the development and a lot of boilerplate code, besides the limitations we can overcome with other frameworks like fixtures. In the case of `nose2` we find the same issues but we can use a lot of plugins to increment the functionality of our tests. The problem here comes when we find a lack of support from the community, mostly in the documentation.

Here is where `Pytest` comes to play. In this case, we find that in order to write a test we just have to write a function that is the one that is going to do the assertions, these ones made using the assert keyword native of the language, making it cleaner and more familiar. We can also use fixtures to reuse code, like specific data we want to modify during the test. On top of everything, this framework also allows us to just run `pytest` in the root of the directory and automatically will find functions that begging with `test_` or end with `_test.py`, inside files that end in `_test.py` that make assertions and call them as part of the test run, but this can be extensively customized using configuration files. Even though it needs to be installed as an external dependency, it is extremely easy to install using pip. For these reasons we got to the decision of using `Pytest` as the framework for testing out project.
