from unittest.mock import patch
import json

import services
from app import app
app = app.test_client()


class TestApp:
    @patch.object(services, 'add')
    def test_get(self, mock_service_get):
        user_id = 'user_id_value'
        response = app.post('/users/add', data=json.dumps({"user_id": user_id}))
        mock_service_get.assert_called_with(user_id=user_id)
        assert response.status_code == 200

    @patch.object(services, 'delete')
    def test_delete(self, mock_service_delete):
        user_id = 'user_id_value'
        response = app.delete(f'/users/delete/{user_id}')
        mock_service_delete.assert_called_with(user_id=user_id)
        assert response.status_code == 200

    @patch.object(services, 'is_valid')
    def test_is_valid(self, mock_service_is_valid):
        mock_service_is_valid.return_value = True
        user_id = 'user_id_value'
        response = app.get(f'/users/is_valid/{user_id}')
        mock_service_is_valid.assert_called_with(user_id=user_id)
        assert response.status_code == 200
        result = json.loads(response.get_data(as_text=True))
        assert result['is_valid'] is True

        mock_service_is_valid.return_value = False
        response = app.get(f'/users/is_valid/{user_id}')
        assert response.status_code == 200
        result = json.loads(response.get_data(as_text=True))
        assert result['is_valid'] is False

