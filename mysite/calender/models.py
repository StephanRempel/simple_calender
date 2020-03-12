from django.db import models

# Create your models here.
class Events(models.Model):
    # PLAYER_CHOICES =( 
    #     ("1", "OE"), 
    #     ("2", "KR"), 
    #     ("3", "ZM"), 
    #     ("4", "VS"), 
    #     ("5", "SR"), 
    #     ("6", "GH"), 
    # ) 
    # geeks_field = forms.MultipleChoiceField(choices = PLAYER_CHOICES ) 
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    # start = models.CharField(max_length=55,null=False,blank=True)
    # end = models.CharField(max_length=55,null=False,blank=True)
    start = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.name

