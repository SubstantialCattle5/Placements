---
tags:
  - docker
---
Container images are executable packages that include everything required to run an application: code, runtime, system tools, libraries, and settings. By building custom images, you can deploy applications seamlessly with all their dependencies on any Docker-supported platform. 

Docker uses a tool called `Docker buildx build` , to create images. 
## [[Dockerfile]]

1. The key component in building a container image is the `Dockerfile`. 
2. It is essentially a script containing instructions on how to assemble a Docker image. 
3. Each instruction in the Dockerfile creates a new layer in the image, making it easier to track changes and minimize the image size. 


