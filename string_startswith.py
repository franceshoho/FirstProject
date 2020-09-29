def what_to_do(instructions):
    phrase = "Simon says"
    length = len(phrase)
    index = instructions.find(phrase)
    if index == -1:
        print("I won't do it!")
    elif instructions.startswith(phrase):
        string = instructions[length+1:]
        print("I "+string)
    elif instructions.endswith(phrase):
        string = instructions[:-(length+1)]
        print("I "+string)

what_to_do("make a wish Simon says")
what_to_do("Simon says make dinner!")
# what_to_do("Move right")