
#Define a function called exchange which will accept an arguemnt which should be an integer
#The code assumes that there is list called "my_coins" which is similar to the available coins in any currency
#For example, the available coins and banknote are 1$, 5$, 10$, 25$, 100$
#If someone gives you 166$ the code should return the best way of exchange with less banknotes or coins to be given to the user
#Thus for 166$, it should return [100,25,25,10,5,1]
def exchange(x):
    
    my_coins = [1,5,10,25,100]
    new_list=[]
    rechange =[]
    y=x
    my_coins.sort(reverse=True)  #Sort the list in descending order
    
    # Create a new list and add to it only the values that are smaller than given amount which is "x"
    for i in range(len(my_coins)):
         if my_coins[i] < x:                  
              new_list.append(my_coins[i])
                  
    j = 0
    while y !=0:            
      if j <= len(new_list):    
          while y >= max(new_list): 
              rechange.append(new_list[j])    
              y = y-new_list[j]           
              continue
          new_list.remove(max(new_list))
    return rechange
print(exchange(166))

    
