from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ContactSerializer

class ContactView(APIView):
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
             # Print the validated data
            print('Data from frontend:', serializer.validated_data)  # Use validated_data to get the cleaned data
            # Here you can handle the data, e.g., save it to the database or send an email
            # For demonstration, we'll just return a success message
    
            return Response({"message": "Message received successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
