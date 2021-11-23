# Tests Container

In order to isolate the test environment in a controlled and secure way, Docker has been selected as the technology to use.

For this, a [Dockerfile](../Dockerfile) was created to handle the build of the docker image. First a base container was selected and then the necesary dependencies and files were added to the new container in order to set it ready for running the tests.

For optimizing the container size and creating as small number of layers as possible, all the RUN commands were grouped inside a single one, avoiding the creation of a layer for each individual command.

## Base container selection criteria

For the selection of the base container, it was decided to use `python:alpine3.14` since it comes with python3 already installed and another basic libraries (like pip) that the project needs in order to install dependencies for running the tests, while maintaining an extremely low size since it uses `Alpine`, an ultra light Linux distribution specifically used for keeping low-sized docker images. This distribution is known for having incompatibilities with some python libraries since it uses `musl libc` instead of the standard `glibc` (and family), but with the current requirements of the project, this is not an issue just yet and it is possible that it will never be, al least not for testing. If it comes to it, the base image will be changed. The version 3.14 was selected since was the latest stable version.

Since the programming language used in the project is Python, the main interest when looking for base containers was those that contain Python already, but using an "empty" light distribution from scratch was also analysed. Some of the following were considered:

- [python](https://hub.docker.com/layers/python/library/python/latest/images/sha256-33b969f0ae7eac496dccf1ae37b8f7d985dc2e6c35fe4b4f0263d4f8e7a3006c?context=explore) (official)
- [python:slim](https://hub.docker.com/layers/python/library/python/3.9-slim/images/sha256-dd5e1bc573f74cecbfda2fe05c7dac563927883250962858371aeaa6bfff7132?context=explore)
- [alpine](https://hub.docker.com/layers/alpine/library/alpine/latest/images/sha256-8595fe2e98735305ca7cbc68399d428d8bf1857daf13511db56a43e079ef960b?context=explore)
- [python:alpine3.14](https://hub.docker.com/layers/python/library/python/alpine3.14/images/sha256-d7d1220049363cfd777af4e0a311dead8376c533515915b24a88b6f43de17cc4?context=explore)

In the first case, it would be the ideal scenario. We would have the (almost) entire python environment to our disposal and not to worry about missing dependencies. The problem is that when the image was pulled and inspected, we saw its size was huge (~ 916.66 MB), and since we are just going to need `make`, `pip` and `pytest`, this size seems excessive.

In the second case, we would have a light version of `python`. When it was pulled and ispected we could see that the image was quite light (~122.18 MB), so we tought it would be appropiate to use it. The slim images contain only the minimum necessary libraries to run `python`, but this one still managed to get a little too big for our purposes, since 122 MB seems, again, too much.

When selecting alpine we were looking starting from scratch: install `make`, then `python` and `pip` and `pytest`. But after pulling the image and staring installing the dependencies into the container, it grew in size enough for us to decide to try another images that maybe came with these requirements and were a little bit lighter (by having less number of layers, for instance).

Then we found `python:alpine3.14`, having installed python (with pip included) over alpine, being extremelly light (~45.5 MB) and having the basic we need, even though it doesn't have `make` or `pytest`, but when installed it didn't almost grow in size. This image is also very well maintained by the community.

## Push docker container on changes

In order to keep the docker image up-to-date with the state of the code, it was convenient to automatize the process of building and pushing the image to a registry. In this case the registry selected was Docker Hub and the automatization was done through GitHub Actions, using [Build and push Docker images](https://github.com/marketplace/actions/build-and-push-docker-images).

For this process is necessary to log into Docker Hub, but for security reasons the credentials must not be places inside the workflow `.yml` file. Instead, the [GitHub actions secrets](https://github.com/marcos-toranzo/SmartFit/settings/secrets/actions) were used, where the secrets `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN` were created containing the username and password, respectively.

In this [workflow](https://github.com/marcos-toranzo/SmartFit/blob/main/.github/workflows/push-to-dockerhub.yml) gets specified first the branch on which we want to listen for changes. In this case is on the branch `main`, since this branch will contain the production code and should have been tested and cleaned previously to pushing. After we specified the branch, we need to write the steps to execute in order to build and push the image. First we add emulation support to build against more platforms without issues by setting up a QEMU virtual machine. Afterwards, we need to set up BuildX, the builder that is going to enable us to build multi-platform images. The next step is to login to DockerHub using the credentials stored in the secrets, and finally we need to build and push the image using the Dockerfile in the project.

## Push to an alternative registry

Another alternative for Docker Hub was GitHub Container Registry. This was selected based on the fact that its workflow is very similar to the one used with Docker Hub, and it is well integrated into the GitHub environment, providing comfortable ways to view it and manage it.

This process was also automatized using GitHub Actions. In this case, the documentation used was [Publishing and installing a package with GitHub Actions](https://docs.github.com/en/packages/managing-github-packages-using-github-actions-workflows/publishing-and-installing-a-package-with-github-actions), where the process is explained in detail. The `.yml` remained almost unmodified, except for the name, since it works for our purposes and uses the recomended version of every step.

In this case, the flow is the same in principle to the one described with Docker Hub, with some minor differences. In this case we define environment variables like the registry we are going to be pushing to (in this case the GitHub Container Registry, or ghcr.io) and the image name, grabbing it from the repository name. Then we need to login to the registry using our GitHub same credentials, with the actor being the user invoking the workflow, and `GITHUB_TOKEN` is a secret autogenerated by the action containing the password. After this, we just have to compile the image to get the necessary information like tags and label for the build and push process afterwards.

This container can be accessed later on under the section Packages in our repository page.
