class QuizBrain:

    def __init__(self, q_list): 
        self.q_number = 0
        self.q_list =  q_list

    def next_question(self):
        current_question = self.q_list[self.q_number]
        self.q_number += 1
        input(f"Q.{current_question}: {current_question.text} (True/False)")