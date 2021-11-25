'''

This program checks if a string reads same was reading the other way.
'''

S1 = input ( 'enter a string:')
#S2 = ['none']*len(S1)
S2 = []
print (S1)

'''[
for i in range(0, len(S1)):
    S2.append ( S1[len(S1) - i] )
'''

# below code fixes the index out of range issue that gives above. Here introduce the
#for using instead of usind index value i

counter1 = 1;
for i in range(0, len(S1)):
    S2.append ( S1[len(S1) - counter1] )
    counter1 = counter1+1

print (S2)
    
#Ref:
#https://www.youtube.com/watch?v=dDU3UuHVLVA



 



