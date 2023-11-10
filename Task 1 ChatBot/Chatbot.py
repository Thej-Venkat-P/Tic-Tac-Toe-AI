import nltk
from nltk.chat.util import Chat,reflections
Responses=[
    [
        r"my name is (.*)",
        ["Hello %1, How are you ?","Hello %1, How is your Day?"]
    ],
    [   r"hi|hey|hello",
        ["Hello", "Hey","Hi There"]
    ], 
    [
        r"what is your name?",
        ["I am ChatBot!",]
    ],
    [
        r"how are you?",
        ["I'm doing good.\nHow about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind","No Problem"]
    ],
    [
        r"i am fine",
        ["Great to hear that, How can I help you?",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","How can I help you?:)",]
    ],
    [
        r"(.*) age?",
        ["Maybe the Same age as You?",]
    ],
    [
        r"(.*) created?",
        ["Thej Venkat created me using Python's NLTK library ","That's Confidential information now.",]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm always healthy, Thank You for Your concern.",]
    ],
    [
        r"(.*) favourite (sports|game) ?",
        ["Chess",]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Sachin","Dhoni","Kohli"]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["No one in Particular"]
    ],
    [
        r"quit",
        ["Bye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
]
if __name__ == "__main__":
    print("Hi! I am a ChatBot.")
    chat = Chat(Responses, reflections)
    chat.converse()
