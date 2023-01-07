# https://betterprogramming.pub/django-annotations-and-aggregations-48685994d149
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return "Choice: {}, Question:{}".format(self.choice_text, self.question.question_text)

# Number of questions
# Number of choices
# Number of choices per question
# Number of choices per question after filtering on question_text
# Number of votes per question
# Questions with a maximum number of votes
# Questions with a minimum number of votes
# Questions with no choices
# Total number of votes cast
# Average votes per choice
# Average votes per question
# Number of questions per question_text
# Number of choices per question_text