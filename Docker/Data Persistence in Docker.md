---
tags:
  - docker
  - docker-presistence
---
### Persisting Data in Docker Containers Using Volumes

1. When a Docker container starts, it operates in an isolated environment, using the files and configuration provided by its image. Containers are ephemeral by nature, meaning any changes to files within the container (such as creating, modifying, or deleting them) are temporary. 
2. Once a container is deleted, these changes are lost. While this behavior can be beneficial for stateless applications, it poses a challenge when persistent data is required, such as for a database.
3. To address this, Docker offers **volumes**, which allow data to persist beyond the life of a container, ensuring it remains available even after a container is deleted.


## Container [[Volumes]]

1. **Volumes** are a mechanism in Docker that lets you persist data across container restarts and deletions. 
2. Volumes function like a symlink (shortcut) that links files inside a container to storage on the host machine.
3. This way, the container can read and write files to the volume as though they were stored inside the container, but the data remains safe even if the container is removed.

#### Creating a Volume

To create a volume in Docker, use the following command:
```bash
docker volume create log-data
```

This creates a volume called `log-data` that will persist even if a container that uses it is deleted.

#### Mounting a Volume in a Container

You can mount this volume in a container when starting it. For example:
```bash
docker run -d -p 80:80 -v log-data:/logs docker/welcome-to-docker
```

In this command:
- The `-v log-data:/logs` option mounts the `log-data` volume at the `/logs` directory inside the container.
- If the volume `log-data` doesn’t exist, Docker automatically creates it.

Any files that the container writes to the `/logs` directory will be stored in the `log-data` volume on the host machine, making them persistent. If the container is deleted and restarted with the same volume, the files in the volume will remain available.

### [[Sharing Volumes Between Containers]]

Multiple containers can share a volume, allowing them to access and modify the same data. This is useful in scenarios like:
- **Log aggregation:** Different containers writing logs to the same volume for centralized logging.
- **Data pipelines:** One container writes data while others process it.
- **Event-driven applications:** Containers sharing event data.

### Managing Docker Volumes

Volumes are separate from the container’s lifecycle and require management to avoid uncontrolled growth. Docker provides several commands for volume management:

- **List all volumes:**
  ```bash
  docker volume ls
  ```

- **Remove a volume:**
  ```bash
  docker volume rm <volume-name>
  ```
  This removes the volume, but only if it is not currently in use by any containers.

- **Prune (delete) unused volumes:**
  ```bash
  docker volume prune
  ```

### Example: Persisting Data in a PostgreSQL Container

#### Step 1: Start the PostgreSQL Container with a Volume

Run the following command to start a PostgreSQL container with a volume attached to persist database files:
```bash
docker run --name=db -e POSTGRES_PASSWORD=secret -d -v postgres_data:/var/lib/postgresql/data postgres
```
- `POSTGRES_PASSWORD=secret`: Sets the password for the PostgreSQL user.
- `-v postgres_data:/var/lib/postgresql/data`: Attaches the `postgres_data` volume to the container’s `/var/lib/postgresql/data` directory.

This ensures that any data written by PostgreSQL to this directory is saved in the `postgres_data` volume, making it persistent.

#### Step 2: Connect to PostgreSQL

You can connect to the running PostgreSQL container with:
```bash
docker exec -ti db psql -U postgres
```

Once inside the PostgreSQL command line, create a table and insert data:
```sql
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    description VARCHAR(100)
);
INSERT INTO tasks (description) VALUES ('Finish work'), ('Have fun');
```

Verify the data is saved:
```sql
SELECT * FROM tasks;
```
This should return:
```
 id | description
----+-------------
  1 | Finish work
  2 | Have fun
(2 rows)
```

#### Step 3: Stop and Remove the Container

Stop and remove the container, which deletes the container but not the data stored in the volume:
```bash
docker stop db
docker rm db
```

#### Step 4: Start a New Container with the Same Volume

Now, run a new container using the same `postgres_data` volume:
```bash
docker run --name=new-db -d -v postgres_data:/var/lib/postgresql/data postgres
```

Because the data was persisted in the volume, you can verify that it’s still present:
```bash
docker exec -ti new-db psql -U postgres -c "SELECT * FROM tasks"
```

### Viewing and Managing Volume Contents

The **Docker Dashboard** provides a visual interface for managing volumes:
- Navigate to the "Volumes" section to see the `postgres_data` volume.
- You can explore the contents of the volume, export, import, or delete files directly.

### Removing Volumes

To remove volumes, ensure they are not attached to any running containers. You can remove volumes using the following methods:
1. **From Docker Dashboard:** Select the volume and click the delete option.
2. **From the command line:**
   - Stop and remove the container if it's using the volume:
     ```bash
     docker rm -f new-db
     ```
   - Remove the volume:
     ```bash
     docker volume rm postgres_data
     ```
   - Prune all unused volumes:
     ```bash
     docker volume prune
     ```

