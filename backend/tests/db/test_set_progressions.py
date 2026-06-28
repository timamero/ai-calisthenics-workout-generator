from unittest.mock import Mock

import pytest

from app.db.set_progressions import get_set_progressions_list


class TestGetSetProgressionsList:
    def test_get_set_progressions_list_success(
        self,
        mock_get_set_progressions_supabase_client,
        sample_set_progressions,
    ):
        mock_client = mock_get_set_progressions_supabase_client
        mock_table = mock_client.table.return_value
        mock_query = mock_table.select.return_value
        mock_query.order.return_value = mock_query

        mock_response = Mock()
        mock_response.data = sample_set_progressions
        mock_query.execute.return_value = mock_response

        result = get_set_progressions_list()

        assert len(result) == len(sample_set_progressions)
        assert result[0].id == sample_set_progressions[0]["id"]
        assert result[0].name == sample_set_progressions[0]["name"]

        mock_client.table.assert_called_once_with("set_progressions")
        mock_table.select.assert_called_once_with("*")
        mock_query.order.assert_called_once_with("display_order")
        mock_query.execute.assert_called_once()

    def test_get_set_progressions_list_raises_and_logs(
        self,
        mock_get_set_progressions_supabase_client,
        capsys,
    ):
        mock_client = mock_get_set_progressions_supabase_client
        mock_table = mock_client.table.return_value
        mock_query = mock_table.select.return_value
        mock_query.order.return_value = mock_query
        mock_query.execute.side_effect = Exception("Supabase failure")

        with pytest.raises(Exception, match="Supabase failure"):
            get_set_progressions_list()

        captured = capsys.readouterr()
        assert "Error fetching challenges and assists" in captured.out
