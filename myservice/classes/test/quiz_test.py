from myservice.classes.quiz import Answer
from myservice.classes.quiz import Question 
from myservice.classes.quiz import Quiz
import unittest

class TestQuiz(unittest.TestCase):
    def test_isCompleted(self):
        answer_1 = Answer("la prima", 1)
        answer_2 = Answer("la seconda")
        question = Question("Buona?",  [answer_1, answer_2] )
        quiz = Quiz( 1, [question])
        self.assertEqual(quiz.isCompleted(), False)
    def test_isLost(self):
        answer_1 = Answer("la prima", 1)
        answer_2 = Answer("la seconda")
        question = Question("Buona?",  [answer_1, answer_2] )
        quiz = Quiz( 1, [question])
        self.assertEqual(quiz.isLost(), False)


        

if __name__ == '__main__':
    unittest.main()
