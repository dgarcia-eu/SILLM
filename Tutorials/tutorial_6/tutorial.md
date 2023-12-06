## Server Tutorial
### General Information
A server is accessed through a shell. A shell is a User Interface intended to operate a computer, just like a normal desktop, but text-based. The standard shell for Linux is bash
and for MAC ZSH, but there is not much difference for standard operations. For windows, I recommend installing WSL2: https://learn.microsoft.com/en-us/windows/wsl/install

In general, a shell command has the following structure:

`<command> <flags> <file>`

This is nothing more than executing a program (command) with the possibility of attaching different options (flags) and applying that programm to a file.

For example, if I want to print a text file, I would do the following:

`cat text.txt`

If I would want to add number lines to the output, i can add an option (called flags) to do so.

`cat -n text.txt`  

It is also possible to chain commands together, using a pipe.

`cat -n text.txt | grep "cake"`

Using the | operator, I pass the output to the command grep, which searches for the word "cake" in the text file, and only lines containing that word are printed to the output.
Of course, i can add flags to grep as well:

`cat -n text.txt | grep -i "cake"`

The -i flag makes the search case-insensitive, such that all occurrences of cake are printed, irrespective of the casing of the character.

Commands are aborted using the shortcut CTRL+C. In general, every operation possible on a normal desktop is also possible using the shell (and much, much more). Hence, if I want to to anything, I can just google "create a file bash". Almost every result found applicable to Linux is applicable to Mac as well.


### Accessing a Server
A server is accessed through SSH, which provides a secure and encrypted connection. The command structure is the following:

`ssh username@server_adress`

Now I am on the server, and I can list all files and directories with the command:

`ls -la`

where `-la` is a flag for a nicer print on the terminal. Just `ls` works as well.

Disconnecting from the Server

`Exit`

### Some useful operations on a server

Creating directories

`mkdir new_dir`

Create files

`touch new_file.txt`

Show current directory

`pwd`

Move files (~ is the location of the home directory, usually /home/user)

`mv newfile.txt ~/new_location`

Copy files

`cp newfile.txt ~/new_location`

Remove files

`rm file.txt`

Be careful when doing any file operation. These operations are not revertible and definite. There is no trash were files can be recovered. Check the operations you are doing and keep backups. You can always write out multiple files to do operations on, e.g.

`rm file1 file2 file3`

You can use wildcards when naming files, for example:

`rm *.txt`

removes all .txt files in the current directory. Be careful that the wildcard expression corresponds to what you actually want to do.


Copying Files to a server (when on local computer)

`scp file.txt username@server_adress:~/desired_location`


Running a script:

`python3 script.py` (python is always preinstalled, although versions can be out of date)

`R script.R` (R needs to be installed)

Back Search:\
You can search your command history with CTRL+R, there is no need to retype commands.

Autocomplete is possible with TAB

### Running remote scripts with tmux
open tmux session

`tmux`
run scripts

detach session with
`ctrl+b+d`

list sessions
`tmux ls`

reattach previous session
tmux attach -d -t number_of_session (usually zero)




