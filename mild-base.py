import os
import sys
# Common class for compilers
class Compiler:
    # Compilers take ONE positional argument. No more than that.
    def __init__(self, *ccargs):
        self.ccomm = ccargs[:-1]
        self.extension = ccargs[len(ccargs)-1]
    def compile(self, argument):
        # if no positional arguments, just execute it
        ccline = ""
        for n in self.ccomm:
            ccline = ccline+" "+n
        ccline = ccline.replace("argument", argument)
        ccline = ccline.replace(".extension", "."+self.extension)
        os.system(ccline)
class MildCC:
    def __init__(self, mildlist):
        # Base cli args from console
        self.cliargs = sys.argv[1:]
        # Common name for mild file, mild.mildlist(like Makefile or smth)
        self.mildfile = mildlist
        # Prefix for all mild files: mildlist(usually one mildlist means one target, no more than that)
        self.mildprefix = ".mildlist"
        # Basic compiler settings: have gcc and g++ by default

        # A list for known file extensions, can be appended
        self.knownextensions = ["c", "cpp"]
        gcc = Compiler("gcc", "-O3", "argument.extension", "-o", "argument.o", "c")
        gpp = Compiler("g++", "-O3", "argument.extension", "-o", "argument.o", "cpp")

        # A list with compilers for the extensions above, must be strictly tied to knownext, e.g. "c" entry index is 0 in knownext, so gcc must have index 0 in compilerforext
        self.compilerforext = [gcc, gpp]
    def generate(self, *targets):
        for target in targets:
            print("mild: generating {} for target {}".format(target, self.mildfile)) 
            if target[-2:] == ".o":
                print("mild: assume {} is an file".format(target))
                files = [f for f in os.listdir('.') if os.path.isfile(f)]
                for f in files:
                    ft = os.path.splitext(f)[0]
                    print(ft)
                    if ft == target[:-2]:
                        ext = os.path.splitext(f)[1]
                        exty = ext[1:]
                        if exty in self.knownextensions:
                            extindex = self.knownextensions.index(exty)
                            CC = self.compilerforext[extindex]
                            CC.compile(target[:-2])
            else:
                raise NotImplementedError("Not now, not noooooww...")
    def parsemildlist(self):
        Generate = self.generate
        try:
            mildlist = open(self.mildfile+self.mildprefix, "r")
        except:
            print("mild: no mildlists found")
            print("mild: no targets")
            exit(1)
        ctr = 0
        for line in mildlist:
            exec(line)
    
if __name__ == "__main__":
    mild = MildCC("mild")
    mild.parsemildlist()
    exit(1)
