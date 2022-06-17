from project import lists


class Parser:
    "Cette classe filtre la question à partir d'une liste de mots."
    def __init__(self, question: str):
        self.parser_user_question = question
        self.parser_parser = self.parser()

    def parser(self) -> str:
        form = self.parser_user_question
        result = []
        for char in form:
            if char in lists.list_char:
                form = form.replace(char, " ")
        for keyword in form.split():
            if keyword.lower() not in lists.list_words:
                result.append(keyword)
        result = " ".join(result)
        result = result.replace(" ", "_")
        print(result)
        return result


if __name__ == "__main__":
    parser1 = Parser("Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?")
    print(parser1.parser_user_question)
    print(parser1.parser_parser)
    print(type(parser1.parser_parser))
