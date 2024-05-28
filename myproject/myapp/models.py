from django.db import models

# Create your models here.

class Product(models.Model):
    # when we dlt data to move trashbin not directly delete so set a value to check the status of prdcts
    # when user clicks the dlt button the status must be set to 0/1 
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))
    title=models.CharField(max_length=200)
    price=models.FloatField()
    description=models.TextField()
    image=models.ImageField(upload_to='media/')

    priority=models.IntegerField(default=0)
    # adjust the priority of prdcts based on season
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.title
    

    # This method is used to define how an instance of your class should be represented as a
    #  string when str() is called on it. In your case,
    #  it looks like you want to return the title attribute of the instance




