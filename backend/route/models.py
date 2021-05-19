from django.db import models


class Route(models.Model):
    id = models.AutoField(primary_key=True)
    route_name = models.CharField(max_length=60, default='')

    def __str__(self):
        return self.route_name
