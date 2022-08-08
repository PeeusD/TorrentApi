
from rest_framework.views import APIView, Response, status
from rest_framework.decorators import api_view
from .models import User, Torrent
from .serializers import UserSerializers

# Create your views here.

# way for sending post request:
# {
#   "search":"avengers"
# }

@api_view(['GET', 'POST'])
def torrent_api(request):
    if request.method == 'GET':
        return Response({'data':'SEARCH YOUR TORRENTS!'}, status=status.HTTP_200_OK) 
    if request.method == 'POST':
            res = request.data.get('search')
            obj = Torrent(res)
            data = obj.handling_request()
            

            return Response({'data':data}, status=status.HTTP_200_OK) 

    return Response({'data':'Something bad happend'}, status=status.HTTP_400_BAD_REQUEST) 

