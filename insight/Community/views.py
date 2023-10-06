from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
from django.views.generic import ListView, DetailView, CreateView
from .forms import CommunityForm
from datetime import datetime
from Member.models import UserCommunity
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



#################
# 
# với mỗi hàm cần làm thì hoàn thiện lun path trong file url.py
# 
# ##########

def community_interface(request, pk):
    if not request.user.is_authenticated:
        return redirect('Member:signin')
    else:
        community = Community.objects.get(id = pk)
        user = request.user
        isMember = UserCommunity.objects.filter(user_id = user, community_id = pk).exists()
        context = {
            "community": community,
            "user": user,
            "isMember": isMember
        }
        return render(request, 'Community/community_interface.html', context)

def community_detail(request, pk):
    user=request.user
    isMember = UserCommunity.objects.filter(user_id = user, community_id = pk).exists()
    isFormer = Community.objects.filter(created_user_id=user).exists()
    if not request.user.is_authenticated:
        return redirect('Member:signin')
    elif not isMember:
        return redirect('Community:community-interface', pk=pk)
    else:
        community=Community.objects.get(id= pk)
        community_doc= CommunityDoc.objects.filter(community_id = community)
        user_community = UserCommunity.objects.filter(community_id = community)
        context = {
            'community': community,
            'community_doc': community_doc,
            'user_community': user_community,
            'isFormer': isFormer,
        }
        # community_size = creater_communities.count()
        # context['community_size'] = creater_communities.count()
        return render(request, 'Community/community_detail.html', context)


#1. xác định người dùng có thuộc community hay ko, nếu ko thì redirect qua trang detail
#2. xác định người dùng có phải former hay ko
#3. truy vấn ra danh sách tất cả các mentor thuộc community 
#4. render trang communitymentor

#anh việt
def community_mentor(request):
    pass


# metadata: usercommunityID,  mentor_id
#vd: request.POST.usercommunityID
# method: POST
# trả về json (không render trang html)
#1. kiểm tra trong bảng request_mentor đã có bản ghi nào trùng usercommunityID và mentor id hay chưa
# nếu có ròi thì gán cờ là flase, 
# nếu chưa có thì thêm vào bảng request_mentor một bảng ghi (usercommunityID, mentorID, status = 0), gán gờ là True
# trả về json
# Khang
def request_mentor(request):
    demo = {"key": 1}
    return JsonResponse(demo)


#meta data: usercommunityID,  mentor_id, option
# method: POST
#0. kiểm tra this.usercommunityID có bằng  mentor_id hay ko, ko thì return false
#1. kiểm tra trong bảng request_mentor đã có bản ghi nào trùng usercommunityID và mentor id hay chưa
# nếu cưa có thì gán cờ là flase,
# nếu có rồi thì thay đổi status thành 1/2 phụ thuộc theo option True, False
# Khang
def ansewer_request_mentor(request):
    pass



# upload document , gọi API của nhóm Hưng
def upload_document(request):
    pass



# get document and return render html
# Trung - Việt
def get_community_docments(request):
    pass




def add_community(request):
    if not request.user.is_authenticated:
        return redirect('Member:signin')
    else:
        user = request.user
        if(request.method == 'POST'):
            name = request.POST.get('community-name')
            description = request.POST.get('community-description')
            mentor_thres = request.POST.get('mentor-threshold')
            upload_permit = request.POST.get('community-upload-permission')
            entrance_test_enable = request.POST.get('enable-entrance-test')

            new_community = Community()
            new_community.name = name
            new_community.description = description
            new_community.created_user = user
            new_community.mentor_threshold = mentor_thres
            new_community.upload_permission = upload_permit
            if(entrance_test_enable == 'on'):
                new_community.entrance_test_enable = 1
            
            new_community.save()
            # if (entrance_test_enable == 'on'):
                # return redirect('Community:entrance_test') Hưng làm tiếp chỗ này
            return redirect('Community:home')
        return render(request, 'Community/add_community.html')

def join_community(request,pk):
    community = Community.objects.get(id = pk)
    user = request.user
    if commmunity.entrance_test_enable:
        pass
    else:
        if request.user.is_authenticated:
            community.Member.add(user)
            community.save()
            user_community = UserCommunity()
            user_community.user_id=user
            user_community.community_id=community
            user_community.joined_date=datetime.now()
            user_community.score=10
            user_community.save()
            context = {
                'this_community': community,
            }
            return redirect('Community:community-detail', pk=pk)
