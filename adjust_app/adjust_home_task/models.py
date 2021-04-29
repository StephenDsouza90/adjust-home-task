from django.db import models


class PerformanceMetrics(models.Model):
    """ Represents the Performance Metrics data """

    date = models.DateField(blank=True)
    channel = models.CharField(max_length=64, null=True)
    country = models.CharField(max_length=2, null=True)
    operating_system = models.CharField(max_length=10, null=True)
    impressions = models.IntegerField(null=True)
    clicks = models.IntegerField(null=True)
    installs = models.IntegerField(null=True)
    spend = models.FloatField(null=True)
    revenue = models.FloatField(null=True)

    class Meta:
        db_table = "performance_metrics"
