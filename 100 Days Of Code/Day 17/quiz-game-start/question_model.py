class Question:

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
        
quest_1 = Question('texto', 'resposta')

print(quest_1.text, quest_1.answer)