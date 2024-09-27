---
tags:
  - docker
---
Docker Engine is an open source containerization technology for building and containerizing your applications. Docker Engine acts as a client-server application with:

- A server with a long-running daemon process [`dockerd`](https://docs.docker.com/reference/cli/dockerd).
- APIs which specify interfaces that programs can use to talk to and instruct the Docker daemon.
- A command line interface (CLI) client [`docker`](https://docs.docker.com/reference/cli/docker/).

The CLI uses [Docker APIs](https://docs.docker.com/reference/api/engine/) to control or interact with the Docker daemon through scripting or direct CLI commands. Many other Docker applications use the underlying API and CLI. The daemon creates and manages Docker objects, such as images, containers, networks, and volumes.