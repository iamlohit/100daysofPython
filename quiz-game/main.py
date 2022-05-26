from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = list()

for question in question_data:
    q_text = question["question"]
    q_ans = question["correct_answer"]
    new_q = Question(q_text,q_ans)
    question_bank.append(new_q)

new_quiz = QuizBrain(question_bank)
while new_quiz.still_has_question():
    new_quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {new_quiz.score}/{len(new_quiz.question_list)}")