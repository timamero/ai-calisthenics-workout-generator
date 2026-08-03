import pytest

from app.ai.responses import parse_workout_response


class TestParseWorkoutResponse:
    """Tests parse_workout_response function"""

    @pytest.mark.skip(reason="not implemented yet")
    def test_valid_json_response_is_expected_structure(self, sample_workout_response):
        """Test that a valid JSON response is parsed correctly"""
        parsed_workout = parse_workout_response(sample_workout_response)

        assert isinstance(parsed_workout, dict)
        assert "workout" in parsed_workout
        assert "exercises" in parsed_workout["workout"]
        assert isinstance(parsed_workout["workout"]["exercises"], list)


# TODO: Create sample_workout_response pytest fixture
