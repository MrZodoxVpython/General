rows = int(input("Masukkan rXc: "))
if rows <=4:
     print("Masukan rowsXcolumn minimal adalah '5'")
     exit()
# 	0 1	2 3	4 5 
# 0	    * 
# 1	*	*	   
# 2	    *        
# 3	    *	
# 4     * 
# 5 * * * * * *


for i in range(rows):
    for j in range(rows):
        if i == 1 and j == 0:
            print("*", end="") 
        elif j == rows // 2 or i == rows -1:
             print("*", end="") 
        elif i == rows:  
             print("*", end="")
        else:
            print(" ", end="")
    print()	# pindah new line

# 	0 1	2 3	4 5 6
# 0	* *	* *	* 
# 1         * 
# 2	* * * * * 
# 3	* 
# 4	* * * * * 	
# 5				

for i in range(rows):
    for j in range(rows):
        if i == 0 or i == rows // 2 or i == rows -1: 
            print("*",end="")
        elif i == 1 and j == rows -1: 
            print("*",end="")
        elif i == rows -2  and j == 0: 
            print("*",end="") 
        else:
            print(" ",end="")
        
    print() 

# 	0 1	2 3	4 5 
# 0	    * 
# 1	*	*	   
# 2	    *        
# 3	    *	
# 4	 	*	
# 5 * * * * * *

for i in range(rows):
    for j in range(rows):
        if i == 1 and j == 0:
            print("*", end="") 
        elif j == rows // 2 or i == rows -1:
             print("*", end="") 
        elif i == rows:  
             print("*", end="")
        else:
            print(" ", end="")
    print() # pindah new line