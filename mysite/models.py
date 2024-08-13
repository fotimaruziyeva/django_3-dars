from django.db import models


class Team(models.Model):
    image = models.ImageField(upload_to='Images/blog')
    name = models.CharField(max_length=80)
    jobs=models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return f"{self.name}  {self.jobs}"