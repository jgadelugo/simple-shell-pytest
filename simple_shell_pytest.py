import subprocess
import difflib


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

#x,y = open_interactive_test("/bin/bash")
#test_interactive(["ls\n", "cd ..\n", "ls\n"],x,y)
