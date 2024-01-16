import random
import time
import colorama
from colorama import Fore

colorama.init()

Password_Characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
time.sleep(0.2)
Password_Length = int(input(Fore.LIGHTGREEN_EX + "Parola Uzunluğunu Giriniz: "))
time.sleep(0.2)
Generated_Password = ""
time.sleep(0.2)
for i in range(Password_Length):
    random_char = random.choice(Password_Characters)
    Generated_Password += random_char
time.sleep(0.2)
print(Fore.LIGHTGREEN_EX + "Oluşturulan Parola: ", Generated_Password)
