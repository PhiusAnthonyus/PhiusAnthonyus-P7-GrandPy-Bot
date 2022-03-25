from flask import (Flask, render_template, request)
from project import api, parser

app = Flask(__name__)


@app.route('/', methods=['get', 'post'])
def hello():
    return render_template('menu.html')


@app.route('/content', methods=['get', 'post'])
def content():
    form_user_question = parser.Parser(str(request.args.get("userQuestion")))
    form_address = api.ApiGoogleMaps(form_user_question.parser_parser)
    form_content = api.ApiWikipedia(form_user_question.parser_parser)
    return render_template("content.html", map=form_address.api_googlemaps_image,
                           address=form_address.api_googlemaps_content,
                           content=f"{form_content.api_wikipedia_content}",
                           keyword=form_content.api_wikipedia_keyword,
                           user_question_dialogue=form_user_question.parser_user_question, )
