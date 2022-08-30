import math 
ini_string = input('digite um binario')
print ("Initial string", ini_string) 
res = "{0:08b}".format(int(ini_string, 16)) 
print ("Resultant string", str(res)) 