import tkinter as tk
from tkinter import messagebox
import random

# Define quiz questions and answers
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Berlin", "Paris", "Madrid"],
        "correct_answer": "Paris",
    },
    {
        "question": "How many continents are there on Earth?",
        "options": ["4", "5", "6", "7"],
        "correct_answer": "7",
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Mars", "Earth", "Jupiter", "Saturn"],
        "correct_answer": "Jupiter",
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["Au", "Ag", "Ge", "Go"],
        "correct_answer": "Au",
    },
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.score = 0
        self.current_question = 0
        self.shuffle_questions()

        self.question_label = tk.Label(root, text="", font=("Arial", 16))
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(root, text="", font=("Arial", 12), command=lambda i=i: self.check_answer(i))
            button.pack(padx=10, pady=5, fill=tk.X)
            self.option_buttons.append(button)

        self.next_question()

    def shuffle_questions(self):
        random.shuffle(quiz_questions)
        self.current_question = 0

    def next_question(self):
        if self.current_question < len(quiz_questions):
            question = quiz_questions[self.current_question]
            self.question_label.config(text=question["question"])
            options = question["options"]
            random.shuffle(options)
            for i in range(4):
                self.option_buttons[i].config(text=options[i])
            self.current_question += 1
        else:
            self.show_results()

    def check_answer(self, selected_option):
        question = quiz_questions[self.current_question - 1]
        correct_answer = question["correct_answer"]
        selected_answer = self.option_buttons[selected_option]["text"]

        if selected_answer == correct_answer:
            self.score += 1

        if self.current_question < len(quiz_questions):
            self.next_question()
        else:
            self.show_results()

    def show_results(self):
        messagebox.showinfo("Quiz Completed", f"You scored {self.score}/{len(quiz_questions)}")
        self.reset_quiz()

    def reset_quiz(self):
        self.score = 0
        self.shuffle_questions()
        self.next_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
