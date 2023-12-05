from django.shortcuts import render
from django.http import HttpResponse
import re

# Create your views here.
def home(request):
    return render(request, 'home.html')

def calculation(request):
    if request.method=="POST":
        values=request.POST['values'] 
        print(values)
        vals=re.findall(r"(\d+)",values)
        operators=['+','x','/','-','.','%']
        opr=[]
        for v in values:
            for o in operators:
                if v==o:
                    opr.append(o)
        print(opr)                     
        print(re.findall(r"(\d+)",values))

        for o in opr:
            if o=='.':
                i=opr.index(o)
                res=vals[i]+"."+vals[i+1]
                vals.remove(vals[i+1])
                opr.remove(opr[i])
                vals[i]=res
                print(vals)
                print(opr)
        for o in opr:
            if o=='%':
                i=opr.index(o)
                res=(float(vals[i])/100)*float(vals[i+1])
                vals.remove(vals[i+1])
                opr.remove(opr[i])
                vals[i]=res
                print(vals)
                print(opr)
        for o in opr:
            if o=='/':
                i=opr.index(o)
                res=float(vals[i])/float(vals[i+1])
                vals.remove(vals[i+1])
                opr.remove(opr[i])
                vals[i]=str(res)
                print(vals)
                print(opr)
        for o in opr:
            if o=='x':
                i=opr.index(o)
                res=float(vals[i])*float(vals[i+1])
                vals.remove(vals[i+1])
                opr.remove(opr[i])
                vals[i]=str(res)
                print(vals)
                print(opr)
        for o in opr:
            if o=='+':
                i=opr.index(o)
                res=float(vals[i])+float(vals[i+1])
                vals.remove(vals[i+1])
                opr.remove(opr[i])
                vals[i]=str(res)
                print(vals)
                print(opr)
            if o=='-':
                i=opr.index(o)
                res=float(vals[i])-float(vals[i+1])
                vals.remove(vals[i+1])
                opr.remove(opr[i])
                vals[i]=str(res)
                print(vals)
                print(opr)

        
        if len(opr)!=0:
            if opr[0]=='/':
                result = float(vals[0])/float(vals[1])
            elif opr[0]=='x':
                result = float(vals[0])*float(vals[1])
            elif opr[0]=='+':
                result = float(vals[0])+float(vals[1])
            else :
                result = float(vals[0])-float(vals[1])
        else:
            result = float(vals[0])

        final_result=round(result,2)
        print(final_result)
        
    res=render(request,'home.html',{'result':final_result,'values':values})
    return res
