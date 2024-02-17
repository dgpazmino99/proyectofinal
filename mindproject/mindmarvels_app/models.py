from django.db import models


# Create your models here.
class Board(models.Model):
    name = models.CharField(max_length=100)

class Column(models.Model):
    name = models.CharField(max_length=100)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    column = models.ForeignKey(Column, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=(('todo', 'To Do'), ('doing', 'Doing'), ('done', 'Done')))