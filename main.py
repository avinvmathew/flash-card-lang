from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pd.read_csv("./data/french_words.csv")
words_dict = dict(zip(data.iloc[:,0],data.iloc[:,1]))
# print(words_dict.items())
# print(french_words)
#------------------------- UI ---------------------#
french_word = "ola"
english_word = ""
def random_word_pair():
    global french_word
    global english_word
    global word_display
    random_pair = random.choice(list(words_dict.items()))
    french_word = random_pair[0]
    english_word = random_pair[1]
    canvas.delete("ww")
    word_display = canvas.create_text(400, 263, text=f"{french_word}", font=("Ariel", 50, "bold"), tags="ww")


window = Tk()
window.title(string="Flash Card App")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526, highlightthickness=0)
canvas.config(bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)

title_display = canvas.create_text(400, 150, text=f"French", font=("Ariel", 30, "italic"))
word_display = canvas.create_text(400, 263, text=f"{french_word}", font=("Ariel", 50, "bold"), tags="ww")

wrong_button_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, bd=0, command=random_word_pair)
wrong_button.grid(row=1, column=0)

right_button_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0, bd=0, command=random_word_pair)
right_button.grid(row=1, column=1)

window.mainloop()
