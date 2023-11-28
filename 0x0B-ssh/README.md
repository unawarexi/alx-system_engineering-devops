# Server Basics README

## What is a server?

A server is a computer or system that is dedicated to managing network resources and providing services to other computers, known as clients. Servers respond to requests from clients and can serve various purposes,
 such as hosting websites, databases, or applications.

## Where servers usually live?

Servers are typically housed in data centers. Data centers are facilities equipped with network infrastructure, cooling systems, and security measures to ensure the continuous operation of servers.

## What is SSH?

SSH (Secure Shell) is a cryptographic network protocol that provides a secure way to access and manage network devices, servers, and other systems remotely. It allows for secure data communication between 
the client and the server over an unsecured network.

## How to create an SSH RSA key pair?

To create an SSH RSA key pair, you can use the following command:

```bash
ssh-keygen -t rsa -b 2048 -C "your_email@example.com"
```
This command generates a new SSH key pair with a 2048-bit RSA key and associates an email address with the key.

## How to connect to a remote host using an SSH RSA key pair?
To connect to a remote host using an SSH RSA key pair, use the following command:

```bash
ssh -i /path/to/private-key username@remote_host
```
Replace `/path/to/private-key` with the path to your private key file, username with the remote user's username, and `remote_host with the IP address or domain of the remote host`.

## The advantage of using #!/usr/bin/env bash instead of /bin/bash
The shebang `(#!/usr/bin/env bash)` is preferred over specifying the absolute path (/bin/bash) 
- as it allows for better portability. 
- Using env ensures that the user's PATH environment variable is used to locate the Bash interpreter, 
- making the script more adaptable to different system configurations.