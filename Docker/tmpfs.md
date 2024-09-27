---
tags:
  - docker
  - operatingsystem
---

1. In Docker, **tmpfs mounts** are a type of mount that allows you to store temporary files in the container's memory (RAM) rather than on disk. 
2. Unlike volumes or bind mounts, which persist data on the host system, `tmpfs` mounts are **ephemeral**. 
3. This means the data stored in a `tmpfs` mount is lost when the container stops, as it is not persisted on the host or in the container's writable layer.

This makes `tmpfs` mounts ideal for temporary, sensitive data that should not be stored on disk. They are only available on Docker for **Linux** and are useful for storing in-memory caches, session data, or other files that don't need to persist.

### Key Features of `tmpfs` Mounts:

1. **Temporary storage**: Data is stored in the host's memory and is cleared when the container stops.
2. **Not persistent**: The data stored is not saved anywhere after the container shuts down.
3. **Cannot be shared**: `tmpfs` mounts cannot be shared across multiple containers.
4. **Linux-only**: `tmpfs` mounts are available only when Docker is running on Linux systems.

---

### How to use `tmpfs` mounts in Docker

You can use a `tmpfs` mount with either the `--mount` flag or the `--tmpfs` flag. Here's how each works:

1. **Using `--mount` flag** (more flexible):
   ```bash
   docker run -d \
     -it \
     --name tmptest \
     --mount type=tmpfs,destination=/app \
     nginx:latest
   ```
   In this example, a `tmpfs` mount is created at the `/app` directory inside the container.

2. **Using `--tmpfs` flag** (simpler):
   ```bash
   docker run -d \
     -it \
     --name tmptest \
     --tmpfs /app \
     nginx:latest
   ```
   This command does the same thing but with less flexibility for configuration.

---

### Specifying `tmpfs` options with `--mount`

If you need more control over the `tmpfs` mount, such as setting its size or permissions, you should use the `--mount` flag. There are two optional settings:

1. **`tmpfs-size`**: Specifies the maximum size of the `tmpfs` mount in bytes.
2. **`tmpfs-mode`**: Sets the file permissions for the `tmpfs` mount (e.g., 1770 for restricting access).

Example with custom options:
```bash
docker run -d \
  -it \
  --name tmptest \
  --mount type=tmpfs,destination=/app,tmpfs-size=100m,tmpfs-mode=1770 \
  nginx:latest
```
Here:
- The `tmpfs-size` is set to `100 MB`.
- The `tmpfs-mode` is set to `1770`, making the files not world-readable.

---

### Why use `tmpfs`?

- **Temporary Storage**: If you need temporary, non-persistent data in memory.
- **Security**: Storing sensitive files that should not persist on disk.
- **Performance**: Since data is stored in memory, `tmpfs` mounts can offer faster read/write performance compared to disk storage.

---

### Limitations of `tmpfs` Mounts:

- **Not shareable**: `tmpfs` mounts cannot be shared across containers like volumes or bind mounts.
- **Linux only**: They are only available when running Docker on Linux systems.
- **Size limits**: By default, `tmpfs` mounts can use up to 50% of the host's RAM, but this can be configured.
