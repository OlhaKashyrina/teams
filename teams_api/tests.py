from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Person, Team


class TeamsTests(APITestCase):

    def test_create_team(self):
        """
        Ensure we can create a new team
        """
        url = '/teams/teams'
        data = {'name': 'Test Team'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_all_teams(self):
        """
        Ensure we can get a list of all teams
        """
        url = '/teams/teams'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_person(self):
        """
        Ensure we can create a new person
        """

        #create a team first
        self.client.post('/teams/teams', {'name': 'Test Team'}, format='json')

        url = '/teams/people'
        data = {'first_name': 'Test', 'last_name': 'Person', 'email': 'tp@ukr.net', 'team': 1}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_all_people(self):
        """
        Ensure we can get a list of all people
        """
        url = '/teams/people'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_wrong_email_format(self):
        """
        Test if wrong email format is recognized as an error
        """
        #create a team first
        self.client.post('/teams/teams', {'name': 'Test Team'}, format='json')

        url = '/teams/people'
        data = {'first_name': 'Test', 'last_name': 'Person', 'email': 'tpukr.net', 'team': 1}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_no_team_assigned(self):
        """
        Test if it is possible to create a person with no team
        """
        #create a team first
        self.client.post('/teams/teams', {'name': 'Test Team'}, format='json')

        url = '/teams/people'
        data = {'first_name': 'Test', 'last_name': 'Person', 'email': 'tp@ukr.net'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
