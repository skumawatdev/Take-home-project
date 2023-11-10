# Docker:-Assignment-Answers

**1. What is docker and why do we need it?**
  
Docker is an open-source platform for containerization, allowing you to package applications and their dependencies into containers. 

**We need Docker for** 
  Consistency in development and production environments.
  Portability of applications.
  Resource efficiency.
  Scalability.
  Version control of container images.
  CI/CD integration.
  Isolation and security.
  
**2. Write a docker file for a** ***Quiz python application.***


![image](https://github.com/skumawatdev/take-home-project/assets/60931208/ace07b36-8a62-4cdd-b62c-789ba25f898c)


![image](https://github.com/skumawatdev/take-home-project/assets/60931208/22d4c594-323d-4a05-a469-2aaecf4e2e45)




**3. What is the docker lifecycle?**

The Docker lifecycle consists of several stages, including:

**Build:** Create a Docker image from a Dockerfile.
**Push:** Upload the image to a container registry (e.g., Docker Hub).
**Pull:** Download the image on another machine or environment.
**Run:** Create a Docker container from an image and execute the application.
**Stop:** Terminate a running container.
**Remove:** Delete a stopped container.
**Commit:** Create a new image from a container's changes.
**Tag:** Assign a name and optional tag to an image.

![image](https://github.com/skumawatdev/take-home-project/assets/60931208/44c58243-3372-4bac-8b8b-550ddfd51bae)


**4. What is the difference between an image and a container?**
   
**Image:** A blueprint or template for a container. It includes application code, dependencies, and configuration. Images are read-only.

**Container:** A running instance of an image. Containers have a writable layer and runtime environment. They can be started, stopped, and deleted.

**5. How to check docker container logs? Provide the command for the same**
    *To check Docker container logs, use the following command:**

```bash
        docker logs container-id/name
  ```

![docker logs](https://github.com/skumawatdev/take-home-project/assets/60931208/36e477d3-eeed-4c79-a500-ea4a0d77113b)




