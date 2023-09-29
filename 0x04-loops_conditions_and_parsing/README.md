# Loops, conditions and parsing

## README: Basic Linux Shell Commands and Scripting

This README provides a brief overview of common Linux shell commands and scripting concepts. 

## How to Create SSH Keys

To create SSH keys on a Linux system, you can use the following commands:

```bash
#### Generate an SSH key pair (RSA by default)
ssh-keygen -t rsa

#### Follow the prompts to set a passphrase (optional)
This will generate a pair of SSH keys (id_rsa and id_rsa.pub) in your ~/.ssh directory.
```

## Advantage of Using #!/usr/bin/env bash Over #!/bin/bash
Using `#!/usr/bin/env` bash as the shebang line at the beginning of a script is more portable because it allows the system to locate the bash interpreter using the env command. This is advantageous because it ensures the script will run with the user's preferred bash interpreter, which may be located in different directories on different systems. It increases compatibility across various environments.

## How to Use While, Until, and For Loops
While Loop
```bash
while [ condition ]; do
  # Commands to execute
done
```
Until Loop
```bash
until [ condition ]; do
  # Commands to execute
done
```
For Loop (Iterating over a range)
```bash
for (( i=1; i<=10; i++ )); do
  # Commands to execute
done
```


## How to Use if, else, elif, and case Condition Statements
#### If-Else Statement
```bash
if [ condition ]; then
  # Commands to execute if condition is true
 else
  # Commands to execute if condition is false

fi
```
#### If-Elif-Else Statement
```bash
if [ condition1 ]; then
  # Commands to execute if condition1 is true
elif [ condition2 ]; then
  # Commands to execute if condition2 is true
else
  # Commands to execute if no conditions are true
fi
```
#### Case Statement
```bash
case $variable in
  pattern1)
    # Commands for pattern1
    ;;
  pattern2)
    # Commands for pattern2
    ;;
  *)
    # Default case commands
    ;;
esac
```
## How to Use the Cut Command
The cut command is used to extract sections from lines of files or strings. Here's a basic example:

```bash
echo "Hello,World,OpenAI" | cut -d "," -f 2
```
This will output World as it extracts the second field (delimited by commas).

## Files and Other Comparison Operators
Comparison operators in bash are used to compare values. Here are some common ones:

-eq: Equal to
-ne: Not equal to
-lt: Less than
-le: Less than or equal to
-gt: Greater than
-ge: Greater than or equal to
Example usage:

```bash
if [ "$a" -eq "$b" ]; then
  # Commands if a is equal to b
fi
```
These operators can be used in conditional statements to compare values.

For more detailed information and usage, refer to the respective man pages or documentation for each command and concept.
