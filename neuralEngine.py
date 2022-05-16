import webbrowser
from googlesearch import search

print("IOTA - The best search engine in the planet")

while True:
    query = input("Search iota for ")
    if query == "the best search engine":
        print("Obviously, iota - the one you are on")
    else:
        for i in search(query, num_results=1):
            webbrowser.open_new(i)