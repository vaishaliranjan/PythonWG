d = dict(weather = "clima", earth = "terra", rain = "chuva")
user_input= input("Enter a word: ")
try:
    print(d[user_input])
except:
    print("No such word")