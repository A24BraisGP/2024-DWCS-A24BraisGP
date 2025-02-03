from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm, NovellForm
from .models import Review,Novell
from django.views import View

# Create your views here.

class ReviewView(View):
  def get(self, request):
    form = ReviewForm()
    novell_form = NovellForm()
    
    return render(request, 'reviews/review.html',{
    'form':form,    
    'novell_form':novell_form
    })
    
  def post(self, request):
    # existing_data = Review.objects.get(id=1)
    # form = ReviewForm(request.POST
                      # instance=existing_data
                      # )
    # if form.is_valid():
    #   print(form)
    #   form.save()
    #   return HttpResponseRedirect('/thank-you')
    
    novell_form = NovellForm(request.POST)
    print('check')
    if novell_form.is_valid():
      novell_form.save()
    return render(request, 'reviews/thank_you.html',
                      {'novell_response':{
                        'user_name': novell_form.cleaned_data['user_name'],
                        'password':novell_form.cleaned_data['password'],
                        'city': novell_form.cleaned_data['city'],
                        'web_server': novell_form.cleaned_data['web_server'],
                        'role': novell_form.cleaned_data['role']          
                      },'novell_form':novell_form})


def thank_you(request):
  return render(request,'reviews/thank_you.html')