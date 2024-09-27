---
tags:
  - docker
  - docker-presistence
---
### **What are Bind Mounts?**
- **Definition**: A bind mount is when a file or directory on your host machine (the computer running Docker) is mapped (mounted) into a Docker container. This allows the container to directly use, modify, or view files from the host.
- **How it works**: You specify a path on your host system (like `/path/on/host`) and a path in your container (like `/path/in/container`). When the container runs, it sees the files in the specified host path as if they are inside the container.

### **Key Points**:
1. **Direct Host Access**: Bind mounts directly map a host's directory to the container, unlike Docker volumes where Docker manages the storage.
2. **High Performance**: Since bind mounts are directly tied to the host’s file system, they are highly performant but rely on the structure of the host's file system.
3. **Automatic Directory Creation**: If the directory doesn’t exist on the host, Docker will automatically create it for you when using `-v` (but not with `--mount`).

### **Basic Syntax**:
There are two main ways to use bind mounts:
- Using `-v` or `--volume` (older style).
- Using `--mount` (newer, more explicit style).

Let’s compare them:

---

### **1. Using `-v` (or `--volume`)**
This is the older, shorter method and consists of three parts separated by a colon `:`:
- **Host path**: The path to the file or directory on your host system.
- **Container path**: The location where you want to mount this directory inside the container.
- **Optional options**: Such as making the mount read-only (`ro`).

**Example**:
```bash
docker run -d -v /path/on/host:/path/in/container nginx
```
- **Host path**: `/path/on/host`
- **Container path**: `/path/in/container`

---

### **2. Using `--mount`**
This newer method is more readable but also a bit more verbose. It uses key-value pairs to specify the mount configuration.
- **type**: The type of mount (`bind`, `volume`, or `tmpfs`).
- **source**: The host file or directory (sometimes referred to as `src`).
- **destination**: The path inside the container (sometimes referred to as `dst` or `target`).
- **Other options**: Like read-only, propagation options, etc.

**Example**:
```bash
docker run -d \
  --mount type=bind,source=/path/on/host,target=/path/in/container \
  nginx
```
- **type**: `bind` (we are using a bind mount).
- **source**: `/path/on/host` (the directory on the host).
- **target**: `/path/in/container` (the directory inside the container).

---

### **When to Use Bind Mounts**:
- **Development**: If you're working on a codebase on your local machine and want the container to see the changes in real time, bind mounts are useful.
- **Testing**: You can replace parts of the container file system with a bind mount to test configurations or new versions of files.
- **Shared Data**: You might want multiple containers to access and share the same data stored on the host machine.

---

### **Differences Between `-v` and `--mount`**:
1. **Flexibility**: The `--mount` syntax is more flexible and easier to understand, especially for advanced cases.
2. **Automatic Creation**: Using `-v`, Docker automatically creates the directory if it doesn’t exist on the host (as a directory). `--mount` generates an error if the directory doesn’t exist.
3. **Options**: `--mount` allows you to explicitly set advanced options like bind propagation and is preferred for more complex configurations.

---

### **Read-Only Mounts**
Sometimes, you only need the container to read data but not write to the host system. You can make the mount read-only.

#### Using `-v`:
```bash
docker run -d -v /path/on/host:/path/in/container:ro nginx
```
#### Using `--mount`:
```bash
docker run -d \
  --mount type=bind,source=/path/on/host,target=/path/in/container,readonly \
  nginx
```

### **Recursive Mounts**
Recursive mounts allow you to bind-mount a directory that contains other mounts (sub-mounts). By default, Docker includes sub-mounts in the bind mount, but you can control this behavior using the `bind-propagation` option with `--mount`.

#### Example (using `--mount`):
```bash
docker run -d \
  --mount type=bind,source=/path/on/host,target=/path/in/container,bind-propagation=rshared \
  nginx
```
This allows changes to submounts to be visible in both the container and the host.

---

### **SELinux Labels**:
- If you're running Docker on a system with SELinux (like some Linux distributions), you can control how SELinux handles bind mounts with the `:z` or `:Z` options.
   - **:z**: Makes the bind mount content available to multiple containers.
   - **:Z**: Private, content is only available to the specific container.

#### Example (using `-v` with `selinux`):
```bash
docker run -d -v /path/on/host:/path/in/container:z nginx
```

**Warning**: Be cautious using SELinux options on sensitive directories (like `/usr`), as they could impact your host’s operability.

---

### **Advanced Use Cases**:
1. **Mount into Non-Empty Directories**: When you mount into a non-empty directory in the container, the contents of that directory are hidden by the mount. This can be useful for overriding directories like `/app` with new builds of your code without rebuilding the image.
   - Example: `docker run -d --mount type=bind,source=/new/code,target=/app nginx`
   
2. **Mount Propagation**: This refers to how changes to mounts inside a container affect the host (and vice versa). You can choose from:
   - **shared**: Changes in the container affect the host and vice versa.
   - **slave**: Only the host can propagate changes to the container, not the other way around.
   - **private**: No propagation in either direction (default).
   
   Example of using `bind-propagation`:
   ```bash
   docker run -d --mount type=bind,source=/path/on/host,target=/path/in/container,bind-propagation=rslave nginx
   ```
