from django.shortcuts import render
from . import extractor
from . import rf_model
# Create your views here.


def index(request):
    if request.method == 'POST':
        url = request.POST.get('url_name')
        url_extractor = extractor.feature_extractor(url)
        features = url_extractor.extractor()
        pred = rf_model.predictor(features)
        if pred == 0:
            prediction = "Spoofed webpage: Yes"
        else:
            prediction = "Spoofed webpage: NO"
        return render(request, 'index.html', {'prediction': prediction})
    else:
        return render(request, 'index.html')

# def phishing_result(request):
#     if request.method == 'POST':
#         print("get request")
#         # url = request.POST.get('url_name')
#         # detector = extractor.feature_extractor(url)
#         # str1, str2 = detector.extractor()
#         return render(request, 'phishing_result.html')

#     return render(request, 'index.html')
