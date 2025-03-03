from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import data,Profile_pic
# Create your views here.
from .forms import DataForm,Profile_form




def index(request):
  
    return render(request,'app1/home.html')

def contact(request):
      form=DataForm()
     
      return render(request,'app1/index.html',{'form':form})


def edit(request,id):
    instance = get_object_or_404(data, id=id)   
    form = DataForm(instance=instance)
    return render(request,'app1/index.html',{'form':form,'instance':instance})



def datas(request):
    # data_value = data.objects.all()
    data_value = data.objects.select_related('profile_pic')
    # profile_pic_object = data_object.profile_pic
    # profile_pic_url = profile_pic_object.profile.url
    # return HttpResponse(data_value.profile_pic.profile.url)
    # print(profile_pic,'fffff')
    # for item in data_value:
    #     item_name = item.name
    #     item_email = item.email
    #     item_message = item.message

    #     # Access the corresponding profile image
    #     if (item.profile_pic):
    #           pf=item.profile_pic
    #     else:
    #        pf=None

    #     print("name",item_name)
    #     print("image",pf)
    return render(request,'app1/datas.html',{'data':data_value})

def save(request):
   
     if request.method == 'POST':
            form = DataForm(request.POST)
            if form.is_valid():
               form.save()
               form=DataForm()
               data_value=data.objects.all()
              
               return render(request,'app1/datas.html',{'data':data_value})
            else:
                  return render(request,'app1/index.html',{'form':form})
     else:
         return render(request,'app1/index.html',{'form':form})
     


      
def update(request,pk=None):
   
     if request.method == 'POST':
        if pk is not None:
         
            instance = data.objects.get(pk=pk)
            form = DataForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                data_value=data.objects.all()
                return render(request,'app1/datas.html',{'data':data_value})
            else:
                 return render(request,'app1/index.html',{'form':form})

        else:
         return redirect('datas')
          
     else:
         return render(request,'app1/index.html',{'form':form})
    



def delete(request,id):
    data.objects.filter(id=id).delete()
    return redirect(datas)


def upload_photo(request,id):
    form=Profile_form()
    return render(request,'app1/profile.html',{'form':form,'userid':id})

def profile_save(request):
    if request.method == 'POST':
  
      
       userid=request.POST.get('userid')
      
   
       form = Profile_form(request.POST, request.FILES)
    if form.is_valid():
      
        try:
          data_instance = get_object_or_404(Profile_pic, name_id=userid)
          profile_instance = form.save(commit=False)
          profile_instance.name_id = data_instance.name_id
          profile_instance.save()
        except Exception as e:
            print(e)
        
        profile_instance = form.save(commit=False)
        profile_instance.name_id = userid
        form.save()
        
        return redirect(datas)
    else:
          form=Profile_form() 
 
    return render(request,'app1/profile.html',{'form':form,'userid':id})










    

