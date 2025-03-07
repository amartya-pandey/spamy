from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from classifier.predict import classify_email

@api_view(['POST'])
def classify_email_view(request):
    email_text = request.data.get('email_text', '')
    if not email_text:
        return Response({"error": "No email text provided"}, status=400)
    
    prediction = classify_email(email_text)
    return Response({"email_text": email_text, "classification": prediction})

def index(request):
    return render(request, 'index.html')