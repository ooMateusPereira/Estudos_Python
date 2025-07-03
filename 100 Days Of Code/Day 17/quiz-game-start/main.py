from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Peguei as perguntas e resposta de um arquivo (data.py) e adicionei em uma variável de fácil acesso.
# Isso é útil quando se trabalha com dados vindos da internet em geral.
# Posso acessar facilmente via dicionário.
question_bank = []
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions:
    quiz.next_question()

print("You've completed the quiz!")