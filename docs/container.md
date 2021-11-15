# Tests Container

In order to isolate the test environment in a controlled and secure way, Docker has been selected as the technology to use.

For this, a [Dockerfile](../Dockerfile) was created to handle the build of the docker image. First a base container was selected and then the necesary dependencies and files were added to the new container in order to set it ready for running the tests.

For optimizing the container size and creating as small number of layers as possible, all the RUN commands were grouped inside a single one, avoiding the creation of a layer for each individual command.

## Base container selection criteria

For the selection of the base container, it was decided to use `python:alpine3.14` since it comes with python3 already installed and another basic libraries (like pip) that the project needs in order to install dependencies for running the tests, while maintaining an extremely low size since it uses `Alpine`, an ultra light Linux distribution specifically used for keeping low-sized docker images. This distribution is known for having incompatibilities with some python libraries since it uses `musl libc` instead of the standard `glibc` (and family), but with the current requirements of the project, this is not an issue just yet and it is possible that it will never be, al least not for testing. If it comes to it, the base image will be changed.

Since the programming language used in the project is Python, the main interest when looking for base containers was those that contain Python already, but using an "empty" light distribution from scratch was also analysed. Some of the following were considered:

- [python](https://hub.docker.com/layers/python/library/python/latest/images/sha256-33b969f0ae7eac496dccf1ae37b8f7d985dc2e6c35fe4b4f0263d4f8e7a3006c?context=explore) (official)
- [python:slim](https://hub.docker.com/layers/python/library/python/3.9-slim/images/sha256-dd5e1bc573f74cecbfda2fe05c7dac563927883250962858371aeaa6bfff7132?context=explore)
- [alpine](https://hub.docker.com/layers/alpine/library/alpine/latest/images/sha256-8595fe2e98735305ca7cbc68399d428d8bf1857daf13511db56a43e079ef960b?context=explore)
- [python:alpine3.14](https://hub.docker.com/layers/python/library/python/alpine3.14/images/sha256-d7d1220049363cfd777af4e0a311dead8376c533515915b24a88b6f43de17cc4?context=explore)

In the first case, it would be the ideal scenario. We would have the (almost) entire python environment to our disposal and not to worry about missing dependencies. The problems comes when we inspect this image and we see it size is huge (~ 916.66 MB), and since we are just going to need `make`, `pip` and `pytest`, this size seems excessive.

In the second case, we would have a light version of `python` and quit light (~122.18 MB). This image contains only the minimum necessary libraries to run `python` but still managed to get a little to big for our purposes, since 122 MB seems again too much.

When selecting alpine we were looking starting from scratch: install `make`, then `python` and `pip` and `pytest`. But this grew in size enough for us to decide to try another images that maybe came with these requirements and were a little bit lighter (by having less number of layers, for instance).

Then we found `python:alpine3.14`, having installed python (with pip included) over alpine, being extremelly light (~45.5 MB) and having the basic we need, even though it doesn't have `make` or `pytest`, but when installed it didn't almost grow in size. This image is also very well maintained by the community.
