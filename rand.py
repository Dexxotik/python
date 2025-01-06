import random 
print("Random number")
num = random.randrange(1, 10)  
print( num )  
num = random.randrange(1, 10, 2)  
print( num )              
num = random.randrange(0, 101, 10)  
print( num )  

#Explanation –Select Random Elements

print("\nRandom elements")
random_s = random.choice('Random Module') #a string  
print( random_s )  
random_l = random.choice([23, 54, 765, 23, 45, 45]) #a list  
print( random_l )  
random_s = random.choice((12, 64, 23, 54, 34)) #a set  
print( random_s )  


#Explanation –Shuffle Elements Randomly
print("\nShuffle elements")
a_list = [34, 23, 65, 86, 23, 43]  
random.shuffle( a_list )  
print( a_list )  
random.shuffle( a_list )  
print( a_list )  
