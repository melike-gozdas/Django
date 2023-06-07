from django.shortcuts import render, redirect, Http404, get_object_or_404
from .models import Data
from .forms import DataForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def data_index(request):
    data_list = Data.objects.all()

    paginator = Paginator(data_list, 20)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        datas = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        datas = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        datas = paginator.page(paginator.num_pages)
    return render(request, 'data/index.html', {'datas': datas})

def data_detail(request, CustomerId):
    data = get_object_or_404(Data, CustomerId=CustomerId)
    context = {
        'data': data,
    }
    return render(request, 'data/detail.html', context)

def data_create(request):
    #Surname = request.Data.get('Surname')
    #CreditScore = request.Data.get('CreditScore')
    #Geography = request.Data.get('Geography')
    #Gender = request.Data.get('Gender')
    #Age = request.Data.get('Age')
    #Tenure = request.Data.get('Tenure')
    #Balance = request.Data.get('Balance')
    #NumOfProducts = request.Data.get('NumOfProducts')
    #HasCrCard = request.Data.get('HasCrCard')
    #IsActivateMember = request.Data.get('IsActivateMember')
    #EstimatedSalary = request.Data.get('EstimatedSalary')
    #Data.objects.create(Surname=Surname, CreditScore=CreditScore,
    #                   Geography=Geography, Gender=Gender, Age=Age,
    #                   Tenure=Tenure, Balance=Balance, NumOfProducts=NumOfProducts,
    #                   HasCrCard=HasCrCard, IsActivateMember=IsActivateMember,
    #                   EstimatedSalary=EstimatedSalary)

    if not request.user.is_authenticated:
        return Http404
    if request.method == 'POST':
        #formdan gelen bilgileri kaydet
        form = DataForm(request.POST)
        if form.is_valid():
            data = form.save()
            return redirect('data:index')
    else:
        #formu kullanıcıya göster
        form = DataForm()

    #form = DataForm(request.POST or None)
    context = {
        'form': form,
    }

    return render(request, 'data/form.html', context)


def data_update(request, CustomerId):
    if not request.user.is_authenticated:
        return Http404
    data = get_object_or_404(Data, CustomerId=CustomerId)
    form = DataForm(request.POST or None, instance=data)
    if form.is_valid():
        form.save()
        return redirect('data:index')

    else:
        form = DataForm(instance=data)

    context = {
        'form': form,
        'data': data,
    }
    return render(request, 'data/form.html', context)

def data_delete(request, CustomerId):
    if not request.user.is_authenticated:
        return Http404
    data = get_object_or_404(Data, CustomerId=CustomerId)
    data.delete()
    return redirect('data:index')