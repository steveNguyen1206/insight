from django.shortcuts import render, redirect
from .models import *
from django.views.generic import ListView, DetailView, CreateView
from .forms import CommunityForm

# Create your views here.

def home(request):
    if not request.user.is_authenticated:
        return redirect('Member:signin')
    else:
        # select * from community
        all_communities = Community.objects.all() 
        flag = False if len(all_communities) == 0 else True
        shorcuts_mock = [
            {
                "name": "Manchester",
                "path": "muvodic",
                "logo": "shiba-shorcuts.jpg"
            },

            {
                "name": "United",
                "path": "muvodic",
                "logo": "shiba-shorcuts.jpg"
            },

            {
                "name": "Jack",
                "path": "muvodic",
                "logo": "shiba-shorcuts.jpg"
            }
        ]
        context = {
            'flag': flag,
            'communities': all_communities,
            'shorcuts': shorcuts_mock
        }
        return render(request, 'Community/home.html', context)

class CommunityDetail(DetailView):
    model = Community   
    template_name = 'Community/community_detail.html'

def add_community(request):
    if not request.user.is_authenticated:
        return redirect('Member:login')
    else:
        user = request.user
        if(request.method == 'POST'):
            name = request.POST.get('community-name')
            description = request.POST.get('community-description')
            new_community = Community()
            new_community.name = name
            new_community.description = description
            new_community.created_user = user
            new_community.save()
            return redirect('Community:home')
        return render(request, 'Community/add_community.html')
