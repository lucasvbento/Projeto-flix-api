from django.db import models


NATIONALITY_CHOICES = (
    ('USA', 'Estados Unidos'),
    ('Brazil', 'Brasil'),
    ('UK', 'Reino Unido'),
    ('ISRAEL', 'Israel'),
    ('AUSTRALIA', 'Austrália'),
    ('SOUTH_AFRICA', 'África do Sul'),
    ('CANADA', 'Canadá'),
    ('IRELAND', 'Irlanda'),
    ('MEXICO', 'México'),
    ('SPAIN', 'Espanha'),
    ('KENYA', 'Quênia'),
)



class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=100, choices=NATIONALITY_CHOICES, blank=True, null=True)


    def __str__(self):
        return self.name
