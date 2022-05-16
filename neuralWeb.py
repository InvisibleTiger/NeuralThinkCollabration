import webbrowser
from googlesearch import search

class NeuralWeb():
    def neuralOpen(command:str):
        for i in search(command, num_results=1):
            webbrowser.open_new(i)