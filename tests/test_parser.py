from project import parser

question = parser.Parser("Quelle est l'adresse d'OpenClassrooms ?")


def test_parser_question():
    assert question.parser_user_question == "Quelle est l'adresse d'OpenClassrooms ?"


def test_parser_result():
    assert question.parser_parser == "OpenClassrooms"
