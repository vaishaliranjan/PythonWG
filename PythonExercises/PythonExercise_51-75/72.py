import webbrowser

query=input("Enter a query: ")

webbrowser.open("https://google.com/search?q={}".format(query))
