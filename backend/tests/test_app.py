import unittest
from unittest.mock import patch
import json

import services
from models import User
from app import app
app = app.test_client()


class TestApp:
    @patch.object(services, 'get')
    def test_get(self, mock_service_get):
        user_obj = User(user_name='david')
        mock_service_get.return_value = user_obj
        response = app.get('/users/get?user_name=david')

        mock_service_get.assert_called_with(user_name='david')
        response_data = json.loads(response.get_data(as_text=True))
        unittest.TestCase().AssertDictEquals(user_obj.__dict__, response_data)
