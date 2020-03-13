import os
import sys
# Common class for compilers
class Compiler:
    # Compilers take ONE positional argument. No more than that.
    def __init__(self, *ccargs):
        self.ccomm = ccargs
        for n in ccargs:
            if n == "argument":
                self.argindex = ccargs.index(n)
                return
        self.argindex = 999
    def compile(self, argument):
        # if no positional arguments, just execute it
        if self.argindex == 999:
            ccline = ""
            for n in self.ccomm:
                ccline = ccline+" "+n
            os.system(ccline)
        else:
            ccline = ""
            for n in self.ccomm:
                if ccomm.index(n) == self.argindex:
                    ccline = ccline + " "+argument
                else:
                    ccline = ccline +" "+n
class MildCC:
    def __init__(self):
        # Base cli args from console
        self.cliargs = sys.argv[1:]
        # Common name for mild file, mild.mildlist(like Makefile or smth)
        self.mildfile = "mild.mildlist"
        # Prefix for all mild files: mildlist(usually one mildlist means one target, no more than that)
        self.mildprefix = ".mildlist"
    def parsemildlist(self):
        try:
            mildlist = open("mild.mildlist", "r")
        except:
            print("mild: no mildlists found")
            print("mild: no targets")
            exit(1)
            
        ctr = 0
        for line in mildlist:
            ctr += 1
            try:
                exec(line)
            except:
                print("mild: syntax error at line "+str(ctr))
                exit(1)
if __name__ == "__main__":
    mild = MildCC()
    mild.parsemildlist()
    exit(1)