from django.db import models

class Parts(models.Model):
    name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    guarantee = models.CharField(max_length=70)
    date = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='parts_images/', blank=True, null=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Parts'

    def __str__(self):
        return f'{self.name} {self.company} {self.date}'