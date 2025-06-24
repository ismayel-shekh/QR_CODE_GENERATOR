from django.shortcuts import render,get_object_or_404
from .models import User_Data_all
from django.db.models import Q





# def index(request):
#     if 'q' in request.GET:
#         q = request.GET['q']
#         # data = Data.objects.filter(last_name__icontains=q)
#         multiple_q = Q(Q(first_name__icontains=q) | Q(last_name__icontains=q))
#         data = Data.objects.filter(multiple_q)
#     else:
#         data = Data.objects.all()
#     context = {
#         'data': data
#     }
#     return render(request, 'dashboard/index.html', context)

# home page all data 

def Homepage(request):
    
    
    users = User_Data_all.objects.all()  # Fetch all user data
    
    return render(request, 'Home.html', {'users': users})




# all user table wise data show 



def all_user(request):
    
    q = request.GET.get('question', '')  # Get the search query, default to empty string if not present
    
    if q:
        multiple_q = Q(Q(Nid_card_number__icontains=q) | Q(phone_number__icontains=q))
        user_all = User_Data_all.objects.filter(multiple_q)
    else:
        user_all = User_Data_all.objects.all()
    
    return render(request, 'all_user.html', {'user_all': user_all, 'query': q})






# pk wise user all data show


def user_detail(request, pk):
    user = get_object_or_404(User_Data_all, pk=pk)
    return render(request, 'data.html', {'user': user})




# add user form

def Add_user(request):
    
    return render(request, 'add_user.html' )