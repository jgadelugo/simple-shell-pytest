import subprocess
import difflib
import os


def myexit(message, code=0):
  "This exits with a custom error message and exit code"
  print(message)
  exit(code)

def get_commands(filename):
  "This gets the commands from a file for interactive mode testing"
  if os.path.isfile(filename):
    f = open(filename, 'r')
    if f.mode == 'r':
      return f.readlines()
    return []
  myexit('Error: Commands file \'' + filename + '\' does not exist.', 1)

def open_interactive_test(ex):
  "This prepares two shell processes in interactive mode."
  x = subprocess.Popen("",stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,executable="/bin/sh")
  y = subprocess.Popen("", stdin=subprocess.PIPE,
  stdout=subprocess.PIPE,
  stderr=subprocess.PIPE,executable=ex)
  return (x, y)


def test_interactive(tests, sh, hsh):
  "This interactively tests a list of commands."
  for test in tests:
    sh.stdin.write(test)
    hsh.stdin.write(test)

  shout, sherr = sh.communicate()
  shret = sh.returncode

  hshout, hsherr = hsh.communicate()
  hshret = hsh.returncode

  print("----------STDOUT----------")
  for line in difflib.Differ().compare(shout.splitlines(), hshout.splitlines()):
    print(line)

  print("----------STDERR----------")
  for line in difflib.Differ().compare(sherr.splitlines(), hsherr.splitlines()):
    print(line)
  print("----------EXIT CODES----------")
  print('sh exit code: ' + str(shret))
  print('simple-shell exit code: ' + str(hshret))

def run_interactive(ex, commandfile):
  "This runs an interactive test using the given executable and the given file with commands"
  if os.path.exists(ex):
    print("__________ Interactive Test __________")
    print("")
    x,y = open_interactive_test(ex)
    test_interactive(get_commands(commandfile), x, y)
    return
  myexit("Error: Executable file " + ex + " not found.")


run_interactive("/bin/bash","temptest")
