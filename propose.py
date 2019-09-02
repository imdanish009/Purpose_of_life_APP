love=input("what you love?using space between each lovething")
lovelist=love.split()
print(lovelist)
#########################
if lovelist[0]!="":
    good=input("what you are good at?using space between each")
    goodlist=good.split()
    print(goodlist)
else:
    print("pls asnwer to proceed")
    ####intersection##
lovelist1=set(lovelist)
goodlist1=set(goodlist)
passion=lovelist1.intersection(goodlist1)
print("passion is",passion)

 #############################   
if goodlist[0]!="":
    paid=input("what you can be paid for?")
    paidlist=paid.split()
    print(paidlist)
else:
    print("pls answer it")
    
if  paidlist[0]!="":
    need=input("what the world needs?(using space between each)")
    needlist=need.split()
    print(needlist)
else:
    print("pls answer the question")
    #####intersection#############
paidlist1=set(paidlist)
needlist1=set(needlist)
vocation=paidlist1.intersection(needlist1)
print("vocation is",vocation)
#######################################
if paidlist[0]!="":
    profession=paidlist1.intersection(goodlist1)
    print("profession is",profession)
else:
    print("plz enter the field")
mission=needlist1.intersection(lovelist1)
print("mission",mission)
 
purpose=passion.intersection(vocation,profession,mission)
print("purpose is:",purpose)
if purpose=="":
    print("no purpose")
