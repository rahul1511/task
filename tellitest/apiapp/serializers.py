from rest_framework import serializers
from apiapp.models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
	class Meta:
		model = BlogPost
		fields = '__all__'