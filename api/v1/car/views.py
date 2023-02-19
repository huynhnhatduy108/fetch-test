from api.base.api_view import  CustomAPIView
from api.base.serializers import ExceptionResponseSerializer
from api.v1.car.schemas import PARAMETER_SEARCH_CAR, PARAMETER_CAR_BY_BRAND
from api.v1.car.serializers import CreateUpdateCarSerializer
from models.car.models import Car
from rest_framework import status
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from django.db.models import Q,F

class CarView(CustomAPIView):
    @extend_schema(
        operation_id='Get list car',
        summary='Get list car',
        tags=["A. car"],
        parameters=PARAMETER_SEARCH_CAR,
        description='Get list car',
        responses={
            status.HTTP_200_OK: None,
            status.HTTP_401_UNAUTHORIZED:ExceptionResponseSerializer,
            status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
        },
        examples=[
            # EXAMPLE_RESPONSE_TASK,
        ]
    )
    def get_list_car(self, request):
        cars = Car.objects

        keywork =request.query_params.get("keyword",None)
        if keywork:
            cars= cars.filter(name__icontains=keywork)
        
        cars = cars.annotate(brand_name=F("brand__name")
                ).values("id", "name", "color", "logo","brand_name",
                        "description","created_at", "updated_at"
                ).order_by("-id")
        
        self.paginate(cars)
        data = self.response_paging(self.paging_list)  

        result ={
            "data":data,
            "mess":"Get list car success!"
        }
        return Response(result, status=status.HTTP_200_OK)

    @extend_schema(
        operation_id='Get list car by brand',
        summary='Get list car by brand',
        tags=["A. car"],
        parameters=PARAMETER_CAR_BY_BRAND,
        description='Get list car by brand',
        responses={
            status.HTTP_200_OK: None,
            status.HTTP_401_UNAUTHORIZED:ExceptionResponseSerializer,
            status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
        },
        examples=[
            # EXAMPLE_RESPONSE_TASK,
        ]
    )
    def get_list_car_by_brand(self, request, pk):
        cars = Car.objects.filter(brand=pk)
        
        cars = cars.annotate(brand_name=F("brand__name")
                ).values("id", "name", "color", "logo","brand_name",
                        "description","created_at", "updated_at"
                ).order_by("-id")
        
        self.paginate(cars)
        data = self.response_paging(self.paging_list)  

        result ={
            "data":data,
            "mess":"Get list car by brand success!"
        }
        return Response(result, status=status.HTTP_200_OK)
    
    @extend_schema(
        operation_id='Get info car',
        summary='Get info car',
        tags=["A. car"],
        description='Get info car',
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
        car = Car.objects.filter(pk=pk
                ).annotate(brand_name=F("brand__name")
                ).values("id", "name", "color", "logo","brand_name",
                         "description","created_at", "updated_at").first()
        if not car:
            return Response({"mess": "car not found!"}, status=status.HTTP_400_BAD_REQUEST)
        result ={
            "data":car,
            "mess":"Get info car success!"
        }
        return Response(result, status=status.HTTP_200_OK)

    @extend_schema(
            operation_id='Create car',
            summary='Create car',
            tags=["A. car"],
            description='Create car',
            parameters=None,
            request =CreateUpdateCarSerializer,
            responses={
                status.HTTP_200_OK: None,
                status.HTTP_401_UNAUTHORIZED:ExceptionResponseSerializer,
                status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
            },
            examples=[
                # EXAMPLE_RESPONSE_TASK,
            ]
        )
    def create_car(self, request):
        serializer = CreateUpdateCarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        name = None
        if "name" in serializer.validated_data:
            name = serializer.validated_data['name']

        color = None
        if "color" in serializer.validated_data:
            color = serializer.validated_data['color']

        logo = None
        if "logo" in serializer.validated_data:
            logo = serializer.validated_data['logo']

        description = None
        if "description" in serializer.validated_data:
            description = serializer.validated_data['description']

        brand = None
        if "brand" in serializer.validated_data:
            brand = serializer.validated_data['brand']

        car = Car.objects.create(name = name, color = color, brand_id = brand, logo = logo, description = description)

        result = { "mess": "Create car success!", 
                   "data":{"id":car.id}}
        return Response(result, status=status.HTTP_201_CREATED)
    
    @extend_schema(
            operation_id='Update car',
            summary='Update car',
            tags=["A. car"],
            description='Update car',
            parameters=None,
            request = CreateUpdateCarSerializer,
            responses={ 
                status.HTTP_200_OK: None,
                status.HTTP_401_UNAUTHORIZED:ExceptionResponseSerializer,
                status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
            },
            examples=[
                # EXAMPLE_RESPONSE_TASK,
            ]
        )
    def update_car(self, request ,pk):
        serializer = CreateUpdateCarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        car = Car.objects.filter(pk=pk).first()
        if not car:
            return Response({"mess": "car do not exist!"}, status=status.HTTP_400_BAD_REQUEST)
    
        if "name" in serializer.validated_data:
            name = serializer.validated_data['name']
            car.name = name
        
        if "color" in serializer.validated_data:
            color = serializer.validated_data['color']
            car.color = color

        if "logo" in serializer.validated_data:
            logo = serializer.validated_data['logo']
            car.logo = logo

        if "description" in serializer.validated_data:
            description = serializer.validated_data['description']
            car.description = description

        if "brand" in serializer.validated_data:
            brand = serializer.validated_data['brand']
            car.brand_id = brand
        car.save()

        result = { "mess": "Update car success!", 
                   "data":{"id":car.id}}
        
        return Response(result, status=status.HTTP_201_CREATED)

    @extend_schema(
            operation_id='Delete car',
            summary='Delete car',
            tags=["A. car"],
            description='Delete car',
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
    def delete_car(self, request ,pk):
        car = Car.objects.filter(pk=pk).first()
        if not car:
            return Response({"mess": "car not found!"}, status=status.HTTP_400_BAD_REQUEST)
        car.delete()  

        result = {"mess": "Delete car success!","data":None}
        return Response(result, status=status.HTTP_200_OK)





