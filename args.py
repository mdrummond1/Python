import sys

argNum = len(sys.argv) - 1

print("script has name %s" % (sys.argv[0]))
print("there are %d arguments" % (argNum))
if len(sys.argv) >= 2:
    print("second arg is %s" % (sys.argv[1]))