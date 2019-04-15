# from django.contrib.auth.models import User 
from .models import *
from rest_framework import serializers


# class UserSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = User
# 		fields = ['username','groups','password',]

class ScrumGoalSerializer(serializers.ModelSerializer):

	class Meta:
		model = ScrumyGoals
		fields = ['visible','id','goal_name','goal_status','user','project']


class ScrumUserSerializer(serializers.ModelSerializer):
	# scrumygoals_set = ScrumGoalSerializer(many=True)
	class Meta:
		model = ScrumUser
		fields = ['id','nickname']


class ScrumProjectRoleSerializer(serializers.ModelSerializer):
	user = ScrumUserSerializer()
	scrumygoals_set = ScrumGoalSerializer(many=True)
	class Meta:
		model = ScrumProjectRole
		fields = ['user','id','scrumygoals_set' ]   

class ScrumProjectSerializer(serializers.HyperlinkedModelSerializer):
    scrumprojectrole_set = ScrumProjectRoleSerializer(many=True)
    class Meta:
        model = ScrumProject
        fields = ['name', 'id', 'project_count','scrumprojectrole_set']