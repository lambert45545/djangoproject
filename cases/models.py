from django.db import models

# Create your models here.
choices=(('H','homme'),('F','femme'))
casechaoice=(
             ('op','open'),
             ('cl','closed'),
             ('ong','on going')
             )
class Client(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    phone = models.CharField(max_length=100)
    gender = models.CharField(max_length=100,choices=choices)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Lawyer(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    phone = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Cases(models.Model):
    title = models.CharField(max_length=100)
    description=models.TextField()
    statue=models.CharField(max_length=10,choices=casechaoice,default='op')
    lawyer=models.ForeignKey(Lawyer,on_delete=models.CASCADE)
    client=models.ForeignKey(Client,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    upadate_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return  self.title





