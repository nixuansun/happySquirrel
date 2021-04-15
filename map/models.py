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

    running = models.BooleanField(blank=True, null=True)

    chasing = models.BooleanField(blank=True, null=True)

    climbing = models.BooleanField(blank=True, null=True)

    eating = models.BooleanField(blank=True, null=True)

    foraging = models.BooleanField(blank=True, null=True)

    kuks = models.BooleanField(blank=True, null=True)

    quaas = models.BooleanField(blank=True, null=True)

    moans = models.BooleanField(blank=True, null=True)

    tail_flags = models.BooleanField(blank=True, null=True)

    tail_twitches = models.BooleanField(blank=True, null=True)

    approaches = models.BooleanField(blank=True, null=True)

    indifferent = models.BooleanField(blank=True, null=True)

    runs_from = models.BooleanField(blank=True, null=True)
