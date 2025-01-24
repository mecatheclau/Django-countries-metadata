from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Country(models.Model):
    name = models.CharField(_("Country name"), max_length=50)
    topLevelDomain = models.CharField(_("Top Leve Domain"), max_length=50)
    alpha2Code = models.CharField(_("alpha2Code"), max_length=50)
    alpha3Code = models.CharField(_("alpha3Code"), max_length=50)
    callingCodes = models.CharField(_("callingCodes"), max_length=50)
    capital = models.CharField(_("capital"), max_length=50)
    altSpellings = models.CharField(_("altSpellings"), max_length=50)
    region = models.CharField(_("region"), max_length=50)
    subregion = models.CharField(_("subregion"), max_length=50)
    population = models.CharField(_("population"), max_length=50)
    latlng = models.CharField(_("latlng"), max_length=50)
    demonym = models.CharField(_("demonym"), max_length=50)
    area = models.CharField(_("area"), max_length=50)
    gini = models.CharField(_("gini"), max_length=50)
    timezones = models.CharField(_("timezones"), max_length=50)
    borders = models.CharField(_("borders"), max_length=50)
    nativeName = models.CharField(_("nativeName"), max_length=50)
    numericCode = models.CharField(_("numericCode"), max_length=50)
    currencies = models.CharField(_("currencies"), max_length=50)
    languages = models.CharField(_("languages"), max_length=50)
    translations = models.CharField(_("translations"), max_length=50)
    flag = models.CharField(_("flag"), max_length=50)
    regionalBlocs = models.CharField(_("regionalBlocs"), max_length=50)
    cioc = models.CharField(_("cioc"), max_length=50)
    
    def __str__(self):
        return self.name
    
    