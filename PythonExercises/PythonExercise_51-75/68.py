d = dict(weather = "clima", earth = "terra", rain = "chuva")
user_input= input("Enter a word: ").lower()
try:
    print(d[user_input])
except KeyError:
    print("No such word")