from django.db import models
from django.utils.translation import gettext as _
# Create your models here.
# test
class Sq(models.Model):
    def __str__(self):
        return self.uid
    X=models.CharField(
        help_text=_('x'),
        max_length=100,
        default=None,
    )
    Y=models.CharField(
        help_text=_('y'),
        max_length=100,
        default=None,
    )
    uid=models.CharField(
        help_text=_('unique squirrel id'),
        max_length=100,
    )
    hectare=models.CharField(
        help_text=_('hectare'),
        max_length=100,
        default=None,
    )
    
    AM='am'
    PM='pm'
    SHIFT_CHOICE=(
        (AM,'AM'),
        (PM,'PM'),
    )

    shift=models.CharField(
        help_text=_('shift'),
        max_length=2,
        choices=SHIFT_CHOICE,
        default=AM,
    )
    date=models.DateField(
        help_text=_('date'),
        default=None,
    )
    hectarenumber=models.CharField(
        help_text=_('hectare squirrel number'),
        max_length=100,
        default=None,
    )
    ADULT='adult'
    JUVENILE='juvenile'

    AGE_CHOICES=(
        (ADULT,'Adult'),
        (JUVENILE,'Juvenile'),
    )
    age=models.CharField(
        help_text=_('age'),
        max_length=20,
        choices=AGE_CHOICES,
        default=ADULT,
    )
    color=models.CharField(
        help_text=_('primary color'),
        max_length=100,
        default=None,
    )
    hcolor=models.CharField(
        help_text=_('highlight fur color'),
        max_length=100,
        default=None,
    )
    ccolor=models.CharField(
        help_text=_('combination color'),
        max_length=100,
        default=None,
    )
    cnotes=models.CharField(
        help_text=_('color notes'),
        max_length=100,
        default=None,
    )
    location=models.CharField(
        help_text=_('location'),
        max_length=100,
        default=None,
    )
    measurement=models.CharField(
        help_text=_('measurement'),
        max_length=100,
        default=None,
    )
    slocation=models.CharField(
        help_text=_('specific location'),
        max_length=100,
        default=None,
    )
    TRUE='true'
    FALSE='false'
    choice=(
        (TRUE,'True'),
        (FALSE,'False'),
    )
    running=models.CharField(
        help_text=_('running'),
        max_length=10,
        choices=choice,
        default=FALSE,
    )
    chasing=models.CharField(
        help_text=_('chasing'),
        max_length=10,
        choices=choice,
        default=FALSE,
    )
    climbing=models.CharField(
        help_text=_('climbing'),
        max_length=10,
        choices=choice,
        default=FALSE,
    )
    eating=models.CharField(
        help_text=_('eating'),
        max_length=10,
        choices=choice,
        default=FALSE,
    )
    foraging=models.CharField(
        help_text=_('foraging'),
        max_length=10,
        choices=choice,
        default=FALSE,
    )
    otheract=models.CharField(
        help_text=_('other activities'),
        max_length=100,
        default=None,
    )
    kuks=models.CharField(
        help_text=_('kuks'),
        max_length=10,
        choices=choice,
        default=FALSE,
    )
    quaas=models.CharField(
        help_text=_('quaas'),
        max_length=10,
        choices=choice,
        default=FALSE,
    )
    moans=models.CharField(
        help_text=_('moans'),
        max_length=10,
        choices=choice,
        default=FALSE,
    )
    tflag=models.CharField(
        help_text=_('tail flags'),
        max_length=10,
        choices=choice,
        default=FALSE,
    )
    ttwitch=models.CharField(
        help_text=_('tail twitches'),
        max_length=10,
        choices=choice,
        default=FALSE,
    )
    approach=models.CharField(
        help_text=_('approach'),
        max_length=10,
        choices=choice,
        default=FALSE,
    )
    idiff=models.CharField(
        help_text=_('indifference'),
        max_length=10,
        choices=choice,
        default=FALSE,
    )
    runsfrom=models.CharField(
        help_text=_('runs from'),
        max_length=10,
        choices=choice,
        default=FALSE,
    )
    otherinter=models.CharField(
        help_text=_('other interactions'),
        max_length=100,
        default=None,
    )
    ll=models.CharField(
        help_text=_('lat/long'),
        max_length=100,
        default=None,
    )
    zc=models.CharField(
        help_text=_('zip codes'),
        max_length=100,
        default=None,
    )
    cdistricts=models.CharField(
        help_text=_('community districts'),
        max_length=100,
        default=None,
    )
    bb=models.CharField(
        help_text=_('borough boundaries'),
        max_length=100,
        default=None,
    )
    ccd=models.CharField(
        help_text=_('city council districts'),
        max_length=100,
        default=None,
    )
    pp=models.CharField(
        help_text=_('police precincts'),
        max_length=100,
        default=None,
    )
