from django.shortcuts import render
from personal.models import Question

# Create your views here.

def home_screen_view(request):
    context = {}
    #context['some_string'] = "this is some string that im passing to view"
    #context['some_number'] = 123
    
    #context={
    #    'some_string':"this is some string that im passing to view",
    #    'some_number':123,
    #}
    
    #list_of_values = []
    #list_of_values.append("first entry")
    #list_of_values.append("second entry")
    #list_of_values.append("third entry")
    #list_of_values.append("forth entry")
    #context['list_of_values'] = list_of_values
    
    questions   = Question.objects.all()
    context['questions'] = questions
    
    
    
    return render(request, "personal/home.html", context)
