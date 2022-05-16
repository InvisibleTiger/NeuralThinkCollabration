import pyjokes
from neuralAI import NeuralThink
from neuralTodo import NeuralToDo, Item
from neuralWeather import NeuralWeather
from randfacts import randfacts
from datetime import datetime
from neuralWeb import NeuralWeb

iota = NeuralThink()
todo = NeuralToDo()

def neuralFacts():
    fact = randfacts.get_fact()
    print(fact)
    iota.neuralSay(fact)

def neuralJoke():
    funny = pyjokes.get_joke()
    print(funny)
    iota.neuralSay(funny)

def neuralAdd_todo()->bool:
    item = Item()
    iota.say("Tell me what to add to the list")
    try:
        item.title = iota.listen()
        todo.neuralNew_item(item)
        message = "Added " + item.title
        iota.neuralSay(message)
        return True
    except:
        print("Oops there was an error")
        return False

def neuralList_todos():
    if len(todo) > 0:
        iota.neuralSay("Here are your todos")
        for item in todo:
            iota.say(item.title)
    else:
        iota.say("The list is empty")

def neuralWeather():
    myweather = NeuralWeather()
    forecast = myweather.forecast
    print(forecast)
    iota.neuralSay(forecast)

def neuralRemove_todo()->bool:
    iota.say("Tell me which item to remove")
    try:
        item_title = iota.neuralListen()
        todo.neuralRemove_item(title=item_title)
        message = "Removed " + item_title
        iota.neuralSay(message)
        return True
    except:
        print("Oops there was an error")
        return False

command = ""
iota.neuralSay("Hey there, I am IOTA your assistant")
while True and command != "goodbye":
    try:
        command = iota.listen()
        command = command.lower()
    except:
        print("oops there was an error")
        command = ""
    print("Command was", command)

    if command == "tell me a joke":
        neuralJoke()
        command = ""
    if command in ["add to-do", "add to do", "add item"]:
        neuralAdd_todo()
        command = ""
    if command in ["list todos", "list todo", "list to-do", "list to do's", "list items"]:
        neuralList_todos()
        command = ""
    if command in ["remove todo", "remove item", "mark done", "remove todos", "remove to-do", "remove to do's"]:
        neuralRemove_todo()
    if command in ["what is the weather like", "give me the forecast", "what is the weather"]:
        neuralWeather()
    if command in ["tell me a fact", "tell me something"]:
        neuralFacts()
    if command in ["good morning", "good evening", "good night"]:
        now = datetime.now()
        hr = now.hour
        if hr <= 0 <= 12:
            message= "Morning"
        if hr >= 12 <= 17:
            message = "Afternoon"
        if hr >= 17 <= 21:
            message = "Evening"
        if hr > 21:
            message = "Night"

        message = "Good" + message + "User"
        iota.neuralSay(message)
        neuralWeather()
        neuralList_todos()
        neuralJoke()
        neuralFacts()
    if command in ["browse"]:
        iota.neuralSay("Browse what")
        site = iota.neuralListen()
        NeuralWeb.neuralOpen(site)

iota.neuralSay("Goodbye, I'm going to sleep now")