from django.db import models
from sizefield import models as sizefield_models
from django.contrib.auth.models import User
from pilani_pirates.settings import CATEGORIES
import requests

# Create your models here.


class File(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=100)
    magnet = models.CharField(max_length=100, unique=True)
    filesize = sizefield_models.FileSizeField(default=0)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    uploader = models.ForeignKey(User, default="SIDS")
    category = models.CharField(max_length=100, choices=CATEGORIES)
    verified = models.BooleanField(default=False)
    hits = models.IntegerField(default=0)
    infoId = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = ('File')
        verbose_name_plural = ('Files')

    def __unicode__(self):
        return self.title

    def getInfo(self):
        try:
            category = self.category
            imdbID = self.infoId
            if category == "movie":
                url = "http://www.omdbapi.com/?i="
                jsonData = requests.get(url+imdbID)
                data = jsonData.json()          

                if data["Response"] == "False":
                    return "Movie not found."
                else:
                    output = "\nRated:\t\t" + data["Rated"]
                    output += "\n\nReleased:\t" + data["Released"]
                    output += "\n\nRuntime:\t" + data["Runtime"]
                    output += "\n\nGenre:\t\t" + data["Genre"]
                    output += "\n\nRating:\t\t" + data["imdbRating"]
                    output += "\n\nPlot:\t\t" + data["Plot"]
                    output += "\n\nDirector:\t" + data["Director"]
                    output += "\n\nWriter:\t\t" + data["Writer"]
                    output += "\n\nStars:\t\t" + data["Actors"]
                    output += "\n\n</pre><span id='poster'></span><script>document.getElementById('poster').innerHTML = ReferrerKiller.imageHtml('" + data["Poster"][:-8] + "Y300.jpg');</script>"
                    return output
            else:
                return ""
        except:
            return "error in getting info."
