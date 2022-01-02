'''

This program checks if a string reads same was reading the other way.
'''

S1 = input ( 'enter a string:')
#S2 = ['none']*len(S1)
S2 = []
print (S1)
# This loop uses index value directly.
for indexValue in S1:
    print ( indexValue )



# This for loop uses the index position to loop around. Here is pritns the string
#last to first
# Use of counter to avoid the array index out of bound error.
counter1 = 1;
for indexPostion in range(0, len(S1)):
    S2.append ( S1[len(S1) - counter1] )
    counter1 = counter1+1

print (S2)
    
#Ref:
#https://www.youtube.com/watch?v=dDU3UuHVLVA



 



