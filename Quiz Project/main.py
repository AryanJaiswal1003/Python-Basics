from data import question_data
from question_model import Question

for question in question_data:
    question_bank = []
    ques_text = question_data["text"]
    ques_ans = question_data["answer"]
    ques_final = Question(ques_text , ques_ans)
    question_bank.append(ques_final)

print(question_bank[1])