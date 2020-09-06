from django.shortcuts import render

# Create your views here.

from .models import MovieTable
from django.db.models import Avg
import requests
import lxml.etree


def add(request):
    #从models取数据传递给templates
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
    headers = {'User-Agent':user_agent}
    url = 'https://movie.douban.com/subject/20495023/comments'

    response = requests.get(url=url, headers=headers)
    # print(response.text)

    selector = lxml.etree.HTML(response.text)

    dict = {'allstar50 rating':5,'allstar40 rating':4,'allstar30 rating':3,
        'allstar20 rating':2,'allstar10 rating':1}

    for i in range(1,21):
        review = selector.xpath(f'//*[@id="comments"]/div[{i}]/div[2]/p/span/text()')
        rating = selector.xpath(f'//*[@id="comments"]/div[{i}]/div[2]/h3/span[2]/span[2]/@class')
        star = dict[rating[0]]
        m = MovieTable()
        m.review = review
        m.star = star
        m.save()
    return render(request,'result.html',locals())

def display(request):
    querystr = request.GET.get('q')
    conditions = {'star__gt':3}
    if querystr is not None and querystr != '':
        conditions = {'star__gt':3,'review__contains':querystr}
    contents = MovieTable.objects.filter(**conditions)
    return render(request,'index.html',locals())