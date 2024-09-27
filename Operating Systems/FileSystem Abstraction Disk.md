---
tags:
  - abstraction
  - operatingsystem
---
![[filesys]]

1. Stored in a tree data structure. 
2. each file contains a human readable name and an innode number for the operating system. 

## File System Api 

1. **Creating Files**
	1. Returns a number called `file descriptor`
	2. `file descriptor (fd)` is just an integer, private per process
	3. Existing files can only be opened through `fd`
	4. all operations uses `fd`. 
2. **Reading Files** 
	1. Uses the read system call. 
	2. reads data in bytes specified by the caller. 
	3. takes it from the file and stores in the buffer. 
	4. The read system call takes three arguments:
		1. The file descriptor of the file.
		2. The buffer where the read data is to be stored.
		3. The number of bytes to be read from the file.
	5. `ssize_t read(int fd, void *buf, size_t count);`
3. **Writing Files**
	1. Writes data to a buffer declared by the user to a given device, such as a file. 
	2. primary way to output data from a program by directly using a system call. 
	3. Destination is identified by a `file descriptor`.
	4. data to be written, for instance a piece of text, is defined by a pointer and a size, given in number of bytes.
	5. `write` thus takes three arguments:
		1. The file code (**fd**).
		2. The pointer to a buffer where the data is stored (**buf**).
		3. The number of bytes to write from the buffer (**nbytes**).
1. **close()** system call closes the file



