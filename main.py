from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pd.read_csv("./data/french_words_temp.csv")
words_dict = dict(zip(data.iloc[:,0],data.iloc[:,1]))

#------------------------- UI ---------------------#
#global vars
english_word = ""
french_word = ""

def flip_card(english_word):
    file_path2 = "./images/card_back.png"
    card_back = PhotoImage(file=file_path2)
    canvas.itemconfig(card, image=card_back)
    canvas.card_back_ref = card_back  # reference to prevent garbage collection

    canvas.itemconfig(title_display, text=f"English", fill="white")
    canvas.itemconfig(word_display, text=f"{english_word}", fill="white")

def random_word_pair():
    global flip_timer, english_word, random_pair, french_word
    window.after_cancel(flip_timer)
    random_pair = random.choice(list(words_dict.items()))
    french_word = random_pair[0]
    english_word = random_pair[1]

    file_path = "./images/card_front.png"
    card_front = PhotoImage(file=file_path)
    canvas.itemconfig(card, image=card_front)
    canvas.card_front_ref = card_front

    canvas.itemconfig(title_display, text=f"French", fill="black")
    canvas.itemconfig(word_display, text = f"{french_word}", fill="black")
    flip_timer = window.after(3000, lambda w=english_word:flip_card(w))    #don't worry about ide warning

def if_right():
    global data
    data = data[data["French"] != french_word]
    data.to_csv("./data/french_words_temp.csv", index=False)
    word = words_dict.pop(french_word)
    # print(f"You know {word}")
    # print(len(words_dict))
    random_word_pair()

window = Tk()
window.title(string="Flash Card App")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526, highlightthickness=0)
canvas.config(bg=BACKGROUND_COLOR)
card = canvas.create_image(400, 263)
canvas.grid(row=0, column=0, columnspan=2)

title_display = canvas.create_text(400, 150, text=f"Title", font=("Ariel", 30, "italic"))
word_display = canvas.create_text(400, 263, text=f"Word", font=("Ariel", 50, "bold"))

wrong_button_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, bd=0, command=random_word_pair)
wrong_button.grid(row=1, column=0)

right_button_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0, bd=0, command=if_right)
right_button.grid(row=1, column=1)

flip_timer = window.after(3000, lambda w=english_word:flip_card(w))
random_word_pair()


window.mainloop()
