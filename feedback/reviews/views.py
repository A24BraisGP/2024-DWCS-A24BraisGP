from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm,NovellForm
from .models import Review
# Create your views here.
def reviews(request):
  if request.method == 'POST':
    form = ReviewForm(request.POST)
    novell_form = NovellForm(request.POST)
    if novell_form.is_valid():
      return HttpResponseRedirect('thank-you',{'novell_response':novell_form.cleaned_data})
    # if form.is_valid():
    #   print(form.cleaned_data)
    #   review = Review(
    #     user_name=form.cleaned_data['user_name'],
    #     review_text=form.cleaned_data['review_text'],
    #     rating=form.cleaned_data['rating']
    #   )
    #   review.save()
        
  else:
    form = ReviewForm()
    novell_form = NovellForm()

    
  return render(request, 'reviews/review.html',{
    'form':form,
    'novell_form':novell_form
    
    })
  


def thank_you(request):
  
  return render(request,'reviews/thank_you.html')