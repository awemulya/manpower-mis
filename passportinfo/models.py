from django.db import models


STATUS = [
    ('On Hold', 'On Hold'),
    ('Completed', 'Completed')
]
class PassportInfo(models.Model):
    name = models.CharField(max_length=255)
    passport_no = models.IntegerField()
    reference = models.CharField(max_length=255)
    document = models.FileField(upload_to=f'documents')
    cost = models.IntegerField()
    entry_date = models.DateField()
    status = models.CharField(max_length=255, choices=STATUS)

    def __str__(self):
        return self.name 