from functions import *
from time import time

 
correctPassword = "145"
run = True

correctPassword = ch2int_arr(correctPassword)
length = len(correctPassword)
password = [32] * length

start = time()
while run:
    password = next_step(password)
    if len(set(password)) == 1 and password[0] == 127:
        print(password)
        break
    elif correctPassword == password:
        print(str(int2ch_arr(password)) + " is correct")
        break
end = time()

print('Total time: %.9f seconds' % (end - start))



s = input()
print(get_distance(s[0], s[1]))

