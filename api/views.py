from django.shortcuts import render
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.response import Response
from api.models import Products,Reviews
from api.serializers import ProductSerializer,ProductModelSerializer,ReviewSerializers,CartSerializer
from rest_framework.decorators import action
from rest_framework import authentication,permissions

class ProductsView(ModelViewSet):
    serializer_class=ProductModelSerializer
    queryset=Products.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]


    # def list(self,request,*args,**kw):
    #     qs=Products.objects.all()
    #     serializer=ProductModelSerializer(qs,many=True)

    #     return Response(data=serializer.data)

    # def create(self,request,*args,**kw):
    #     serilizer=ProductModelSerializer(data=request.data)
    #     if serilizer.is_valid():
    #         serilizer.save()
    #         # Products.objects.create(**serilizer.validated_data)
    #         return Response(data=serilizer.data)
    #     else:
    #         return Response(data=serilizer.errors)

    # def retrieve(self,request,*args,**kw):
    #     id=kw.get("pk")
    #     qs=Products.objects.get(id=id)
    #     serializer=ProductModelSerializer(qs)
    #     return Response(data=serializer.data)        


    # def destroy(self,request,*args,**kw):
    #     id=kw.get("pk")
    #     Products.objects.get(id=id).delete()
    #     return Response(data="deleted")

    # def update(self,request,*args,**kw):
    #     id=kw.get("pk")
    #     obj=Products.objects.get(id=id)
    #     serializer=ProductModelSerializer(data=request.data,instance=obj)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(data=serializer.data)
    #     else:
    #         return Response(data=serializer.errors)
    #localhost:8000/products/categories/
    #GET
    @action(methods=["get"],detail=False)
    def categories(self,request,*args,**kw):
        qs=Products.objects.values_list('category',flat=True)
        print(qs)
        categories=Products.objects.values_list('category',flat=True).distinct()
        return Response(data=categories)
    #localhost:8000/products/1/add_review/
    @action(methods=["post"],detail=True)
    def add_review(self,request,*args,**kw):
        user=request.user
        product=self.get_object()
        serializer=ReviewSerializers(data=request.data,context={"user":user,"product":product})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    # localhost:8000/products/1/reviews
    # get
    @action(methods=["get"],detail=True)
    def reviews(self,request,*args,**kw):
        product=self.get_object()
        qs=Reviews.objects.filter(product=product)
        serializer=ReviewSerializers(qs,many=True)
        return Response(data=serializer.data)
    
    #localhost:8000/products/1/addto_cart/
    @action(methods=["post"],detail=True)
    def addto_cart(self,request,*args,**kw):
        product=self.get_object()
        user=request.user
        serializer=CartSerializer(data=request.data,context={"product":product,"user":user})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


    
