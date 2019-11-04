from django_nameko_standalone import DjangoModels
from nameko.events import event_handler
from nameko.rpc import rpc


class NamekoService:
    name = "nameko_service"
    models = DjangoModels()

    @rpc
    def search(self, search_text):
        from polls.models import Question
        question = Question.objects.filter(question_text=search_text).first()
        if not question:
            return f"Question {search_text} is not found"
        else:
            return f"Question {question.question_text} is found. Date: {question.pub_date}"

    @event_handler('ipms', 'import')
    def imps_import(self, search_text):
        from polls.models import Question
        question = Question.objects.filter(question_text=search_text).first()
        if not question:
            print(f"Question {search_text} is not found")
        else:
            print(f"Question {question.question_text} is found. Date: {question.pub_date}")
