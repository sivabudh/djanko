from django_nameko_standalone import DjangoModels
from nameko.rpc import rpc


class NamekoService:
    name = "nameko_service"
    models = DjangoModels()  # Inject the django model dependency

    @rpc
    def search(self, search_text):
        from polls.models import Question
        question = Question.objects.filter(question_text=search_text).first()
        if not question:
            return f"Question {search_text} is not found"
        else:
            return f"Question {question.question_text} is found. Date: {question.pub_date}"
