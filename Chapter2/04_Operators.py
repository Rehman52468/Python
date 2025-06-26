# Arithmetic Operators   
                        #   Arithmetic Operators are +,-,*,/ in this operator we add subtract and multiply and divide the values of variable 
a=10
b=25
c=a+b
print(a+b)


# Assignment Operators       
                        #  in this Operator we assign values by using =,+=,-= these are assignment operators
a=50                      
a+=25                   #Increment the value of 'a' by 25 and then assign it to a
print(a)

b=9
b-=7                     #Decrement the value of 'b' by 7  and then assign it to b
print(b)

#Comparison  Operators
                         #This operators are used to compare values (The output of this operator comes always in  boolean mean False or True)  
a= 10==9
print(a)  

r = 10<=20
print(r)

w = 50>=100
print(w)

z = 5!=5
print(z)


# Logical Operators
                     # Logical Operators are (AND,OR,NOT)  

        #  Truth Table of "OR"
                                            # OR Operator(in OR Operator if any one side is  true then the outputt will be true if both sides are false
                                            # then only in that case the output will be false ).
print("True or False is", True or False)
print("False or True is", False or True)
print("True or True is", True or True)
print("False or False is", False or False) 


         #Truth Table of  "AND"    
                                             # AND Operator(in AND operator if both sides are true then the output will be true 
                                            #  otherwise if any one side is false then the output will be false).
print("True and False is", True and False)
print("False and True is", False and True)
print("True and True is", True and True)
print("False and False is", False and False)          


          #Truth Table of "NOT"
                  # NOT Operator(Only single oprent are used in NOT Operator and gives you the oppssite output means
                  #  if u give true input in "not operator" the output will be false
                  #  if u give false input the output will give u True ).  
print(not(True))
print(not(False))           