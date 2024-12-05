from django.http import HttpResponse,JsonResponse
def home_page(request):
    print("home page requested")
    friends=[
        'vinay',
        'madhu',
        'vijay'
    ]
        
    
    
    
    return JsonResponse(friends,safe=False)