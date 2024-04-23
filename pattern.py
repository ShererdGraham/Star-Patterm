#number of lines of stars are set, 9 is default but this can be edited easily
num_of_lines=9
#loops with i incrementing from 1 to num_of_lines
for i in range(num_of_lines+1) :
    #for the first half of the for loop, a number of stars are printed on each line increasing by one
    if i <= (num_of_lines+1)/2 : 
        print("*"*i)
    #for the second half of the loop the number of stars go down as it loops
    else :
        print("*"*((num_of_lines+1)-i))
    