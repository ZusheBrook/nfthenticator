from unittest.mock import patch
import json

import services
from app import app
app = app.test_client()


class TestApp:
    @patch.object(services, 'add')
    def test_get(self, mock_service_get):
        user_id = 'user_id_value'
        app.post('/users/add', data=json.dumps({"user_id": user_id}))
        mock_service_get.assert_called_with(user_id=user_id)
