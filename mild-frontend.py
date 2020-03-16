import importlib
import sys

if __name__ == "__main__":
    mb = importlib.import_module("mild-base")
    args = sys.argv[1:]
    multithreadstate = 0
    if "-M" in args:
        multithreadstate = 1
    mild = mb.MildCC("mild", multithreadstate)
    mild.parsemildlist()
    exit(1)