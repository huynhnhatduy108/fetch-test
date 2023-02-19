from api.base.api_view import  CustomAPIView
from api.base.serializers import ExceptionResponseSerializer
from api.v1.brand.schemas import PARAMETER_SEARCH_BRAND
from api.v1.brand.serializers import CreateUpdateBrandSerializer
from models.brand.models import Brand
from rest_framework import status
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from django.db.models import Q

class BrandView(CustomAPIView):
    @extend_schema(
        operation_id='Get list brand',
        summary='Get list brand',
        tags=["B. brand"],
        parameters=PARAMETER_SEARCH_BRAND,
        description='Get list brand',
        # parameters=None,
        responses={
            status.HTTP_200_OK: None,
            status.HTTP_401_UNAUTHORIZED:ExceptionResponseSerializer,
            status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
        },
        examples=[
            # EXAMPLE_RESPONSE_TASK,
        ]
    )
    def get_list_brand(self, request):
        brands = Brand.objects.all().values("id", "name", "created_at", "updated_at").order_by("-id")
        
        self.paginate(brands)
        data = self.response_paging(self.paging_list)  

        result ={
            "data":data,
            "mess":"Get list brand success!"
        }
        return Response(result, status=status.HTTP_200_OK)
    
    @extend_schema(
        operation_id='Get info brand',
        summary='Get info brand',
        tags=["B. brand"],
        description='Get info brand',
        parameters=None,
        responses={
            status.HTTP_200_OK: None,
            status.HTTP_401_UNAUTHORIZED:ExceptionResponseSerializer,
            status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
        },
        examples=[
            # EXAMPLE_RESPONSE_TASK,
        ]
    )
    def get_info(self, request, pk):
        brand = Brand.objects.filter(pk=pk).values("id","name",).first()
        if not brand:
            return Response({"mess": "brand not found!"}, status=status.HTTP_400_BAD_REQUEST)
        result ={
            "data":brand,
            "mess":"Get info brand success!"
        }
        return Response(result, status=status.HTTP_200_OK)

    @extend_schema(
            operation_id='Create brand',
            summary='Create brand',
            tags=["B. brand"],
            description='Create brand',
            parameters=None,
            request =CreateUpdateBrandSerializer,
            responses={
                status.HTTP_200_OK: None,
                status.HTTP_401_UNAUTHORIZED:ExceptionResponseSerializer,
                status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
            },
            examples=[
                # EXAMPLE_RESPONSE_TASK,
            ]
        )
    def create_brand(self, request):
        serializer = CreateUpdateBrandSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        name = None
        if "name" in serializer.validated_data:
            name = serializer.validated_data['name']

        brand = Brand.objects.create(name = name)

        result = { "mess": "Create brand success!", 
                   "data":{"id":brand.id}}
        return Response(result, status=status.HTTP_201_CREATED)
    
    @extend_schema(
            operation_id='Update brand',
            summary='Update brand',
            tags=["B. brand"],
            description='Update brand',
            parameters=None,
            request = CreateUpdateBrandSerializer,
            responses={ 
                status.HTTP_200_OK: None,
                status.HTTP_401_UNAUTHORIZED:ExceptionResponseSerializer,
                status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
            },
            examples=[
                # EXAMPLE_RESPONSE_TASK,
            ]
        )
    def update_brand(self, request ,pk):
        serializer = CreateUpdateBrandSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        brand = Brand.objects.filter(pk=pk).first()
        if not brand:
            return Response({"mess": "brand do not exist!"}, status=status.HTTP_400_BAD_REQUEST)
    
        if "name" in serializer.validated_data:
            name = serializer.validated_data['name']
            brand.name = name
        
        brand.save()

        result = { "mess": "Update brand success!", 
                   "data":{"id":brand.id}}
        
        return Response(result, status=status.HTTP_201_CREATED)

    @extend_schema(
            operation_id='Delete brand',
            summary='Delete brand',
            tags=["B. brand"],
            description='Delete brand',
            parameters=None,
            responses={
                status.HTTP_200_OK: None,
                status.HTTP_401_UNAUTHORIZED:ExceptionResponseSerializer,
                status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
            },
            examples=[
                # EXAMPLE_RESPONSE_TASK,
            ]
        )
    def delete_brand(self, request ,pk):
        brand = Brand.objects.filter(pk=pk).first()
        if not brand:
            return Response({"mess": "brand not found!"}, status=status.HTTP_400_BAD_REQUEST)
        brand.delete()  

        result = {"mess": "Delete brand success!","data":None}
        return Response(result, status=status.HTTP_200_OK)





