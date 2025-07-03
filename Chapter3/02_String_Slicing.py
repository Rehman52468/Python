Z= "Rahman"

A = Z[1:4]     # start from index 1 to 4 all the way (excluding index4) mean index 4 will be not included. Because index start includes and the last index
#does not includes

print(A)



Name = "Rahman Ullah"

name = Name[5:]         # Name[5:] is same as Name[5:11]

print(name)



Name = "Rahman Ullah"

name = Name[:9]         # Name[:9] is same as Name[0:9]

print(name)
  

# Negative Slicing

Name = "Waqas"

print(Name[-4:-2])

print(Name[1:3])


Name = "RahmanUllah"

print(Name[-9:-3])

print(Name[2:8])
