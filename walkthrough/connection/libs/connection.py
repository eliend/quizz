import os.path

def inc(username):
    nbcnx = 0
    filename = username + ".co.txt"
    if os.path.exists(filename):
        nbcnx = int(open(filename, "r").read())
    print 'nbcnx for ' + username + ' was ' + str(nbcnx)
    nbcnx = nbcnx + 1
    print 'nbcnx for ' + username + ' is now ' + str(nbcnx)
    open(filename, "w").write(str(nbcnx))
    return nbcnx
