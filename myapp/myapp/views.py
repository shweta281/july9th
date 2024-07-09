
from django.shortcuts import render

def index(request):
    a=''
    ans=0
    try:
        if(request.method=='POST' ):
            a=request.POST.get('inputexpression')
    except:
        pass
    if(len(a)>0):
        try:
            ans=eval(a)
        except:
            ans='invalid expression'
    else:
        ans=''
    return render(request,'index.html',{'ans':ans, 'exp':a})

