#!/usr/bin/python
import subprocess
import difflib
from threading import Timer
import os
import sys


def myexit(message, code=0):
  "This exits with a custom error message and exit code"
  print(message)
  quit(code)

def printDiff(shout, sherr,shret, hshout, hsherr, hshret):
    "This prints the diff info for stdout, stderr and exitcodes of two processes."
    print("----------STDOUT----------")
    for line in difflib.Differ().compare(shout.splitlines(), hshout.splitlines()):
      print(line)

    print("----------STDERR----------")
    for line in difflib.Differ().compare(sherr.splitlines(), hsherr.splitlines()):
      print(line)
    print("----------EXIT CODES----------")
    print('sh exit code: ' + str(shret))
    print('simple-shell exit code: ' + str(hshret))

def get_commands(filename):
  "This gets the commands from a file for noninteractive mode testing"
  if os.path.isfile(filename):
    f = open(filename, 'r')
    if f.mode == 'r':
      return f.readlines()
    return []
  myexit('Error: Commands file \'' + filename + '\' does not exist.', 1)

def open_noninteractive_test(ex):
  "This prepares two shell processes in noninteractive mode."
  x = subprocess.Popen("",stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,executable="/bin/sh")
  y = subprocess.Popen("", stdin=subprocess.PIPE,
  stdout=subprocess.PIPE,
  stderr=subprocess.PIPE,executable=ex)
  return (x, y)


def test_noninteractive(tests, sh, hsh):
  "This noninteractively tests a list of commands."
  for test in tests:
    sh.stdin.write(test)
    hsh.stdin.write(test)

  shout, sherr = sh.communicate()
  shret = sh.returncode

  hshout, hsherr = hsh.communicate()
  hshret = hsh.returncode

  printDiff(shout, sherr, shret, hshout, hsherr, hshret)

def run_noninteractive(ex, commandfile):
  "This runs a noninteractive test using the given executable and the given file with commands"
  if os.path.exists(ex):
    print("__________ Non-interactive Test __________")
    print("")
    x,y = open_noninteractive_test(ex)
    test_noninteractive(get_commands(commandfile), x, y)
    return
  myexit("Error: Executable file " + ex + " not found.", 1)


def timeout_error():
  myexit("It's taking awhile. Infinite loop? (use Ctrl+C to exit early.)")


if (len(sys.argv) == 3):
  arg1 = sys.argv[1]
  arg2 = sys.argv[2]
else:
  myexit("Error: Usage - ./simple_shell_test.py EXECUTABLE COMMANDFILE", 1)

timeout = Timer(5,timeout_error)
timeout.start()
run_noninteractive(arg1, arg2)
print("")
timeout.cancel()
myexit("Diff successful.", 0)
