from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm, Novell
from .models import Review,Novell
from django.views import View

# Create your views here.

class ReviewView(View):
  def get(self, request):
    form = ReviewForm()
    # novell_form = NovellForm()
    
    return render(request, 'reviews/review.html',{
    'form':form,    
    # 'novell_form':novell_form
    })
  def post(self, request):
    existing_data = Review.objects.get(id=1)
    form = ReviewForm(request.POST
                      # instance=existing_data
                      )
    if form.is_valid():
      print(form)
      form.save()
      return HttpResponseRedirect('/thank-you')
    # novell_form = NovellForm(request.POST)
    # print(novell_form)
    # if novell_form.is_valid():
    #   print(novell_form.cleaned_data)
    #   return HttpResponseRedirect('thank-you',{'novell_response':novell_form.cleaned_data})


def thank_you(request):
  return render(request,'reviews/thank_you.html')