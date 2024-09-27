---
tags:
  - docker
---
1. A Dockerfile is a text document that contains a list of instructions used by the Docker engine to build an image. 
2. Each instruction in the Dockerfile adds a new layer to the image. 
3. Docker will build the image based on these instructions, and then you can run containers from the image.

| Instruction  | Description                                                       |
|--------------|-------------------------------------------------------------------|
| ADD          | Add local or remote files and directories.                        |
| ARG          | Use build-time variables.                                         |
| CMD          | Specify default commands.                                         |
| COPY         | Copy files and directories.                                       |
| ENTRYPOINT   | Specify default executable.                                       |
| ENV          | Set environment variables.                                        |
| EXPOSE       | Describe which ports your application is listening on.           |
| FROM         | Create a new build stage from a base image.                      |
| HEALTHCHECK  | Check a container's health on startup.                           |
| LABEL        | Add metadata to an image.                                        |
| MAINTAINER   | Specify the author of an image.                                   |
| ONBUILD      | Specify instructions for when the image is used in a build.      |
| RUN          | Execute build commands.                                           |
| SHELL        | Set the default shell of an image.                               |
| STOPSIGNAL   | Specify the system call signal for exiting a container.          |
| USER         | Set user and group ID.                                           |
| VOLUME       | Create volume mounts.                                            |
| WORKDIR      | Change working directory.                                        |

### Format 

```bash
INSTRUCTION argument
```
The instruction is not case-sensitive. However, convention is for them to be UPPERCASE to distinguish them from arguments more easily.


