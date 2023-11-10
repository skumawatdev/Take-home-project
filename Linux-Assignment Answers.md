# take-home-project
DevOps-Assignment-Answers


**1. Provide steps to create a directory inside a directory where the parent directory does not exist.**

Solution:- 
![image](https://github.com/skumawatdev/take-home-project/assets/60931208/76e47cbb-d6ac-41dd-87eb-0a29717b1f10)


**2. How to install a package on a Linux server when there is no internet connection?**

Solution:- 
To install a package on a Linux server without an internet connection ----  package like net-tools

**For Red Hat-Based Systems (RHEL, CentOS):**

1. Download the package on a system with internet access.

   ```bash
             yumdownloader net-tools
    ``` 
2. Transfer the downloaded RPM package to the offline server, for example, using a USB drive or SCP.
3. On the offline server, navigate to the directory where the RPM package is located.
4. Install the package and its dependencies using yum:
   
 ```bash
    sudo yum localinstall net-tools.rpm
 ```

**3. How to access specific folders of Server A from Server B and Server C?**

Solution:-

We can access this by using **SSH** commands to access specific folders on Server A from Server B and Server C .

1. Firstly Generate SSH keys on Server B and Server C (if not done).

  ```bash
         ssh-keygen
  ```

2. Now Copy the public key from Server B and Server C to Server A , This file allows **~/.ssh/authorized_keys** to securily login , passwordless access.

     ```bash
         ssh-copy-id user@ServerA
     ```

3. Access Specific Folders on Server A from Server B and Server C --

  To access specific folders on Server A from Server B, use SSH:

```bash
       ssh user@ServerA
```

  To access specific folders on Server A from Server C, use SSH:

```bash
    ssh user@ServerA
```

4. Navigate to the Specific Folder on Server A --

   Once logged into Server A from Server B or Server C, navigate to the specific folder you want to access:

   ```bash
   cd /path/to/specific/folder
   ```

**4. How to check all the running processes from a server?**

Solution:-


  ![image](https://github.com/skumawatdev/take-home-project/assets/60931208/3e75730a-ffef-49c4-b79b-9a458f38ca70)

  Examine the Process List --

    ![image](https://github.com/skumawatdev/take-home-project/assets/60931208/e4e1f120-0ecc-41aa-86d7-3d166fab68f3)


**5. Provide the command to delete all the files older than X days inside a specific directory.**

Solutions:- 

   To delete all files older than X days inside a specific directory, you can use the find and rm commands in combination.

   ```bash
            find /path/to/directory -type f -mtime +X -exec rm {} \;
   ```

**6. Create a shell script to identify the process ID
		a. script should as a user input for process ID.
		b. If the process exists script should print the process ID and exit.
	   	c. If the process doesn't exist script should print the process doesn't exist and asks for another input.**

Solution:-

![image](https://github.com/skumawatdev/take-home-project/assets/60931208/4ea77a57-3a49-4be9-9385-75aace5d49c4)

**Script-Code**
```bash
#!/bin/bash

# Prompt the user for a process ID
read -p "Enter a process ID: " pid

# Check if the process exists
if ps -p $pid > /dev/null; then
    echo "Process with ID $pid exists."
else
    echo "Process with ID $pid does not exist."
fi
```








