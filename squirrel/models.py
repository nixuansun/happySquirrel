from django.db import models

# Create your models here.
class happySquirrel(models.Model):

    latitude = models.FloatField(
        max_length=20,
    )

    longitude = models.FloatField(
        max_length=20,
    )

    unique_squirrel_id = models.CharField(
        max_length=20,
    )

    AM = 'AM'
    PM = 'PM'

    SHIFT_CHOICES = [
        (AM, 'AM'),
        (PM, 'PM'),
    ]

    shift = models.CharField(
        max_length=2,
        choices=SHIFT_CHOICES,
    )

    date = models.CharField(
        max_length=8,
        help_text='Date Format: MMDDYYYY',
    )

    Adult = 'Adult'
    Juvenile = 'Juvenile'

    AGE_CHOICES = [
        (Adult, 'Adult'),
        (Juvenile, 'Juvenile'),
    ]

    age = models.CharField(
        max_length=20,
        choices=AGE_CHOICES,
    )

    Gray = 'Gray'
    Cinnamon = 'Cinnamon'
    Black = 'Black'
    White = 'White'

    COLOR_CHOICES = [
        (Gray, 'Gray'),
        (Cinnamon, 'Cinnamon'),
        (Black, 'Black'),
        (White, 'White'),
    ]

    primary_fur_color = models.CharField(
        max_length=20,
        choices=COLOR_CHOICES,
    )

    AG = 'Above Ground'
    GP = 'Ground Plane'

    LOCATION_CHOICES = [
        (AG, 'Above Ground'),
        (GP, 'Ground Plane'),
    ]

    location = models.CharField(
        max_length=20,
        choices=LOCATION_CHOICES,
    )

    running = models.BooleanField()

    chasing = models.BooleanField()

    climbing = models.BooleanField()

    eating = models.BooleanField()

    foraging = models.BooleanField()

    kuks = models.BooleanField()

    quaas = models.BooleanField()

    moans = models.BooleanField()

    tail_flags = models.BooleanField()

    tail_twitches = models.BooleanField()

    approaches = models.BooleanField()

    indifferent = models.BooleanField()

    runs_from = models.BooleanField()

    def __str__(self):
        return self.unique_squirrel_id

