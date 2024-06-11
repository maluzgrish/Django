
from datetime import  datetime,date
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from intake.forms import WaterintakeForm
from django.utils.timezone import localdate

from .models import Waterintake
from django.core.paginator import Paginator


@login_required(login_url='login')
def add_intake(request):
        form = WaterintakeForm(request.POST)
        if form.is_valid():
            water_intake = form.save(commit=False)
            water_intake.user = request.user
            today = date.today()
            existing_intake = Waterintake.objects.filter(user=request.user, date=today)
            if existing_intake.exists():
                return render(request, 'intake_mes.html', {
                    'form': form,
                    'error_message': 'Sorry,You have already added a water intake for today.' })
            
                  
            water_intake.save()
            return redirect('list')
        else:
         form = WaterintakeForm()
        name= request.user.username
        return render(request, 'intake.html', {'form': form,'name':name})


@login_required(login_url='login')
def intake_list(request):
   
    intakes = Waterintake.objects.filter(user=request .user)
    paginator = Paginator(intakes, 3)  # Set the number of items per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'intakelist.html', {'page_obj': page_obj})




def intake_update(request, id):
    intake = Waterintake.objects.get(pk=id)
    if request.method == 'POST':
        form = WaterintakeForm(request.POST,instance=intake)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form =WaterintakeForm(instance=intake)           
    return render(request, 'update.html', {'form': form,'intake': intake})

def intake_delete(request,id):
    intake=Waterintake.objects.get(pk=id)  
    if request.method == 'POST':
        intake.delete()
        return redirect('list')
    
    return render(request,'delete.html',{'intake':intake})




