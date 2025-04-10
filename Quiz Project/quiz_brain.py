# TODO-3: Asking the Question. Check if the answer was correct. Checking if we're the end of the quiz

#create a class called QuizBrain --> write an __init()__ method --> initialize the question_number = 0 -->
    #initialize the question_list to an input

class QuizBrain:
    def __init__(self , q_list):
        self.ques_num = 0
        self.ques_list = q_list
        self.user_score = 0

#TODO-4: Create a new method next_question which would get hold of current question from question_list. Use the input()
    #TODO-4: function to show the user the Question text and ask for the user's answer

    def next_question(self):
        current_ques = self.ques_list[self.ques_num]
        self.ques_num += 1
        user_input = input(f"Q.{self.ques_num}: {current_ques.text} [True / False] --> ") #important to add current_ques.text
        self.check_answer(user_input , current_ques.answer)

#TODO-5: Create method called still_has_question() --> Return a boolean based on value of question_number
    # TODO-5: use the while loop to show the next question until the end

    def still_has_question(self):
        if self.ques_num < len(self.ques_list):
            return True
        else:
            return False

    #simplified way --> return self.ques_num < len(self.ques_list)

#TODO-6: Create a new method check_answer(), that compares user_input & correct answer & continues to next ques
#TODO-7: Add a new attribute score to keep a track of the user_score

    def check_answer(self , user_input, check_ans):
        if user_input.lower() == check_ans.lower():
            self.user_score += 1
            print("Congratulation, You are Right!!!")
        else:
            print("Sorry, You answered it Incorrectly!!!")
        print(f"The Correct Answer is --> {check_ans}")
        print(f"Your Current Score is --> {self.user_score}/{self.ques_num}")
        print("\n")
