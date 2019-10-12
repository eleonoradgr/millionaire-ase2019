from flakon import JsonBlueprint
from flask import request, jsonify, abort
from myservice.classes.quiz import Quiz, Question, Answer, NonExistingAnswerError, LostQuizError, CompletedQuizError

quizzes = JsonBlueprint('quizzes', __name__)

_LOADED_QUIZZES = {}  # list of available quizzes
_QUIZNUMBER = 0  # index of the last created quizzes


# TODO: complete the decoration
@quizzes.route("/quizzes")
def all_quizzes():
    if 'POST' == request.method:
        # TODO: Create new quiz 
    elif 'GET' == request.method:
        # TODO: Retrieve all loaded quizzes

    return result

# TODO: complete the decoration
@quizzes.route("/quizzes/loaded", methods=['GET'])
def loaded_quizzes():  # returns the number of quizzes currently loaded in the system
    return # TODO: Return the correct number


# TODO: complete the decoration
@quizzes.route("/quiz/<id>")
def single_quiz(id):
    global _LOADED_QUIZZES
    result = ""

    # TODO: check if the quiz is an existing one

    if 'GET' == request.method:  
        # TODO: retrieve a quiz <id>
       

    elif 'DELETE' == request.method:
        # TODO: delete a quiz and get back number of answered questions
        # and total number of questions

    return result


# TODO: complete the decoration
@quizzes.route("/quiz/<id>/question", methods=['GET'])
def play_quiz(id):
    global _LOADED_QUIZZES
    result = ""

    # TODO: check if the quiz is an existing one

    if 'GET' == request.method:  
        # TODO: retrieve next question in a quiz, handle exceptions

    return result


# TODO: complete the decoration
@quizzes.route("/quiz/<id>/question/<answer>", methods=['PUT'])
def answer_question(id, answer):
    global _LOADED_QUIZZES
    result = ""
    # TODO: check if the quiz is an existing one
    quiz = _LOADED_QUIZZES[id]
    
    # TODO: check if quiz is lost or completed and act consequently

    if 'PUT' == request.method:  

        # TODO: Check answers and handle exceptions 

        return jsonify({'msg': result})

############################################
# USEFUL FUNCTIONS BELOW (use them, don't change them)
############################################

def create_quiz(request):
    global _LOADED_QUIZZES, _QUIZNUMBER

    json_data = request.get_json()
    qs = json_data['questions']
    questions = []
    for q in qs:
        question = q['question']
        answers = []
        for a in q['answers']:
            answers.append(Answer(a['answer'], a['correct']))
        question = Question(question, answers)
        questions.append(question)

    _LOADED_QUIZZES[str(_QUIZNUMBER)] = Quiz(_QUIZNUMBER, questions)
    _QUIZNUMBER += 1

    return jsonify({'quiznumber': _QUIZNUMBER - 1})


def get_all_quizzes(request):
    global _LOADED_QUIZZES

    return jsonify(loadedquizzes=[e.serialize() for e in _LOADED_QUIZZES.values()])


def exists_quiz(id):
    if int(id) > _QUIZNUMBER:
        abort(404)  # error 404: Not Found, i.e. wrong URL, resource does not exist
    elif not(id in _LOADED_QUIZZES):
        abort(410)  # error 410: Gone, i.e. it existed but it's not there anymore
