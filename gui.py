import tkinter as tk
import html
from main import get_question

window = tk.Tk()
window.title("Trivia Quiz")
window.geometry("500x450")
window.config(bg="#F4F1EA")

questions = get_question()
question_number = 0
current_question = questions[question_number]
clean_question = html.unescape(current_question["question"])
score = 0

def check_answer(answer):
    global score
    global question_number
    if answer == current_question["correct_answer"]:
        print("Correct")
        score += 1
    else:
        print("Incorrect")
    question_number += 1


    score_label.config(text=f"Score: {score}/10")

    if question_number < len(questions):
        next_question()
    else:
        true_button.unbind("<Button-1>")
        false_button.unbind("<Button-1>")
        main_text.config(text=f"Quiz finished! Your score: {score}/10")
        play_again_button.grid()

def next_question():
    global question_number
    global current_question
    current_question = questions[question_number]
    clean_question = html.unescape(current_question["question"])
    main_text.config(text=clean_question)

def play_again():
    global question_number
    global score
    global questions

    questions = get_question()
    question_number = 0
    score = 0

    true_button.bind("<Button-1>", lambda event: check_answer("True"))
    false_button.bind("<Button-1>", lambda event: check_answer("False"))

    score_label.config(text=f"Score: {score}/10")

    next_question()
    play_again_button.grid_remove()

title = tk.Label(window, text="TRUE / FALSE QUIZ", font=("Arial", 20), bg="#F4F1EA",
fg="#26344A")
title.grid(row=0, column=0, padx=20, pady=20)
main_text = tk.Label(
    window,
    text=clean_question,
    font=("Arial", 16),
    bg="#FFFFFF",
    fg="#26344A",
    wraplength=450,
    padx=25,
    pady=35,
    justify="center"
)
main_text.grid(row=1, column=0, columnspan=2, padx=20, pady=30)

true_button = tk.Label(
    window,
    text="TRUE",
    bg="#418966",
    fg="white",
    font=("Arial", 14, "bold"),
    width=12,
    height=2,
    cursor="hand2"
)
true_button.grid(row=2, column=0, padx=10, pady=20)
true_button.bind("<Button-1>", lambda event: check_answer("True"))
false_button = tk.Label(
    window,
    text="FALSE",
    bg="#C85B5B",
    fg="white",
    font=("Arial", 14, "bold"),
    width=12,
    height=2,
    cursor="hand2"
)
false_button.grid(row=2, column=1, padx=10, pady=20)
false_button.bind("<Button-1>", lambda event: check_answer("False"))

play_again_button = tk.Button(
    window,
    text="Play Again",
    command=play_again,
    bg="#26344A",
    fg="white",
    font=("Arial", 13, "bold"),
    width=15,
    pady=10,
    relief="flat",
    cursor="hand2"
)
play_again_button.grid(row=3, column=0, columnspan=2, pady=20)
play_again_button.grid_remove()

score_label = tk.Label(
    window,
    text=f"Score: {score}/10",
    font=("Arial", 15, "bold"),
    bg="#F4F1EA",
    fg="black"
)
score_label.grid(row=0, column=1, padx=20, pady=20)







window.mainloop()