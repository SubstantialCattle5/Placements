---
tags:
  - docker
  - operatingsystem
---
Linux namespaces provide a powerful way to isolate processes from one another on the same system. When applied to containers (like in Docker), namespaces limit what resources a containerized process can access, giving it a virtualized view of the system, separate from other containers and the host system. One of these namespaces, the **user namespace**, remaps the container's users to a different set of users on the host machine. This is especially important for security when containers need to run processes as the `root` user within the container.

Here’s a breakdown of how **user namespace remapping** works:

### Purpose
The user namespace remapping feature in Docker ensures that even if a process inside the container is running as `root` (UID 0), it doesn’t have root privileges on the host. Instead, it is mapped to a less-privileged user on the host machine. This limits the scope of potential privilege-escalation attacks from the container to the host.

### Key Concepts
1. **UID and GID mapping:**
   - **/etc/subuid** and **/etc/subgid** files store mappings between container UIDs/GIDs and host UIDs/GIDs.
   - For example, the entry `testuser:231072:65536` means the user `testuser` is mapped to UID 231072 on the host but appears as UID 0 (root) inside the container.
   - Other UIDs follow: UID 1 inside the container becomes 231073 on the host, and so on.

2. **Remapping UID 0:**
   - Even though a process inside the container may run as root (UID 0), it is actually running as an unprivileged user (like UID 231072) on the host.
   - This prevents container processes from performing privileged operations on the host, even though they can act like root inside the container.

3. **Why remapping matters:**
   - Without remapping, if a container escapes isolation, it could run as root on the host system.
   - With remapping, any attempt to access or modify host resources as root is restricted, because the container’s root user is just a regular user on the host.

### How it works in Docker
To enable user namespace remapping, you:
1. Set up the user mappings in **/etc/subuid** and **/etc/subgid**.
2. Configure Docker to use these mappings by editing **/etc/docker/daemon.json** and setting `userns-remap` to a specific user or `default`.
3. Restart Docker to apply the configuration.
4. When Docker runs containers, it transparently applies the remapped UID/GID range to the container's processes, ensuring they operate under unprivileged UIDs on the host.

For example, if `testuser` is used:
- Inside the container, `testuser`'s processes might see themselves as running with UID 0 (root).
- On the host, these processes are actually running under UID 231072, preventing root-level access on the host.

### Handling limitations and special cases
1. **File permissions**: 
   - If a container needs access to a file on the host, the UID/GID on the host must match the remapped values (e.g., UID 231072). This may require changing ownership of files on the host.
   
2. **Container-specific adjustments**:
   - For specific containers (e.g., ones needing elevated privileges), you can disable user namespace remapping using the `--userns=host` flag. However, this might expose the container to host privileges.

3. **Known limitations**:
   - Not all features work with user namespaces enabled, such as PID or network namespace sharing with the host or certain external storage drivers.

In short, **user namespace remapping** provides an extra layer of security by ensuring that even root users inside containers don’t have root privileges on the host system.