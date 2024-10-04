from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Team, Person
from .serializers import TeamSerializer, PersonSerializer

class TeamListApiView(APIView):

    def get(self, request, *args, **kwargs):
        '''
        List all teams
        '''
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        '''
        Create a team with given team data
        '''
        data = {
            'name': request.data.get('name')
        }
        serializer = TeamSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonListApiView(APIView):

    def get(self, request, *args, **kwargs):
        '''
        List all people
        '''
        people = Person.objects.all()
        serializer = PersonSerializer(people, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        '''
        Create a person with given data
        '''
        data = {
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
            'email': request.data.get('email'),
            'team': request.data.get('team')
        }
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeamDetailApiView(APIView):

    def get_object(self, team_id):
        '''
        Helper method to get the object with given team_id
        '''
        try:
            return Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return None

    def get(self, request, team_id, *args, **kwargs):
        '''
        Retrieves the team with given team_id
        '''
        team_instance = self.get_object(team_id)
        if not team_instance:
            return Response(
                {"res": "Object with this team_id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = TeamSerializer(team_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, team_id, *args, **kwargs):
        '''
        Updates the team with given team_id if exists
        '''
        team_instance = self.get_object(team_id)
        if not team_instance:
            return Response(
                {"res": "Object with this team_id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'name': request.data.get('name')
        }
        serializer = TeamSerializer(instance = team_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, team_id, *args, **kwargs):
        '''
        Deletes the team with given team_id if exists
        '''
        team_instance = self.get_object(team_id)
        if not team_instance:
            return Response(
                {"res": "Object with this team_id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        team_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )


class PersonDetailApiView(APIView):

    def get_object(self, person_id):
        '''
        Helper method to get the object with given person_id
        '''
        try:
            return Person.objects.get(id=person_id)
        except Person.DoesNotExist:
            return None

    def get(self, request, person_id, *args, **kwargs):
        '''
        Retrieves the person with given person_id
        '''
        person_instance = self.get_object(person_id)
        if not person_instance:
            return Response(
                {"res": "Object with this person_id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = PersonSerializer(person_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, person_id, *args, **kwargs):
        '''
        Updates the person with given person_id if exists
        '''
        person_instance = self.get_object(person_id)
        if not person_instance:
            return Response(
                {"res": "Object with this person_id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
            'email': request.data.get('email'),
            'team': request.data.get('team')
        }
        serializer = PersonSerializer(instance = person_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, person_id, *args, **kwargs):
        '''
        Deletes the person with given person_id if exists
        '''
        person_instance = self.get_object(person_id)
        if not person_instance:
            return Response(
                {"res": "Object with this person_id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        person_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
