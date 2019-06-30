def solution(l):
    lista_1 = []
    lista_2 = []
    count = 0

    #if length of list if less than 3, we'll return 0
    if(len(l) < 3):
        return 0
    
    #in order to find the number of triples, we need to find all the divisors of each number
    #in the left part and in the right part
    for i in range(1, len(l)):  #start from index 1 of our list
    
        #check for divisors of our item l[i] in the left part and append them to first list
        #start from 0 to the previous element of current item
        # for x in l[:i]:         
        #     if(l[i] % x == 0):
        #         lista_1.append(x)
                
        #as an alternative and faster version, we can use list comprehension
        lista_1 = [x for x in l[:i] if l[i] % x == 0]
                
        #check for divisors of our item l[i] in the right part and append them to first list
        #start from the next index next to current item
        # for x in l[i+1:]:
        #     if(x % l[i] == 0):
        #         lista_2.append(x)
                
        lista_2 = [x for x in l[i+1:] if x % l[i] == 0]
        
        #number of triples of certain item is the product of lenghts of both lists
        count += len(lista_1) * len(lista_2)
        
        #clear lists for future use
        #if we use list comprehension, we don't need to clear the lists anymore
        # lista_1 = []
        # lista_2 = []

    return count