# def funksiya_a(arg):
#    arg = {"var_a": 20, "var_b": 40, "var_c": 30}
  


# x = {"var_a": 20, "var_b": 40, "var_c": 30}

# print("ilk x=", x)

# funksiya_a(x)

# print("son x=", x)


# keys = ["reng", "olcu", "material"]
# values = ["qirmizi", "xl", "pambiq"]

# dict_a = {}

# for key, value in zip(keys, values):
#     dict_a[key] = value


# print(dict_a)


# print("cem_a =",cem_a)

# print(sum_a(list_b))

# print_list(list_b)


# Bir liste alan ve listenin en büyük elemanını bulan bir Python fonksiyonu yazın. Kullanıcıdan bir liste girmesini isteyin ve bu fonksiyonu kullanarak en büyük elemanı ekrana yazdırın.

# Bir metin dizisi ve bir harf alan bir Python fonksiyonu yazın. Bu fonksiyon, metin dizisinde belirtilen harfin kaç kez geçtiğini hesaplar. Kullanıcıdan bir metin dizisi ve bir harf girmesini isteyin ve sonucu ekrana yazdırın.

# Verilen bir sayının faktöriyelini hesaplayan bir Python fonksiyonu yazın. Kullanıcıdan bir sayı girmesini isteyin ve bu fonksiyonu kullanarak faktöriyel sonucunu ekrana yazdırın.

# Bir dizi sayı alan ve bu sayıları sıralayan bir Python fonksiyonu yazın. Kullanıcıdan bir dizi sayı girmesini isteyin ve bu fonksiyonu kullanarak sıralanmış dizi sonucunu ekrana yazdırın.


# İki sayı arasındaki tüm asal sayıları bulan bir Python fonksiyonu yazın. Kullanıcıdan iki sayı girmesini isteyin ve bu fonksiyonu kullanarak bu aralıktaki asal sayıları ekrana yazdırın.

# Bir metin dizisi alan ve metindeki kelimelerin sayısını hesaplayan bir Python fonksiyonu yazın. Kullanıcıdan bir metin dizisi girmesini isteyin ve bu fonksiyonu kullanarak kelime sayısını ekrana yazdırın.

# Bir liste alan ve listedeki tek sayıları ayrı bir liste olarak döndüren bir Python fonksiyonu yazın. Kullanıcıdan bir liste girmesini isteyin ve bu fonksiyonu kullanarak tek sayıları içeren yeni bir liste sonucunu ekrana yazdırın.

# İki metin dizisi alan ve bu iki metni birleştiren bir Python fonksiyonu yazın. Kullanıcıdan iki metin dizisi girmesini isteyin ve bu fonksiyonu kullanarak birleştirilmiş metin sonucunu ekrana yazdırın.

# Bir liste alan ve listenin ortalamasını hesaplayan bir Python fonksiyonu yazın. Kullanıcıdan bir liste girmesini isteyin ve bu fonksiyonu kullanarak ortalama değeri ekrana yazdırın.




# dict_a = {
#    "value_1":10,
#    "value_2":20,
#    "value_3":30,
# }


# max=dict_a["value_1"]
# max_key = "value_1"
# for key in dict_a.keys():
#    if dict_a[key]>max:
#       max = dict_a[key]
#       max_key = key
      
   
# print(max)
# print(max_key)
      
   



# def f(*args):
#     for i in args:
#             print(i)


# a = [1, 2, 3]
# t = (4, 5, 6)
# s = {7, 8, 9}

# f(*a, *t, *s)
def f(a: int, b: int) -> float:
    print(a, b)
    return("salam")


f(1, "2")

a= f(1,"34a")
print(a)
f.__annotations__