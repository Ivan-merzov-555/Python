import eel

eel.init("web")

eel.start("main.html", size=(700, 700))

@eel.expose
beh = input("как настроение?")

@eel.expose
if beh == "Хорошо":
    print("Ну и ладно!")