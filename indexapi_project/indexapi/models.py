from django.db import models

class Index(models.Model):
    name = models.CharField(max_length=255, unique=True)
    csv_file = models.FileField(upload_to='csv_files/')

class DailyPrice(models.Model):
    index = models.ForeignKey(Index, on_delete=models.CASCADE, related_name='daily_prices')
    date = models.DateField()
    open_price = models.FloatField()
    high_price = models.FloatField()
    low_price = models.FloatField()
    close_price = models.FloatField()
    shares_traded = models.FloatField()
    turnover = models.FloatField()
