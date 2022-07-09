# Pushing-to-Docker-Hub
How to push your repo in docker hub

1. Creating repositories
  - To create a repository, sign into Docker Hub, click on Repositories then Create Repository:
  ![image](https://user-images.githubusercontent.com/33689324/178095567-8b9407a0-13ee-44ee-a665-65aac9a8cb65.png)
  
2. First tag the repository with the one you created on dockerhub (empty one)
  ```sh 
  $ docker tag hello-world:1.0 vinayakz/devopsjuly22:v1
  ```
3. Now login to docker hub using command  
  ```sh
  $ docker login
  Login with your Docker ID to push and pull images from Docker Hub. If you don't have a Docker ID, head over to https://hub.docker.com to create one.
  Username: DOCKER ID 
  password: **********
  ```
4. Enter the credentials and once succeeded run the following command:   
  ```sh
  $ docker push vinayakz/devopsjuly22:v1
  ```
5. Now check the docker hub to confirm if it reflects it.   
