from django.contrib.auth import authenticate
from rest_framework.views import APIView, Response, status
from .models import Torrent
from .serializers import UserLoginSerializer, UserRegistrationSerializer, UserProfileSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
# Create your views here.

# Generate Token Manually
def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }



class UserregistrationView(APIView):
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'Registration Success'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'token':token,'msg':'Login Successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'non_field_errors':["Email or Password is Invalid!"]}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):

    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)








# way for sending post request:
# {
#   "search":"avengers"
# }


class TorrentHandlerView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        return Response({'data':'SEARCH YOUR TORRENTS!'}, status=status.HTTP_200_OK) 

    def post(self, request, format=None):
        res = request.data.get('search')
        obj = Torrent(res)
        data = obj.handling_request()
        if "Error" in data:
            return Response({'data':data}, status=status.HTTP_400_BAD_REQUEST) 
        else: return Response({'data':data}, status=status.HTTP_200_OK) 
            
        

