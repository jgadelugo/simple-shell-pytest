# The Simple Shell Lite Test Suite

## What is it?

~~~
It's basically a fancy diff program. It's not
intended to be a full checker for the simple
shell project. Rather, it's intended to be a
quickly usable sanity-checking program to see
how far away your simple-shell program is from
the behavior of the real /bin/sh shell.
~~~

## What does it not do?

~~~
It doesn't handle valgrind, and it doesn't handle
interactive mode (with a printed prompt string).
~~~

## What does it do?

~~~
It takes a simple shell executable and a file with
commands in it, and it runs all the commands in the
file in non-interactive mode for both /bin/sh and
your simple shell. It will then show you the unified
diff of the standard output, the standard error, and
the exit codes for both of the programs.
~~~

## Usage

~~~
The program is used in the form

    ./simple_shell_pytest.py EXECUTABLE COMMANDFILE

with EXECUTABLE replaced by the name of your simple
shell program and COMMANDFILE replaced by the name
of the file containing the commands you want to run.

The format of the COMMANDFILE file is just every command
to run on a separate line. For example:

   ls
   cd ..
   echo "Hello" && ls

and so on.