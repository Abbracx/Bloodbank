from django.shortcuts import render, redirect, get_object_or_404
from .models import UserGroup, Membership, BloodRequest
from .forms import BloodRequestForm
from bloodapp.models import User, Profile
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse

@login_required
def blood_donate(request):
    return render(request, 'bloodapp/donate.html')

@login_required
def blood_request(request):
   
    if request.method == "POST":

        user_id = request.user.user_id
        user = User.objects.get(user_id = user_id)
        form = BloodRequestForm(request.POST)
        if form.is_valid():
            blood_request = form.save(commit=False)
            blood_request.sender = user
            blood_request.save()
            
            group_of_donors = {   
            #patient: [list_of_posible_donors]
            "A+" :  ['O-', 'O+', 'A-', 'A+'],
            "B+" :  ['O-', 'O+', 'B-', 'B+'],
            "AB+":  ['O-','O+','B-','B+','A-','A+','AB-','AB+'],
            "O+" :  ['O-','O+'],
            "O-" :  ['O-'],
            "AB-":  ['O-','B-', 'A-', 'AB-'],
            "B-" :  ['O-','B-'],
            "A-" :  ['O-','A-']
            }
      
            possible_list_of_donors = group_of_donors.get(blood_request.blood_type, None)
            
            if possible_list_of_donors is not None:
                for group_code in possible_list_of_donors:
                    group = UserGroup.objects.get(group_code=group_code)
                    group.request.add(blood_request)
                messages.success(request, f'blood request sent successfully.')
                return redirect('bloodrequestapp:user_requests', user_id)

    form = BloodRequestForm()
    context = {'form': form}
    return render(request, 'bloodapp/request.html', context)

@login_required
def list_of_request(request, user_id):
    user = User.objects.get(user_id=user_id)
    all_sent_request = user.blood_requests.all().order_by('-request_date')
    context = {"all_sent_request": all_sent_request}
    return render(request, 'bloodapp/list_of_request.html', context)

@login_required
def incoming_request(request):
    try:
        user_id = request.user.user_id
        user = User.objects.get(user_id= user_id)
       
        user_group = UserGroup.objects.get(group_code=user.profile.blood_group)
    except KeyError:
        raise HttpResponse('No such user')
    except User.DoesNotExist:
        raise Http404("User not found")

    context = {
        "incoming_request": user_group.request.all().exclude(sender=user).order_by('-request_date')
    }
    return render(request, 'bloodapp/incoming_request.html', context)

@login_required
def blood_refer(request):
    return render(request, 'bloodapp/refer.html')