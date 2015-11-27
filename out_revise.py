import os
import os.path

#help(os.path)
def makedirs(path):
    dirs=path.split('/')
    for i in range(len(dirs)):
        if not os.path.exists(dirs[i]):
            if i==0:
                os.mkdir(dirs[i])
            else:
                os.chdir(os.getcwd()+'\\\\'+dirs[i-1])
                os.mkdir(dirs[i])

                
makedirs('templates') 
makedirs('static/poster')

#print os.getcwd()

# os.chdir('templates')
# print os.getcwd()

# if os.path.exists('index.html'):
    # os.remove('index.html')
    
# index='''
# $def with (movies)
# <h1>Chestnut's Movie Site</h1>
# $movies

# $for movie in movies:
    # <li>
    # $movie['title'],$movie['year']
    # </li>
# '''

# f=file('index.html','w')
# f.write(index)
# f.close()


