from django.db import models


class Author(models.Model):
    name = models.CharField()
    fk_target = models.PositiveIntegerField(null=True, blank=True, unique=True)


class Book(models.Model):
    name = models.CharField()
    author = models.ForeignKey(
        to=Author, to_field="fk_target", on_delete=models.CASCADE, null=True
    )
