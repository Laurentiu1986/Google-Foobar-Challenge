def solution(x, y):
    
    m = int(x)
    f = int(y)
    count = 0
    
    '''
    In order to make the solution optimal and run the worst case in the best time,
    we need to cut the steps down and minimize the number of counts that need to be done
    
    Instead of starting from M=1 and F=1 to achieve the (M, F) target, we can start directly 
    from the target and process until we reach (1, 1)
    In order to make this happen faster, we know that we can count immediately more than half 
    of our steps by dividing the greater type of bomb with the other type. 
    
    *For example, if we have M = 7 and F = 30, we'll divide 30//7 and keep the real floor (using the real floor division operator)
    and in that way, we already know that 30//7 = 4 and we can increase the number of steps with 4.
                                    M   F
                                    7   30
                                    7   23  -> F-M  |
                                    7   16  -> F-M  |   => 4 steps that we already know by division
                                    7   9   -> F-M  |
   remainder of 30//7 is 2  ===>    7   2   -> F-M  |  
  , so we'll assign F = 2           7   2   -> M-F   
                                    5   2   -> M-F
                                    3   2   -> M-F   
                                    1   1   
                                   
    Next step is to calculate the rest of the division in order to assign the type of the bomb
    with the remainder
    '''
    if f != 1 and m != 1:   #if F or M is already equal to 1, we don't need to use the following algorithm
        if m > f:
          division = m // f    #real floor division
          m = m % f            #remainder 
          count += division    #increase number of steps with the 
        elif f > m:
          division = f // m
          f = f % m
          count += division
    
    if(m % 2 == 0 and f % 2 == 0):   #we know that if both types of bombs has an even number of bombs, then it's impossible to move on
        return "impossible"
    
    while (m > 1 or f > 1):     #execute the algorithm while m and f are greater than 1
        if m > f:               
            m = m - f           #substract from the greater bomb the number of the other type
            count += 1
        if f > m:
            f = f - m
            count += 1
        
        
        '''
        In the following block, I used another way to shorten the number of process made by the algorithm.
        
        *For example, if we have M = 4 and F = 7, we'll use the following steps:
                                            M   F
                                            4   7
                                            4   3
                                            1   3   |
                                            1   2   |   => in those 3 steps, we always have the M equal with 1, so we can shorten the algorithm 
                                            1   1   |      by comparing each of the bomb's type with 1, and if we find a match, then we'll
                                                           increase the count with the 'greater number - 1' and make the greater bomb equal to 1
                        So, when the M = 1 and F = 3, then we know that we'll substract until the F will be 1.
                        In that way, we can make immediately F = 1 and increase the steps count with F-1 ( 3-1 = 2 )
                                            
        '''
        if m == 1:              
          count += f - 1
          #print("--------shortcut m")
          f = 1
        elif f == 1:
          count += m - 1
          #print("--------shortcut f")
          m = 1
        
        if m == 1 and f == 1:           #if m=1 and f=1, we are done
            return str(count)
            
       
        if m == f:                      
            return "impossible"
    return "impossible"
            
    
    