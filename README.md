# Fabric
Example How To Use Fabric To Automate Administration Tasks And Deployments

What is Fabric?
As the README says:

Fabric is a Python (2.5-2.7) library and command-line tool for streamlining the use of SSH for application deployment or systems administration tasks.
More specifically, Fabric is:

A tool that lets you execute arbitrary Python functions via the command line;
A library of subroutines (built on top of a lower-level library) to make executing shell commands over SSH easy and Pythonic.
Naturally, most users combine these two things, using Fabric to write and execute Python functions, or tasks, to automate interactions with remote servers. Let’s take a look.


To install Fabric on MacOS: 

Press Command+Space and type Terminal and press enter/return key.
Run in Terminal app:
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" < /dev/null 2> /dev/null
and press enter/return key. Wait for the command to finish.
Run:
$ brew install fabric


# Example to execute fab function from a file list. First, read pass the function read_hosts to read the file and after pass the function that you want to execute

cat servers-centos7.txt |fab read_hosts host_type -P
