from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
class QuizInterface:
    def __init__(self,quiz_brain : QuizBrain):
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(pady=20,padx=20,background=THEME_COLOR)
        self.quiz = quiz_brain
        self.score_board()
        self.question_box()
        self.right_buttons()
        self.wrong_buttons()
        self.get_next_question()
        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():

            self.score.config(text=f"Score:{self.quiz.score}")
            next_question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=next_question_text)

        else:
            self.canvas.itemconfig(self.text ,text="You've reached the end")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def question_box(self):
        self.canvas = Canvas(height=250,width=300,background="white")
        self.text = self.canvas.create_text(150,125,width=280, text="hello",font=("Arial",20,"italic"))

        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

    def right_buttons(self):
        self.rightimg = PhotoImage(file="images/true.png")
        self.right_button = Button(image=self.rightimg,height=100,
                                   width=100,highlightthickness=0,command=self.true_pressed)
        self.right_button.grid(row=2,column=0)

    def wrong_buttons(self):
        self.wrongimg = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=self.wrongimg,height=100,
                                   width=100,highlightthickness=0,command=self.wrong_pressed)
        self.wrong_button.grid(row=2,column=1)

    def score_board(self):
        self.score = Label(text=f"Score: ",background=THEME_COLOR,font=("Arial",20,"bold"),foreground="white")
        self.score.grid(row = 0,column =1)

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def wrong_pressed(self):
        wrong = self.quiz.check_answer("False")
        self.give_feedback(wrong)


    def give_feedback(self,answer:bool):
        if answer:
            self.canvas.config(background="green")

        else:
            self.canvas.config(background="red")

        self.window.after(1000,self.get_next_question)