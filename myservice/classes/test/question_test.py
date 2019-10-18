from myservice.classes.quiz import Answer
from myservice.classes.quiz import Question 
import unittest

class QuestionQuiz(unittest.TestCase):
    def test_isCompleted(self):
        answer_1 = Answer("la prima", 1)
        answer_2 = Answer("la seconda")
        question = Question("Buona?",  [answer_1, answer_2] )
        self.assertEqual(question.checkAnswer("la prima"), True)
    
if __name__ == '__main__':
    unittest.main()
