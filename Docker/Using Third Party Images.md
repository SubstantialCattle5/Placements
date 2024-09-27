---
tags:
  - docker
---
### Steps to Run and Manage a Containerized Database:

1. **Running a Local Containerized Database**:
   - Pull a database image from **Docker Hub** (e.g., MySQL).
   - Use the `docker run` command to start a database container, specifying environment variables like root password and database name.

   ```bash
   docker run --name my-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -e MYSQL_DATABASE=mydb -d mysql:latest
   ```

2. **Accessing the Shell of a Containerized Database**:
   - Use `docker exec` to interact with the running container.
   
   ```bash
   docker exec -it my-mysql bash
   ```
   - Once inside, manage the database via MySQL commands.

   ```bash
   mysql -u root -p
   ```

3. **Connecting to a Containerized Database from the Host**:
   - Expose the MySQL port (default: 3306) to allow host-machine connections.

   ```bash
   docker run -p 3307:3306 --name my-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -e MYSQL_DATABASE=mydb -d mysql:latest
   ```

4. **Connecting to a Containerized Database from Another Container**:
   - Create a Docker network, and then run the database container and other dependent containers (like **phpMyAdmin**) on the same network for easy inter-container communication.

   ```bash
   docker network create my-network
   docker run --name my-mysql --network my-network -d mysql:latest
   docker run --name my-phpmyadmin --network my-network -p 8080:80 -e PMA_HOST=my-mysql phpmyadmin
   ```

5. **Persisting Data Using Docker Volumes**:
   - Attach a volume to persist database data, ensuring the data remains intact across container restarts and removals.

   ```bash
   docker run --name my-mysql -v my-db-volume:/var/lib/mysql -d mysql:latest
   ```

6. **Building a Customized Database Image**:
   - Use a `Dockerfile` to build custom images with initialization scripts or specific configurations.

   ```Dockerfile
   FROM mysql:latest
   ENV MYSQL_DATABASE mydb
   COPY ./scripts/ /docker-entrypoint-initdb.d/
   ```

7. **Running a Database with Docker Compose**:
   - Use **Docker Compose** to manage multi-container applications, such as a MySQL container with **phpMyAdmin**.
   
   ```yaml
   services:
     db:
       image: mysql:latest
       environment:
         MYSQL_ROOT_PASSWORD: my-secret-pw
         MYSQL_DATABASE: mydb
       ports:
         - 3307:3306
       volumes:
         - my-db-volume:/var/lib/mysql
     phpmyadmin:
       image: phpmyadmin/phpmyadmin:latest
       environment:
         PMA_HOST: db
         PMA_PORT: 3306
         MYSQL_ROOT_PASSWORD: my-secret-pw
       ports:
         - 8080:80
   volumes:
     my-db-volume:
   ```

   Run the containers with:
   
   ```bash
   docker compose up
   ```
