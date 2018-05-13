epic_programmer_dic={'tim berners-lee':['tbl@gmail.com',111],'guido van rossum':['gvr@gmail.com',222],
                     'linus torvalds':['lt@gmail.com',333],'lary page':['lp@gmail.com',444],'sergey brin':['sb@gmail.com',555]}
print epic_programmer_dic['tim berners-lee'][1]

#programmer=epic_programmer_dic['tim berners-lee']
#print programmer[1]

#personsName=raw_input('enter name here: ').lower()
#print personsName
def searchPeople(personsName):
    try:
        personsInfo=epic_programmer_dic[personsName]
        print 'name: ' +personsName.title()
        print 'email: '+personsInfo[0]
        print 'Number: '+str(personsInfo[1])
    except:
        print 'No information found for that name'

userWantsMore=True
while userWantsMore==True:
    personsName=raw_input('Please Enter a Name: ').lower()
    searchPeople(personsName)
    userWantsMore=False
searchAgain=raw_input('Search Again? (y/n)')
if searchAgain=='y':
    userWantsMore=True
elif searchAgain=='n':
    userWantsMore=False
else:
    print "I do not understand what you mean by quitting"
    userWantsMore=False
