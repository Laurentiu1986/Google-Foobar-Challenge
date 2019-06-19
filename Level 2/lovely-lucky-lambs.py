#####Amzarescu Laurentiu-Gabriel#####
def solution(total_lambs):
    total = 1   #total of lambs given
    current = 1    #current henchman   
    minimum_hench = 1    #number of henchmen
    
    #pre-calculate the number of LAMBs given in the first iteration
    #here, 'total' will be the first henchman's number of LAMBs  gathered with the previous total
    total = current + total*2   
    
    while total <= total_lambs:   #execute while 'total' is under 'total_lambs'
        current = current*2     #rule no. 2; for the current henchman, we'll double the number of LAMBs of the previous henchman
        total = total + current*2   #sum the current 'total' with the next henchman's number of LAMBs
        minimum_hench += 1      #increment the number of henchmen for the generous strategy
    
    maximum_hench = 1
    last = 0
    current = 1
    total_lambs -= 1
    while total_lambs > 0:
        if total_lambs < last + current:
            break
        maximum_hench += 1  #increment the number of henchmen for the stingy strategy
        
        #it looks like fibonacci series, so we'll always 
        #sum the current henchman with the previous number of LAMBs, 
        #then we'll assign last to the new current
        current, last = current + last, current  
        total_lambs -= current   #decrease the amount of LAMBs
        
    return maximum_hench - minimum_hench