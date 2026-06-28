from unittest.mock import Mock
from app.db.exercises import get_exercises
from app.schemas.exercise import ExerciseFilterParams


class TestGetExercises:
    """Tests for get_exercises function."""

    def test_get_exercises_no_filters(
        self, mock_get_supabase_client, mock_supabase_client, sample_exercises
    ):
        """Test getting all exercises with no filters applied."""
        mock_client, mock_table, mock_query = mock_supabase_client
        mock_response = Mock()
        mock_response.data = sample_exercises
        mock_query.execute.return_value = mock_response

        filter_params = ExerciseFilterParams()
        result = get_exercises(filter_params)

        assert result == sample_exercises
        mock_client.table.assert_called_once_with("exercises")
        mock_table.select.assert_called_once_with("*")
        mock_query.execute.assert_called_once()

    def test_get_exercises_with_muscle_filter(
        self, mock_get_supabase_client, mock_supabase_client, sample_exercises
    ):
        """Test filtering exercises by target muscles."""
        mock_client, mock_table, mock_query = mock_supabase_client
        mock_response = Mock()
        mock_response.data = [sample_exercises[0]]
        mock_query.execute.return_value = mock_response

        filter_params = ExerciseFilterParams(muscles=["chest"])
        result = get_exercises(filter_params)

        assert result == [sample_exercises[0]]
        mock_query.or_.assert_called_once()
        mock_query.execute.assert_called_once()

    def test_get_exercises_with_multiple_muscles(
        self, mock_get_supabase_client, mock_supabase_client, sample_exercises
    ):
        """Test filtering exercises by multiple target muscles."""
        mock_client, mock_table, mock_query = mock_supabase_client
        mock_response = Mock()
        mock_response.data = sample_exercises
        mock_query.execute.return_value = mock_response

        filter_params = ExerciseFilterParams(muscles=["chest", "back"])
        result = get_exercises(filter_params)

        assert result == sample_exercises
        # or_ should be called with muscles condition
        mock_query.or_.assert_called_once()

    def test_get_exercises_with_equipment_filter(
        self, mock_get_supabase_client, mock_supabase_client, sample_exercises
    ):
        """Test filtering exercises by required equipment."""
        mock_client, mock_table, mock_query = mock_supabase_client
        mock_response = Mock()
        mock_response.data = [sample_exercises[1]]
        mock_query.execute.return_value = mock_response

        filter_params = ExerciseFilterParams(equipments=["pull-up bar"])
        result = get_exercises(filter_params)

        assert result == [sample_exercises[1]]
        mock_query.or_.assert_called_once()
        mock_query.execute.assert_called_once()

    def test_get_exercises_with_muscles_and_equipment(
        self, mock_get_supabase_client, mock_supabase_client, sample_exercises
    ):
        """Test filtering exercises by both muscles and equipment."""
        mock_client, mock_table, mock_query = mock_supabase_client
        mock_response = Mock()
        mock_response.data = sample_exercises
        mock_query.execute.return_value = mock_response

        filter_params = ExerciseFilterParams(muscles=["chest"], equipments=["dumbbell"])
        result = get_exercises(filter_params)

        assert result == sample_exercises
        # or_ should be called once with combined conditions
        mock_query.or_.assert_called_once()

    def test_get_exercises_with_difficulty_filter(
        self, mock_get_supabase_client, mock_supabase_client, sample_exercises
    ):
        """Test filtering exercises by difficulty level."""
        mock_client, mock_table, mock_query = mock_supabase_client
        mock_response = Mock()
        mock_response.data = [sample_exercises[0]]
        mock_query.execute.return_value = mock_response

        filter_params = ExerciseFilterParams(difficulty="beginner")
        result = get_exercises(filter_params)

        assert result == [sample_exercises[0]]
        mock_query.eq.assert_called()
        mock_query.execute.assert_called_once()

    def test_get_exercises_with_emphasis_filter(
        self, mock_get_supabase_client, mock_supabase_client, sample_exercises
    ):
        """Test filtering exercises by emphasis type."""
        mock_client, mock_table, mock_query = mock_supabase_client
        mock_response = Mock()
        mock_response.data = sample_exercises
        mock_query.execute.return_value = mock_response

        filter_params = ExerciseFilterParams(emphasis="strength")
        result = get_exercises(filter_params)

        assert result == sample_exercises
        mock_query.eq.assert_called()
        mock_query.execute.assert_called_once()

    def test_get_exercises_with_search_query(
        self, mock_get_supabase_client, mock_supabase_client, sample_exercises
    ):
        """Test searching exercises by name with 'q' parameter."""
        mock_client, mock_table, mock_query = mock_supabase_client
        mock_response = Mock()
        mock_response.data = [sample_exercises[0]]
        mock_query.execute.return_value = mock_response

        filter_params = ExerciseFilterParams(q="push")
        result = get_exercises(filter_params)

        assert result == [sample_exercises[0]]
        mock_query.ilike.assert_called_once()
        mock_query.execute.assert_called_once()

    def test_get_exercises_with_all_filters(
        self, mock_get_supabase_client, mock_supabase_client, sample_exercises
    ):
        """Test filtering exercises with all filter parameters combined."""
        mock_client, mock_table, mock_query = mock_supabase_client
        mock_response = Mock()
        mock_response.data = [sample_exercises[0]]
        mock_query.execute.return_value = mock_response

        filter_params = ExerciseFilterParams(
            q="push",
            muscles=["chest"],
            equipments=["dumbbell"],
            difficulty="beginner",
            emphasis="strength",
        )
        result = get_exercises(filter_params)

        assert result == [sample_exercises[0]]
        # Verify all filter methods were called
        mock_query.or_.assert_called()
        mock_query.eq.assert_called()
        mock_query.ilike.assert_called_once()
        mock_query.execute.assert_called_once()

    def test_get_exercises_empty_result(
        self, mock_get_supabase_client, mock_supabase_client
    ):
        """Test when no exercises match the filters."""
        mock_client, mock_table, mock_query = mock_supabase_client
        mock_response = Mock()
        mock_response.data = []
        mock_query.execute.return_value = mock_response

        filter_params = ExerciseFilterParams(muscles=["nonexistent"])
        result = get_exercises(filter_params)

        assert result == []
        mock_query.execute.assert_called_once()

    def test_get_exercises_error_handling(
        self, mock_get_supabase_client, mock_supabase_client, capsys
    ):
        """Test that errors are caught and printed."""
        mock_client, mock_table, mock_query = mock_supabase_client
        mock_query.execute.side_effect = Exception("Supabase connection error")

        filter_params = ExerciseFilterParams()
        result = get_exercises(filter_params)

        # Function should return None on error (due to no return statement in except)
        assert result is None
        captured = capsys.readouterr()
        assert "Error fetching exercises" in captured.out
