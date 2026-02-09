from django.test import TestCase

# Create your tests here.



class DashboardViewTest(TestCase):
    def test_dashboard_view(self):
        response = self.client.get('/ui_TicketSystem_Dashboard')
        self.assertEqual(response.status_code, 200)
      