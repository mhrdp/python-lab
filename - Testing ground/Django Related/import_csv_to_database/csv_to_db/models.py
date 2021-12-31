from django.db import models

# Create your models here.
class ImportViaShell(models.Model):
    team_name = models.CharField(max_length=100)
    prize = models.CharField(max_length=100)

    def __str__(self):
        return self.team_name

class ImportViaDjangoImportExportDependencies(models.Model):
    team_name = models.CharField(max_length=100)
    prize = models.CharField(max_length=100)

    def __str__(self):
        return self.team_name
