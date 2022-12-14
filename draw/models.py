from django.db import models
from lottery.models import Schedule, Icon

# Create your models here.
class Draw(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    #
    timestamp = models.DateTimeField(auto_now_add=True)
    #
    class Meta:
        db_table = 'draw'
    #
    def __str__(self): return '%s - Date: %s' % (self.schedule, self.date,)

class DrawResult(models.Model):
    draw = models.ForeignKey(Draw, on_delete=models.CASCADE)
    icon = models.ForeignKey(Icon, on_delete=models.CASCADE)
    #
    timestamp = models.DateTimeField(auto_now_add=True)
    #
    class Meta:
        db_table = 'draw_result'
        verbose_name = 'Draw Result'
    #
    def __str__(self): return '%s - Result: %s' % (self.draw, self.icon.name)