from email.policy import default
from unicodedata import name
from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
class Menu(models.Model):
    vegA = models.IntegerField(default=150)
    nonA = models.IntegerField(default=200)
    chicA = models.IntegerField(default=100)
    fishA = models.IntegerField(default=170)
    rotiA = models.IntegerField(default=8)
    saladA = models.IntegerField(default=20)
    panerA = models.IntegerField(default=160)
    curryA = models.IntegerField(default=75)
    rotiP =  models.IntegerField(default=10) 
    chicP =  models.IntegerField(default=110)
    butP =   models.IntegerField(default=20)
    babyP =  models.IntegerField(default=75)
    friP =  models.IntegerField(default= 85)
    chicfriP =  models.IntegerField(default= 130)
    rotiC =  models.IntegerField(default=30) 
    chicC =  models.IntegerField(default=40)
    butC =   models.IntegerField(default=45)
    babyC =  models.IntegerField(default=60)
    friC =  models.IntegerField(default= 45)
    chicfriC =  models.IntegerField(default= 30)
    rotiH =  models.IntegerField(default=150) 
    chicH =  models.IntegerField(default= 160)
    butH =   models.IntegerField(default= 140)
    babyH =  models.IntegerField(default= 120)
    chicfriH =  models.IntegerField(default= 180)
    rotiM =  models.IntegerField(default= 450) 
    chicM =  models.IntegerField(default= 400)
    butM =   models.IntegerField(default= 540)
    babyM =  models.IntegerField(default= 400)
    chicfriM =  models.IntegerField(default= 600)
    
    a1 =   models.IntegerField(default= 0)
    a2 =  models.IntegerField(default= 0)
    a3 =  models.IntegerField(default= 0)
    a4 =  models.IntegerField(default= 0) 
    a5 =  models.IntegerField(default= 0)
    a6 =   models.IntegerField(default= 0)
    a7 =  models.IntegerField(default= 0)
    a8 =  models.IntegerField(default= 0)

    p1 =   models.IntegerField(default= 0)
    p2 =  models.IntegerField(default= 0)
    p3 =  models.IntegerField(default= 0)
    p4 =  models.IntegerField(default= 0) 
    p5 =  models.IntegerField(default= 0)
    p6 =   models.IntegerField(default= 0)

    c1 =   models.IntegerField(default= 0)
    c2 =  models.IntegerField(default= 0)
    c3 =  models.IntegerField(default= 0)
    c4 =  models.IntegerField(default= 0) 
    c5 =  models.IntegerField(default= 0)
    c6 =   models.IntegerField(default= 0)


    h1 =   models.IntegerField(default= 0)
    h2 =  models.IntegerField(default= 0)
    h3 =  models.IntegerField(default= 0)
    h4 =  models.IntegerField(default= 0) 
    h5 =  models.IntegerField(default= 0)
    h6 =   models.IntegerField(default= 0)
    
    
    m1 =  models.IntegerField(default= 0)
    m2 =  models.IntegerField(default= 0)
    m3 =  models.IntegerField(default= 0)
    m4 =  models.IntegerField(default= 0) 
    m5 =  models.IntegerField(default= 0)
    m6 =  models.IntegerField(default= 0)
     
    ma =  models.IntegerField(default= 5)
    mp =  models.IntegerField(default= 5)
    mf =  models.IntegerField(default= 5)
    mh =  models.IntegerField(default= 5) 
    mm =  models.IntegerField(default= 5)

    da =  models.IntegerField(default= 3)
    dp =  models.IntegerField(default= 3)
    df =  models.IntegerField(default= 3)
    dh =  models.IntegerField(default= 3) 
    dm =  models.IntegerField(default= 3)

    ra =  models.IntegerField(default= 3, validators=[MinValueValidator(1), MaxValueValidator(5)])
    rp =  models.IntegerField(default= 3, validators=[MinValueValidator(1), MaxValueValidator(5)])
    rf =  models.IntegerField(default= 3, validators=[MinValueValidator(1), MaxValueValidator(5)])
    rh =  models.IntegerField(default= 3, validators=[MinValueValidator(1), MaxValueValidator(5)]) 
    rm =  models.IntegerField(default= 3, validators=[MinValueValidator(1), MaxValueValidator(5)])

    
    nA =   models.IntegerField(default= 0)
    nP =  models.IntegerField(default= 0)
    nC =  models.IntegerField(default= 0)
    nH =  models.IntegerField(default= 0) 
    nM =  models.IntegerField(default= 0)

    priceA =   models.IntegerField(default= 0)
    priceP =  models.IntegerField(default= 0)
    priceC =  models.IntegerField(default= 0)
    priceH =  models.IntegerField(default= 0) 
    priceM =  models.IntegerField(default= 0)

    otp = models.IntegerField(default= 4523)
    otp1 = models.IntegerField(default= 4523)
    otp2 = models.IntegerField(default= 4523)
    otp3 = models.IntegerField(default= 4523)
    otp4 = models.IntegerField(default= 4523)

    name = models.CharField(max_length= 20)
    named = models.CharField(max_length= 20)

    



