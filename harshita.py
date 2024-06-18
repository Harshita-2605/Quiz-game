import tkinter as tk
from tkinter import messagebox
import random

class QuizApp:
    def __init__(self, master, questions):
        self.master = master
        self.master.title("Quiz Game")

        self.questions = questions
        self.score = 0
        self.current_question_index = 0

        self.label_question = tk.Label(master, text="", font=("Helvetica", 18))
        self.label_question.pack(pady=18)


        self.radio_var = tk.StringVar()
        self.radio_buttons = []
        for i in range(4):
            radio_btn = tk.Radiobutton(master, text="", variable=self.radio_var, value=str(i + 1))
            radio_btn.pack()
            self.radio_buttons.append(radio_btn)

        self.next_button = tk.Button(master, text="Next", command=self.next_question)
        self.next_button.pack(pady=24)

        self.load_question()

    def load_question(self):
        if self.current_question_index < len(self.questions):
            current_question = self.questions[self.current_question_index]
            self.label_question.config(text=current_question["text"])

            for i, option in enumerate(current_question["options"]):
                self.radio_buttons[i].config(text=option, font=("Helvetica", 18))

            self.radio_var.set(" ")  # Clear the selection
        else:
            self.show_result()

    def next_question(self):
        if self.radio_var.get():
            user_answer = int(self.radio_var.get())
            current_question = self.questions[self.current_question_index]

            if current_question["correct_option"] == user_answer:
                self.score += 1

            self.current_question_index += 1
            self.load_question()
        else:
            messagebox.showinfo("Error", "Please select an answer.")

    def show_result(self):
        messagebox.showinfo("Quiz Completed", f"Quiz completed! Your score: {self.score}/{len(self.questions)}")
        self.master.destroy()

def main():
    root = tk.Tk()

    questions = [
        {"text": "What is the capital of France?", "options": ["Berlin", "Paris", "Madrid", "Rome"], "correct_option": 2},
        {"text": "Which programming language is this quiz written in?", "options": ["Java", "Python", "C++", "JavaScript"], "correct_option": 2},
        {"text": "What is the largest mammal?", "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"], "correct_option": 2},
        {"text": "In which year did World War II end?", "options": ["1943", "1945", "1950", "1960"], "correct_option": 2},
        {"text": "Who wrote 'Romeo and Juliet'?", "options": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"], "correct_option": 1},
        {"text": "What is the capital of Japan?", "options": ["Beijing", "Seoul", "Tokyo", "Bangkok"], "correct_option": 3},
        {"text": "Which planet is known as the 'Red Planet'?", "options": ["Venus", "Mars", "Jupiter", "Saturn"], "correct_option": 2},
        {"text": "What is the largest ocean on Earth?", "options": ["Atlantic Ocean", "Indian Ocean", "Southern Ocean", "Pacific Ocean"], "correct_option": 4},
        {"text": "Who is known as the 'Father of Computer Science'?", "options": ["Alan Turing", "Ada Lovelace", "Charles Babbage", "Steve Jobs"], "correct_option": 1},
        {"text": "Which country is known as the 'Land of the Rising Sun'?", "options": ["China", "South Korea", "Japan", "Vietnam"], "correct_option": 3},
        {"text": "What is the square root of 144?", "options": ["10", "11", "12", "13"], "correct_option": 3},
    ]

    app = QuizApp(root, questions)

    root.mainloop()

if __name__ == "__main__":
    main()