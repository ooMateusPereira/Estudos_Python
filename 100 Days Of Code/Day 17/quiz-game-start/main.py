from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Peguei as perguntas e resposta de uma pasta e adicionei em uma variável de fácil acesso.
# Isso é útil quando se trabalha com dados vim da internet em geral.
# Posso acessar facilmente via dic[0].
question_bank = []
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()