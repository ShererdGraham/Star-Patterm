#loops with i incrementing from 1 to num_of_lines
def printstars(num_of_lines):
    for i in range(num_of_lines+1) :
        #for the first half of the for loop, a number of stars are printed on each line increasing by one
        if i <= (num_of_lines+1)/2 : 
            print("*"*i)
        #for the second half of the loop the number of stars go down as it loops
        else :
            print("*"*((num_of_lines+1)-i))
    print("\n")

while(True):
    #number of lines of stars are entered
    num_of_lines=int(input("Please enter the number of lines for the pattern or 0 to close program\n"))
    if num_of_lines == 0:
        break
    else :
        printstars(num_of_lines)