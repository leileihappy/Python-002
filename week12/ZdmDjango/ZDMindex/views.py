from django.shortcuts import render

# Create your views here.
from .models import ZdmTable

def phones(request):
    querystr = request.GET.get('querystr')
    commentdate = request.GET.get('commentdate')
    conditions = {}
    if querystr is not None and querystr != '':
        conditions = {'comment__contains':querystr}
    if commentdate is not None and commentdate != '':
        conditions['comment_date__contains'] =str(commentdate)
    contents = ZdmTable.objects.filter(**conditions)
    return render(request,'result.html',locals())