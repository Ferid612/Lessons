test_a = [1,3,5,7,9,11]
test_b = [2,4,6,8,10]

test_a.append(12)
test_a.extend(test_b)
# Verilen ededlerden sade olanlari ekrana yazdir.
# 1 ve ozunden basqa boleni olmayan ededlere sade ededler deyilir deyilecek deyirem

import math



def ededlerin_sade_olub_olmadigini_tapin(ededler):
    for eded_a in ededler:
        sadedirmi = True
        for i in range(2, int(math.sqrt(eded_a))+1):
            if eded_a % i == 0: 
                sadedirmi = False
                
        if sadedirmi:
            print("Eded sadedir", eded_a)
        else:
            print("Eded sade deyil",eded_a)
      




ededler_1 = [12,23,332,12,34,5457,77,75,545,4]
ededler_2 = [12,23,332,12,34,5457,77,75,545,42]
ededlerin_sade_olub_olmadigini_tapin(ededler_1)
ededlerin_sade_olub_olmadigini_tapin(ededler_2)
