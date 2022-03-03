from django.db import models


# transactions model that stores details of every transactions
class transactions(models.Model):
    toemail = models.EmailField()
    toname = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
