##Program
A program is a squeunce of instructions that specifies how to perform a computation. The computation might be something mathematical, such as solving a system of equations or finding the roots of a polynomial, but it can also be a symbolic computation, such as searching and replacing text in a document or something graphical, like processing an image or playing a video.

##Process
A process is simply an instance of a running program. The operating system allows the process to use the CPU, memory, and other resources, and provides system calls to allow the process to perform various tasks, such as reading from and writing to files.

code segment | data segment | heap
-------------|--------------|------
Stack | Registers
-------------|--------------|------

Seperate Memory Space - i. One process connot access the memory of another process. 
                        ii. One process cannot directly communicate with another process.

##Thread
A thread is a unit of execution within a process. A process can have multiple threads running as part of it. Each thread in a process shares the process's resources, including memory and open files. Threads share the same memory space, so they can communicate with each other more easily than processes can.

code segment | data segment | heap
-------------|--------------|------
Stack | Registers
-------------|--------------|------

#Single Threaded Process - i. One thread per process.
                          ii. One process can have multiple threads.
                          iii. One thread can access the memory of another thread.
                          iv. One thread can directly communicate with another thread.

#Multi Threaded Process - i. One process can have multiple threads.
                         ii. One thread can access the memory of another thread.
                         iii. One thread can directly communicate with another thread.



##When to use Multi Threading
1. When you want to perform multiple tasks simultaneously.
2. When you want to perform multiple tasks in the background.
3. When you want to perform multiple tasks in parallel.
4. When you want to perform multiple tasks in a single process.
5. When you want to perform multiple tasks in a single program.
6. When you want to perform multiple tasks in a single application.
7. When you want to perform multiple tasks in a single system.

##When not to use Multi Threading
1. When you want to perform a single task.
2. When you want to perform a single task in the foreground.
3. When you want to perform a single task in the background.
4. When you want to perform a single task in parallel.
5. When you want to perform a single task in a single process.
6. When you want to perform a single task in a single program.
7. When you want to perform a single task in a single application.


