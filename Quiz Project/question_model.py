class Question:
    def __init__(self , q_text , q_answer):
        self.text = q_text
        self.answer = q_answer



from data import question_data
import random

for question in question_data:
    question_bank = []
    a = random.randint(0 , 11)
    ques = question_data[a]["text"]
    ques_ans = question_data[a]["answer"]
    
    ques_final = Question(q_text=ques , q_answer=ques_ans)
    
    question_bank.append(ques_final)

print(question_bank)