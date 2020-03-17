import importlib
import sys

if __name__ == "__main__":
    mb = importlib.import_module("mild_base")
    args = sys.argv[1:]
    multithreadstate = 0
    asyncthreads = 0
    if "-M" in args:
        multithreadstate = 1
    if "--async" in args:
        asyncthreads = 1
    mild = mb.MildCC("mild", multithreadstate, asyncthreads)
    mild.parsemildlist()
    exit(1)