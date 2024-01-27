from random import shuffle
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

print("""
  __   _  _  __  ____     ___   __   _  _  ____ 
 /  \ / )( \(  )/ ___)   / __) / _\ ( \/ )(  __)
(  O )) \/ ( )( \___ \  ( (_ \/    \/ \/ \ ) _) 
 \__\)\____/(__)(____/   \___/\_/\_/\_)(_/(____)
""")

shuffle(question_data)
question_bank = []

for i in range(0, len(question_data)):
    question_bank.append(Question(question_data[i]['text'], question_data[i]['answer']))

quiz = QuizBrain(question_bank)
quiz.next_question()