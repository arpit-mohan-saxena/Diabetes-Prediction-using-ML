from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def predict(request):
    # Example logic – adjust as needed
    if request.method == "POST":
        # handle prediction here
        return render(request, 'result.html', {'prediction': 'Your result here'})
    return render(request, 'predict.html')

def result(request):
    return render(request, 'result.html')
