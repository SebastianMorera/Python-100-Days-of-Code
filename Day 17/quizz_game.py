from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


def quiz_game():
    question_bank = []
    for question in question_data:
        question_bank.append(Question(question["text"], question["answer"]))
    quiz = QuizBrain(question_bank)

    while quiz.still_has_questions():
        quiz.next_question()

    print(f"You've completed the quiz! 📝\nYour final score was: {quiz.score}/{quiz.question_number} 🧠")


if __name__ == '__main__':
    quiz_game()
