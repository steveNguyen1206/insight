from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
from django.views.generic import ListView, DetailView, CreateView
from .forms import CommunityForm
from Member.models import RequestMentor, UserCommunity


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

1. # xác định người dùng có thuộc community hay ko, nếu có thì redirect qua trang interface

#anh việt
def community_detail(request, pk):
    if not request.user.is_authenticated:
        return redirect('Member:signin')
    else:
        community = Community.objects.get(id = pk)
        user = request.user
        context = {
            "community": community,
            "user": user
        }
        return render(request, 'Community/community_detail.html', context)



#1. xác định người dùng có thuộc community hay ko, nếu ko thì redirect qua trang detail
#2. xác định người dùng có phải former hay ko
#3. Truy vấn ra danh sách các người dùng thuộc cộng đồng (có thể làm phân trang - nhưng chưa cần thiết)
#anh việt

def community_interface(request, pk):

    if not request.user.is_authenticated:
        return redirect('Member:signin')
    else:
        # this_user = User.objects.get(id = pk)
        # this_user2 = User.objects.get(id = pk)
        # print(this_user)
        community=Community.objects.get(id= pk)
        community_doc= CommunityDoc.objects.filter(community_id = community)
        print(community)
        context = {
            'community': community,
            'community_doc': community_doc,

        }
        # community_size = creater_communities.count()
        # context['community_size'] = creater_communities.count()
        return render(request, 'Community/community_interface.html', context)


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
    if request.method == 'POST':
        # Retrieve usercommunityID and mentorID from POST data
        usercommunityID = request.POST.get(...) #tên của trường usercommunityid trong form
        mentorID = request.POST.get(...) #tên của trường mentorID trong form
        
        # Check if a record with the same usercommunityID and mentorID exists
        existing_request = RequestMentor.objects.filter(
            UserCommunityId=usercommunityID,
            mentorId=mentorID
        ).first()
        
        # Initialize flag and status
        flag = True
        status = None
        
        if existing_request:
            # If a record exists, set flag to False and retrieve status
            flag = False
            status = existing_request.status
        else:
            # Check foreign key reference
            requesting_user = UserCommunity.objects.filter(id=usercommunityID) 
            requested_mentor = UserCommunity.objects.filter(user_id=mentorID).first()
            if (requested_mentor != None and requesting_user != None):
                record = RequestMentor(
                    UserCommunityId=usercommunityID,
                    mentorId=mentorID,
                    status = 0,
                )
                record.save()

                
        
        # Create a JSON response
        response_data = {
            'usercommunityID': usercommunityID,
            'mentorID': mentorID,
            'status': status,
            'flag': flag
        }
        
        return JsonResponse(response_data)
    else:
        # Handle other HTTP methods (e.g., GET)
        return JsonResponse({'error': 'Invalid request method'}, status=405)


#meta data: usercommunityID,  mentor_id, option
# method: POST
#0. kiểm tra this.usercommunityID có bằng  mentor_id hay ko, ko thì return false
#1. kiểm tra trong bảng request_mentor đã có bản ghi nào trùng usercommunityID và mentor id hay chưa
# nếu cưa có thì gán cờ là flase,
# nếu có rồi thì thay đổi status thành 1/2 phụ thuộc theo option True, False
# Khang
def ansewer_request_mentor(request):
    if request.method == "POST":
        # Retrieve usercommunityID, mentorID, and option from POST data
        usercommunityID = request.POST.get('...')
        mentorID = request.POST.get('...')
        option = request.POST.get('...')

        # Check if a record with the same usercommunityID and mentorID exists
        existing_request = RequestMentor.objects.filter(
            UserCommunityId=usercommunityID,
            mentorId=mentorID
        ).first()

        # Initialize flag
        flag = True

        if not existing_request:
            # If no record exists, set flag to False
            flag = False
        else:
             # Check foreign key reference
            requesting_user = UserCommunity.objects.filter(id=usercommunityID) 
            requested_mentor = UserCommunity.objects.filter(user_id=mentorID).first()
            if (requested_mentor != None and requesting_user != None):
                # If a record exists, update the status based on the option
                if option == 1:
                    existing_request.status = 1  # Accept
                elif option == 2:
                    existing_request.status = 2  # Reject
                else:
                    flag = False
                    return JsonResponse({'error': 'Invalid option'})
                existing_request.save()

        # Create a JSON response
        response_data = {
            'usercommunityID': usercommunityID,
            'mentorID': mentorID,
            'status': option,
            'flag': flag
        }

        return JsonResponse(response_data)
    else:
        # Handle other HTTP methods (e.g., GET)
        return JsonResponse({'error': 'Invalid request method'}, status=405)



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
