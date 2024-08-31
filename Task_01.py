import tkinter as tk
from tkinter import messagebox
import tkinter.font as font

# Sample questions for different difficulty levels
QUIZ_DATA = {
    'EASY': [
        {'question': 'Which of these data types does \n Python not natively support?', 'options': ['Lists', 'Tuples', 'Arrays', 'Dictionaries'], 'answer': 'Arrays'},
        {'question': 'Which of the following character\n is used to give single-line comments in Python?', 'options': [' //', '#', ' !', ' /*'], 'answer': '#'},
        {'question': 'What does the sep parameter do \n in the print() function?', 'options': ['Separates lines', 'Specifies separator values', 'Separates syntax errors', 'None of these'], 'answer': 'Specifies separator values'}
    ],
    'MEDIUM': [
        {'question': 'Which of the following types of \n loops are not supported in Python?', 'options': ['for', 'while', 'do-while', 'None of above'], 'answer': 'do-while'},
        {'question': 'Python supports the creation of  anonymous \n  functions at runtime, using a construct called ', 'options': [' pi', 'lambda', ' anonymous', ' none of the mentioned'], 'answer': 'lambda'},
        {'question': ' What does pip stand for python?', 'options': ['Preferred Installer Program', ' Pip Installs Python', ' Pip Installs Packages', 'All of the mentioned'], 'answer': 'Preferred Installer Program'}
    ],
    'HARD': [
        {'question': 'The method to extract the last element of a list is', 'options': ['List_name[2:3]', 'List_name[0]', 'List_name[-1]', 'None of the above'], 'answer': 'List_name[-1]'},
        {'question': 'What will be the output of the \n following code snippet? \n\n s = {1, 2, 3, 3, 2, 4, 5, 5}\n print(s)', 'options': ['{1,2,3,3,2,4,5,5}', '{1,2,3,4,5}', 'Error', 'None of the above'], 'answer': '{1,2,3,4,5}'},
        {'question': 'What will be the result of the \n following expression in Python? \n\n “2 ** 3 + 5 ** 2”', 'options': ['65536', '33', '169', 'None of the above'], 'answer': '33'}
    ]
}

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("400x600")
        self.root.configure(bg='indigo')  # Set background color
        
        # Game variables
        self.score = 0
        self.current_question = 0
        self.difficulty = tk.StringVar(value="EASY")

        # Widgets
        self.create_widgets()
        self.load_question()
        

    def create_widgets(self):
        tk.Label(self.root, text="QUIZ GAME", font=("math sans blod italic", 24), bg='white').pack(pady=10)
        # Bold font for the label
        bold_font = font.Font(weight="bold")

        # Custom font for question text
        question_font = font.Font(family="Century Gothic", size=13, weight="bold")
        option_font = font.Font(family="Century Gothic", size=10)

        # Highlighted Label
        option_menu = tk.OptionMenu(self.root, self.difficulty, "EASY", "MEDIUM", "HARD")
        option_menu.config(font=("Georgia", 12), bg='lightgrey')
        option_menu.pack(pady=10)

        self.start_button = tk.Button(self.root, text="Let's Start ", command=self.start_quiz, font=("Showcard Gothic", 11), bg='lightgrey')
        self.start_button.pack(pady=10)


        self.question_label = tk.Label(self.root, text="", font=question_font,  bg="lightblue")
        self.question_label.pack(pady=20)

        self.options = []
        for _ in range(4):
            option = tk.Button(self.root, text="", width=20, command=lambda i=_: self.check_answer(i))
            option.config(font=option_font)
            option.pack(pady=5)
            self.options.append(option)

        self.score_label = tk.Label(self.root, text="Score: 0", font=("Eras Bold ITC", 12, "bold"), bg='lightblue')
        self.score_label.pack(pady=20)

    def start_quiz(self):
        self.score = 0
        self.current_question = 0
        self.update_score()
        self.load_question()

    def load_question(self):
        questions = QUIZ_DATA[self.difficulty.get()]
        question_data = questions[self.current_question]

        self.question_label.config(text=question_data['question'])
        for i, option in enumerate(self.options):
            option.config(text=question_data['options'][i])

    def check_answer(self, selected_option):
        questions = QUIZ_DATA[self.difficulty.get()]
        correct_answer = questions[self.current_question]['answer']

        if self.options[selected_option].cget("text") == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct!", "Well done!")
        else:
            messagebox.showerror("Incorrect!", f"The correct answer was: {correct_answer}")

        self.update_score()
        self.current_question += 1

        if self.current_question < len(questions):
            self.load_question()
        else:
            messagebox.showinfo("Quiz Over", f"Your final score is: {self.score}")
            self.start_button.config(state=tk.NORMAL)

    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}")


if __name__ == "__main__":
    root = tk.Tk()
    game = QuizGame(root)
    root.mainloop()
