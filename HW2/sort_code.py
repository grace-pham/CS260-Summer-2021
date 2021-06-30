#Mark Boady - CS 260
#Drexel University

#Implement the sorts from lecture in this file.

#Here are two example sorts to start off with.

#These functions have no return values.
#They sort the array in place.

#The built in sort is probably optimal.
def builtin(A):
    A.sort()
    return

#Gnome sort is pretty weird.
#It is like a bad version of insertion sort
#Read more:https://en.wikipedia.org/wiki/Gnome_sort
def gnome(A):
    #Current index in the array
    i = 0
    #While we haven't made it to the end
    while i < len(A):
        #We cannot compare at 0
        #Otherwise check order is correct
        if i == 0 or A[i] >= A[i-1]:
            i+=1#Move forward
        else:
            #Swap values
            temp = A[i]
            A[i] = A[i-1]
            A[i-1] = temp
            #Go back one and try again
            i-=1
    return

#Implement the sorts from class below!
