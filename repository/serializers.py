from rest_framework import serializers
from .models import Repository,RepositoryContributor,Star_Repo
from accounts.models import MyUser
from project.models import Project,ProjectAccess
from project.serializers import ProjectListSerializer

class RepositoryCreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model=MyUser
        fields=['id','username','profile_pic']

class ProjectNameSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields=['project_name']

class RepositorySerializer(serializers.ModelSerializer):
    created_by=RepositoryCreatorSerializer()
    project_id=ProjectNameSerializer()
    contributors_count=serializers.SerializerMethodField('get_contributors_count')
    def get_contributors_count(self,obj):
        count=RepositoryContributor.objects.filter(repo_id=obj.id).count()
        return count
    class Meta:
        model=Repository
        fields="__all__"

class RepositoryCreateSerializer(serializers.ModelSerializer):
    project_name=serializers.CharField(max_length=200)
    class Meta:
        model=Repository
        fields=("repo_name","repo_description","project_name")

class AddContributorSerializer(serializers.ModelSerializer):
    project_name=serializers.CharField(max_length=200)
    repo_name=serializers.CharField(max_length=200)
    class Meta:
        model=RepositoryContributor
        fields="__all__"

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = MyUser
        fields = ["id","username","first_name","last_name","email","profile_pic","bio","dob"]

class GetContributorSerializer(serializers.ModelSerializer):
    user_id = MyUserSerializer()
    is_manager=serializers.SerializerMethodField('get_manager')
    def get_manager(self,obj):
        projectAccess=ProjectAccess.objects.get(project_id=obj.repo_id.project_id,user_id=obj.user_id).is_manager
        return projectAccess
    class Meta:
        model=RepositoryContributor
        fields="__all__"

class GetUserRepositorySerializer(serializers.ModelSerializer):
    created_by=MyUserSerializer()
    project_id=ProjectNameSerializer()
    stars=serializers.SerializerMethodField('get_stars_count')
    def get_stars_count(self,obj):
        count=Star_Repo.objects.filter(star_repo=obj).count()
        return count
    contributors_count=serializers.SerializerMethodField('get_contributors_count')
    def get_contributors_count(self,obj):
        count=RepositoryContributor.objects.filter(repo_id=obj.id).count()
        return count
    class Meta:
        model=Repository
        fields="__all__"

class StarRepoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Star_Repo
        fields="__all__"

class RecentContributionSerializer(serializers.ModelSerializer):
    project_id=ProjectListSerializer()
    contributors_count=serializers.SerializerMethodField('get_contributors_count')
    def get_contributors_count(self,obj):
        count=RepositoryContributor.objects.filter(repo_id=obj.id).count()
        return count
    created_by = MyUserSerializer()
    class Meta:
        model=Repository
        fields=["id","repo_name","repo_description","created_by","created_at","project_id","contributors_count"]