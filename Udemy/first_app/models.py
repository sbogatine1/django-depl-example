from django.db import models

# Create your models here.
class topics(models.Model):
    top_name = models.CharField(max_length = 264, unique=True)

    def __str__(self):
        return self.top_name

class webPage(models.Model):
    topic = models.ForeignKey(topics, on_delete=models.CASCADE)
    name = models.CharField(max_length=264, unique=True)
    url = models. URLField(unique=True)

    def __str__(self):
        return self.name

class accessRecord(models.Model):
    name = models.ForeignKey(webPage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)
