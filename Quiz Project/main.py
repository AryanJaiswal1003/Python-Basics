from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
"""TODO-2: write a loop to iterate over question_data. Create a Question object from each entry in question_data 
                & append each question object to the question_bank"""

question_bank = []
for question in question_data:
    ques_text = question["question"]
    ques_ans = question["correct_answer"]
    quiz_main = Question(quiz_question=ques_text , quiz_answer=ques_ans)
    question_bank.append(quiz_main)

#TODO-8: Print the Final Score post completion of Quiz

quiz = QuizBrain(q_list=question_bank)

while quiz.still_has_question():
    quiz.next_question()

if quiz.ques_num == len(question_data):
    print(f"***** Thankyou for Playing the Game. Your Final Score --> {quiz.user_score}/{len(question_data)} *****")