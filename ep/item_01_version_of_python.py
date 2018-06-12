#!/usr/bin/env python

# Chapter 1: Pythonic thinking
#
# The idioms of a programming language are defined by its users. Over the
# years, the Python community has come to use the adjective Pythonic to
# describe code that follows a particular style. The Pythonic style isn't
# regimented or enforced by the compiler. It has emerged over time through
# experience using the language and working with others. Python programmers
# prefer to be explicit, to choose simple over complex, and to maximize
# readability (type import this).
#
# Programmers familiar with other language may try to write Python as if it's
# C++, Java, or whatever know best. New programmers may still be getting
# comfortable with the vast range of concepts expressible in Python. It's
# important for everyone to know the best--the Pythonic--way to do the most
# common things in Python. These patterns will affect every program you write.
#
#
# Item 1: Know which version of python you're using
#
# Things to Remember
#
# 1. There are two major version of Python still in active use: Python 2 and
#    Python 3.
# 2. There are multiple popular runtimes for Python: CPython, Jython,
#    IronPython, PyPy, etc.
# 3. Be sure that the command-line for running Python on your system is the
#    version you expect it to be.
# 4. Prefer Python 3 for your next project because that is the primary focus of
#    the Python community.

import sys
import subprocess

p = subprocess.Popen(["python", "--version", "2>&1"], stdout=subprocess.PIPE)
out, err = p.communicate()
print("Default Python version: %s" % out)
print(sys.version_info)
print(sys.version)

p = subprocess.Popen(["python3", "--version"], stdout=subprocess.PIPE)
out, err = p.communicate()
print("\nDefault Python3 version: %s" % out)
