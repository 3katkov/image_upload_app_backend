from rest_framework import viewsets, generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from .models import ImageModel, UserProfile, Plan, ImageModel
from .serializers import ImageSerializer, UserProfileSerializer, PlanSerializer, ImageSerializer
from . import utils

"""
PROJECT REQUIREMENT 4A. 
ADMINS SHOULD BE ABLE TO CONFIGURATE ARBIRARY PLANS WITH CUSTOM 
THUMBNAIL SIZES, PRESENCE OF ORIGINAL LINK, GENERATION OF EXPIRING LINK 

ONLY ADMINS ARE ABLE TO CHANGE THE PLAN OF CUSTUMER
"""

class PlanList(generics.CreateAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = (IsAdminUser,)


    def post(self, request, *args, **kwargs):
        serializer = PlanSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=200)
        else: 
            return Response(serializer.errors, status=400)

    
    def get(self, request, *args, **kwargs):
        serializer = PlanSerializer(Plan.objects.all(), many=True)
        
        return Response(serializer.data, status=200)

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsAdminUser,)


"""
PROJECT REQUIREMENT 2A. 
USERS SHOULD BE ABLE TO UPLOAD IMAGES 
VIA HTTP REQUEST  


PROJECT REQUIREMENT 2B. 
USERS SHOULD BE ABLE TO LIST THEIR IMAGES

"""
class ImageUploadView(generics.CreateAPIView):
    queryset = ImageModel.objects.all()
    serializer_class = ImageSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = (IsAuthenticated, IsAuthenticatedOrReadOnly)

    def post(self, request, *args, **kwargs):
        user = self.request.user
        serializer = ImageSerializer(data=request.data)

        if serializer.is_valid():
            if request.user.is_authenticated:
                serializer.save(user=user)
                user = UserProfile.objects.get(user=user)
                utils.process_image(serializer.instance, user.plan)
            
                return Response(serializer.data, status=200)
            else: 
                return Response(serializer.errors, status=400)

    def get(self, request, *args, **kwargs):
        user = self.request.user
        serializer = ImageSerializer(ImageModel.objects.filter(user=user).order_by('-upload_time'), many=True)
        return Response(serializer.data, status=200)



"""
PROJECT REQUIRMENT 3.4

USERS ON ENTERPRISE PLAN SHOULD BE ABLE TO FETCH LINK FOR PREVIOUSLEY UPLOADED IMAGE 
THAT EXPIRES AFTER X SECONDS. 

USER CAN SPECIFY X SCONDS TO BE BETWEEN 30 AND 300.

"""

# last_uploaded_image_id = ImageModel.objects.all().order_by('-id').first()
# print(last_uploaded_image_id)

# class TemporaryLinkView(generics.GenericAPIView):
#     queryset = ImageModel.objects.all()
#     serializer_class = ImageSerializer

#     def get(self, request, *args, **kwargs):
#         image_id = self.kwargs.get('pk')
#         try:
#             image = ImageModel.objects.get(pk=image_id)
#         except ImageModel.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#         try:
#             seconds = int(request.query_params.get('seconds', 300))
#             if seconds < 300 or seconds > 30000:
#                 raise ValidationError("Seconds should be between 300 and 30000.")
#         except ValueError:
#             return Response(status=status.HTTP_400_BAD_REQUEST)

#         # Check if the link has expired
#         now = datetime.now(pytz.utc)
#         if (now - image.upload_time).total_seconds() > seconds:
#             return Response(status=status.HTTP_410_GONE)

#         # Serve the image file
#         file_path = os.path.join(settings.MEDIA_ROOT, str(image.image))
#         response = FileResponse(open(file_path, 'rb'))
#         return response