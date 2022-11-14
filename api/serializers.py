from rest_framework import serializers
from api.models import Products,Reviews,Carts

class ProductSerializer(serializers.Serializer):
    name=serializers.CharField()
    description=serializers.CharField()
    category=serializers.CharField()
    price=serializers.IntegerField()
    image=serializers.ImageField(read_only=True)

    def update(self, instance, validated_data):
        instance.name=validated_data.get("name")
        instance.category=validated_data.get("category")
        instance.price=validated_data.get("price")
        instance.description=validated_data.get("description")
        instance.save()
        return instance


class ProductModelSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)

    class Meta:
        model=Products
        fields=["id","name","description","category","price","image"]


class ReviewSerializers(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    product=serializers.CharField(read_only=True)

    class Meta:
        
        model=Reviews
        fields=["comment","rating","product","user"]


    def create(self, validated_data):
        user=self.context.get("user")
        product=self.context.get("product")

        return Reviews.objects.create(**validated_data,user=user,product=product)


class CartSerializer(serializers.ModelSerializer):
    product=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    date=serializers.CharField(read_only=True)
    class Meta:
        model=Carts
        fields=["product","user","date"]
    def create(self, validated_data):
        user=self.context.get("user")
        product=self.context.get("product")
        return Carts.objects.create(user=user,product=product,**validated_data)

# localhost:8000/users/carts

