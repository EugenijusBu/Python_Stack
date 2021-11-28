from stack import Stack

def reversed(text_to_reverse):

    s = Stack()

    reversed_string = ""

    for i in range(len(text_to_reverse)):
        s.push(text_to_reverse[i])

    for i in range(len(text_to_reverse)):
        reversed_string = reversed_string + s.pop()

    return reversed_string



print(reversed("!sujineguE si emaN ym olleH"))