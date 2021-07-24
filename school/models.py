from django.db import models



class Punkt(models.Model):
    punct = models.CharField(max_length=255, verbose_name='Населеный пункт')

    def __str__(self):
        return self.punct

    class Meta:
        verbose_name = 'Населеный пункт'
        verbose_name_plural = 'Населеные пункты'

class School(models.Model):
    punct = models.ForeignKey(Punkt, verbose_name='Населеный пункт', on_delete=models.CASCADE)
    school = models.CharField(max_length=255, verbose_name='Школа')

    def __str__(self):
        return self.school

    class Meta:
        verbose_name = 'Школа'
        verbose_name_plural = 'Школа'

class Klas(models.Model):
    school = models.ForeignKey(School, verbose_name='Школа', on_delete=models.CASCADE)

    STATUS_KLASS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
    )
    klas = models.CharField(max_length=30, choices=STATUS_KLASS, verbose_name='Статус')
    STATUS_ALF = (
        ('1', 'А'),
        ('2', 'Б'),
        ('3', 'В'),
        ('4', 'Г'),
        ('5', 'Д'),
        ('6', 'Е'),
        ('7', 'Ё'),
        ('8', 'Ж'),
        ('9', 'З'),
        ('10', 'И'),
        ('11', 'Й'),
        ('12', 'К'),
        ('13', 'Л'),
        ('14', 'М'),
        ('15', 'Н'),
    )
    alf = models.CharField(max_length=30, choices=STATUS_ALF, verbose_name='Статус')

    def __str__(self):
        return self.klas

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Класс'