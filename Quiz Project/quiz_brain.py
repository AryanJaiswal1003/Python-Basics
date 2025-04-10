#TODO-1: Asking the Question.
#TODO-1: checking if the answer was correct
#TODO-1: checking if we're the end of the quiz

"""create a class called QuizBrain
write an __init() method
initialize the question_number = 0
initialize the question_list to an input"""

from main import question_bank

class QuizBrain:
    def __init__(self):
        self.q_num = 0
        
print(question_bank[0])