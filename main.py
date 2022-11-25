from functions import *
from time import time

correct_password = "12mc" # 12q3w
len_password = len(correct_password)

mode = input("Введите режим работы 1 стандарт брут, 2 кастом брут\n")

if mode == '1': # default bruteforce
    alph = list(alph.keys())
elif mode == '2': # custom bruteforce
    s = input("Введите символ от которого перибирать пароль\n")
    alph = list(alph.keys())
    alph = create_distance_list(s, alph)


start = time()

print(alph)
i_count = len(alph) ** len_password - 1
for i in range(i_count):
    res = check_password(i_count - i, alph, correct_password)
    if res:
        print(res)
        break

end = time()
print('Total time: %.9f seconds' % (end - start))






