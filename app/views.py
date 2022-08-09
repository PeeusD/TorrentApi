
from rest_framework.views import APIView, Response, status
from .models import User, Torrent
from .serializers import UserSerializers

# Create your views here.

# way for sending post request:
# {
#   "search":"avengers"
# }


class TorrentHandler(APIView):
    def get(self, request, format=None):
        return Response({'data':'SEARCH YOUR TORRENTS!'}, status=status.HTTP_200_OK) 

    def post(self, request, format=None):
        res = request.data.get('search')
        obj = Torrent(res)
        data = obj.handling_request()
        if "Error" in data:
            return Response({'data':data}, status=status.HTTP_400_BAD_REQUEST) 
        else: return Response({'data':data}, status=status.HTTP_200_OK) 
            
        

