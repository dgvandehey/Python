#print 'a'*1000 fuzzing test for Python. Prints one thousand a's

from hashlib import md5

import sys

def passcrack(pass_hash):
    for i in range(1001): #try 1-1000
        m=md5() #reset m
        m.update(str(i)) #calculate hash
        test_hash=m.hexdigest()
        if(test_hash!=pass_hash): #check the hash
            print "Failed:%s\t%s"(test_hash,pass_hash)
        else:
            print "Success %d" %i
            return
        m=md5()
        m.update(str(sys.argv[1]))
        passcrack(m.hexdigest())
        
        

