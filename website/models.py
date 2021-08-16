from django.db import models
import datetime

now = datetime.datetime.now()

#organizar para enviar por matérias

class Document(models.Model):

    


    
    name = models.CharField(max_length=30)
    materia = models.CharField(max_length=30)
    #docfile = models.FileField(upload_to=f'documents/%Y/%m/%d')

    def generate_path(self, filename):
        url = f'documents/{self.materia}/{now.year}/{filename}'
        return url



    docfile = models.FileField(upload_to=generate_path)
    