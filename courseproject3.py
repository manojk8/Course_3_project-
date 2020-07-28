1.
import json
import requests_with_caching

def get_movies_from_tastedive(n):
    base='https://tastedive.com/api/similar'
    d={}
    d['q']=n
    d['limit']=5
    d['type']='movies'
    s=requests_with_caching.get(base,d,permanent_cache_file="permanent_cache.txt")
    ss=s.json()
    print(s.url)
    print (ss)
    return ss



2.
import json
import requests_with_caching

def get_movies_from_tastedive(n):
    d={}
    base='https://tastedive.com/api/similar'
    d['limit']=5
    d['type']='movies'
    d['q']=n
    s=requests_with_caching.get(base,d,permanent_cache_file='permanent_cache.txt')
    print(s.url)
    ss=s.json()
    return ss
def extract_movie_titles(q):
    print(type(q))
    p=[]
    for x in q['Similar']['Results']:
        p.append(x['Name'])
    print(p)
    return p     
            
q=get_movies_from_tastedive('Black Panther')


3.
import json
import requests_with_caching

def get_movies_from_tastedive(n):
    d={}
    base='https://tastedive.com/api/similar'
    d['limit']=5
    d['type']='movies'
    d['q']=n
    s=requests_with_caching.get(base,d,permanent_cache_file='permanent_cache.txt')
    ss=s.json()
    return ss
def extract_movie_titles(q):
    p=[]
    for x in q['Similar']['Results']:
        p.append(x['Name'])
    return p   

def get_related_titles(l):
    one=[]
    for x in l:
        c=get_movies_from_tastedive(x)
        cc=extract_movie_titles(c)
        for b in cc:
            one.append(b)
    return list(set(one))

q=get_movies_from_tastedive('Black Panther')
l=extract_movie_titles(q)


4.

import json
import requests_with_caching

def get_movie_data(o):
    d={}
    d['t']=o
    d['r']='json'
    base='http://www.omdbapi.com/'
    x=requests_with_caching.get(base,d,permanent_cache_file='permanent_cache.txt')
    c=x.json()
    print(c)
    return c
a=get_movie_data('Black Panther')


5.import json
import requests_with_caching

def get_movie_data(o):
    d={}
    d['t']=o
    d['r']='json'
    base='http://www.omdbapi.com/'
    x=requests_with_caching.get(base,d,permanent_cache_file='permanent_cache.txt')
    c=x.json()
    return c
def get_movie_rating(r):
    rate=r['Ratings']
    for x in rate:
        if x['Source']=='Rotten Tomatoes':
            a=(x['Value'])
            return int(a[:2])
    else:
        return 0
    
    
6.

import json
import requests_with_caching

def get_movies_from_tastedive(n):
    d={}
    base='https://tastedive.com/api/similar'
    d['limit']=5
    d['type']='movies'
    d['q']=n
    s=requests_with_caching.get(base,d,permanent_cache_file='permanent_cache.txt')
    ss=s.json()
    return ss

def extract_movie_titles(q):
    p=[]
    for x in q['Similar']['Results']:
        p.append(x['Name'])
    return p 

def get_related_titles(l):
    one=[]
    for x in l:
        c=get_movies_from_tastedive(x)
        cc=extract_movie_titles(c)
        for b in cc:
            one.append(b)
    return list(set(one))

def get_movie_data(o):
    d={}
    d['t']=o
    d['r']='json'
    base='http://www.omdbapi.com/'
    x=requests_with_caching.get(base,d,permanent_cache_file='permanent_cache.txt')
    c=x.json()
    return c

def get_movie_rating(r):
    
    rate=r['Ratings']
    for x in rate:
        if x['Source']=='Rotten Tomatoes':
            a=(x['Value'])
            return int(a[:2])
    else:
        return 0
def get_sorted_recommendations(l):
    a=get_related_titles(l)
    i=sorted(a,key= lambda x:(get_movie_rating(get_movie_data(x)),x),reverse=True)
    print(i)
    return i
   