import urllib
import web
import os
import time

def get_poster(id,url):
    pic=urllib.urlopen(url).read()
    pic_name='%d.jpg'%id
    f=file(pic_name,'wb')
    f.write(pic)
    f.close()
    
db=web.database(dbn='sqlite',db='MovieSite.db')
movies=db.select('movie')
count=0
os.chdir('static/poster')
for movie in movies:
    get_poster(movie.id,movie.image)
    count+=1
    print count,movie.title
    time.sleep(2)