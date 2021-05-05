from django.db import models

class Poll(models.Model):
    title = models.CharField(max_length=4096)
    subtitle = models.CharField(max_length=4096)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_questions(self):
        return Question.objects.filter(poll=self)

class QuestionType():
    QUESTION_TYPE = (
        (0, 'text'),
        (1, 'single'),
        (2, 'multiple'),
    )
    TEXT = 0
    SINGLE = 1
    MULTIPLE = 2

class Question(QuestionType, models.Model):
    poll = models.ForeignKey('Poll', on_delete=models.CASCADE)
    title = models.CharField(max_length=4096)
    type = models.IntegerField(choices=QuestionType.QUESTION_TYPE, default=QuestionType.TEXT)

    def __str__(self):
        return self.title

    def get_choices(self):
        return Choice.objects.filter(question=self)

class Choice(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    title = models.CharField(max_length=4096)

    def __str__(self):
        return self.title

class Answer(models.Model):
    poll = models.ForeignKey('Poll', on_delete=models.CASCADE)
    user_name = models.CharField(max_length=4096)

    def __str__(self):
        return f'{self.poll}_{self.user_name}'

    def get_answerquestions(self):
        return AnswerQuestion.objects.filter(answer=self)

class AnswerQuestion(models.Model):
    answer = models.ForeignKey('Answer', on_delete=models.CASCADE)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    text = models.CharField(max_length=4096, blank=True)

    def get_choices(self):
        choices = Choice.objects.filter(question=self.question)
        choices_1 = [e.choice for e in AnswerChoice.objects.filter(answerquestion=self)]
        return [(e, e in choices_1) for e in choices]


class AnswerChoice(models.Model):
    answerquestion = models.ForeignKey('AnswerQuestion', on_delete=models.CASCADE)
    choice = models.ForeignKey('Choice', on_delete=models.CASCADE)



# Create your models here.
