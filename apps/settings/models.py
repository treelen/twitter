from django.db import models

# Create your models here.
class Settings(models.Model):
    title=models.CharField(
        max_length=20
    )
    logo=models.ImageField(
        upload_to='logo/'
    )
    number=models.CharField(
        max_length=18
    )
    email=models.EmailField(
        max_length=25
    )
    twiiter=models.URLField(
       
    )
    facebook=models.URLField(
        
    )
    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name='настройка'
        verbose_name_plural='настройки'
        

