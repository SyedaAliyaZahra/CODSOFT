import tkinter as tk
from tkinter import messagebox

class QuizGUI:
    def __init__(self, root, questions):
        self.root = root
        self.questions = questions
        self.current_question = 0
        self.score = 0
        
        self.question_label = tk.Label(root, text="")
        self.question_label.pack(pady=10)

        self.choice_buttons = []
        for _ in range(4):
            button = tk.Button(root, text="", width=30, command=lambda idx=_: self.check_answer(idx))
            button.pack(pady=5)
            self.choice_buttons.append(button)
        
        self.next_button = tk.Button(root, text="Next Question", command=self.next_question)
        self.next_button.pack(pady=10)
        
        self.update_question()

    def update_question(self):
        question_data = self.questions[self.current_question]
        question_text = question_data['question']
        choices = question_data['choices']

        self.question_label.config(text=question_text)
        for idx, choice in enumerate(choices):
            self.choice_buttons[idx].config(text=choice)

    def check_answer(self, choice):
        correct_answer = self.questions[self.current_question]['answer']
        if choice == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct!", "Your answer is correct.")
        else:
            messagebox.showerror("Incorrect", f"Your answer is incorrect. The correct answer is {correct_answer + 1}.")

    def next_question(self):
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.update_question()
        else:
            self.show_results()

    def show_results(self):
        total_questions = len(self.questions)
        percentage = (self.score / total_questions) * 100

        message = f"Quiz Finished!\nYour Score: {self.score}/{total_questions} ({percentage:.2f}%)\n"
        if percentage == 100:
            message += "Congratulations! You got a perfect score!"
        elif percentage >= 70:
            message += "Great job! You did well."
        else:
            message += "Keep practicing to improve your score."

        messagebox.showinfo("Quiz Results", message)
        self.root.destroy()

def main():
    root = tk.Tk()
    root.title("Quiz Game")

    quiz_questions = [
        {
            'question': 'What is the capital of France?',
            'choices': ['Berlin', 'Madrid', 'Paris', 'Rome'],
            'answer': 2
        },
        {
            'question': 'Who wrote the play "Romeo and Juliet"?',
            'choices': ['William Shakespeare', 'Jane Austen', 'Charles Dickens', 'Leo Tolstoy'],
            'answer': 0
        },
    ]

    quiz_app = QuizGUI(root, quiz_questions)
    root.mainloop()

if __name__ == "__main__":
    main()
