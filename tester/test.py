#!/usr/bin/env python

"""simple (bad) tester
  2 args, program and directory
  program is path to executable to run
  directory si path to directory containing input and output to test
  expects .in and .out files with matching basenames.
  runs program with each .in file as input and checks that
  the output for each matches the corresponding .out file
"""

import argparse, os, re, subprocess

parser = argparse.ArgumentParser(description="simple tester")
parser.add_argument("program")
parser.add_argument("test_directory")
#optional arg: whether to pass input on stdin or from argument
args = parser.parse_args()

#probably a better way to ensure that program has the ./ at the front and dir ends in / but I'm lazy.
prog = args.program
if prog[:0] != ".":
    if prog[0] != "/":
        prog = "/" + prog
    prog = "." + prog
dir = args.test_directory
if dir[-1] != "/":
    dir = dir + "/"

dirlist = os.listdir(dir)
# find each basename in dirlist, 
class Testset:
    in_file = None
    out_file = None

    def __repr__(self):
        return f"<Testset in_file:{self.in_file} out_file:{self.out_file}>"

tests = {}
for e in dirlist:
    if re.search(r"\.[Oo][Uu][Tt]$", e):
        bn = e[:e.rfind(".")]
        if bn not in tests:
            tests[bn] = Testset()
        tests[bn].out_file = e
    elif re.search(r"\.[Ii][Nn]$", e):
        bn = e[:e.rfind(".")]
        if bn not in tests:
            tests[bn] = Testset()
        tests[bn].in_file = e
    else:
        print(f"WARNING: skipping {e}")

for e in tests:
    t = tests[e]
    if t.in_file == None:
        print(f"WARNING: missing {t}.in, skipping {t}")
        del(tests[e])
    if t.out_file == None:
        print(f"WARNING: missing {t}.out, skipping {t}")
        del(tests[e])

for e in tests:
    t = tests[e]
    # subprocess.run requires python 3.5 or higher
    output = subprocess.run([prog, dir + t.in_file], stdout=subprocess.PIPE, cwd=os.getcwd()).stdout.decode("UTF-8")

    with open(dir + t.out_file, "r") as file:
        true_output = file.read()

    if output != true_output:
        print(f"TEST {e} FAILED.")#\nEXPECTED:\n{true_output}\nGOT:{output}\n")
        import difflib
        d = difflib.Differ()
        diff = d.compare(true_output.splitlines(), output.splitlines())
        print('\n'.join(diff))
    else:
        print(f"TEST {e} PASSED.")

