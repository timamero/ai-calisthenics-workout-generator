import pytest
from pydantic import ValidationError

from app.ai.responses import parse_workout_response


class TestParseWorkoutResponse:
    """Tests parse_workout_response function"""

    @pytest.mark.skip(reason="not implemented yet")
    def test_valid_json_response_is_expected_structure(self, sample_generated_workout):
        """Test that a valid JSON response is parsed correctly"""
        parsed_workout = parse_workout_response(sample_generated_workout)

        assert isinstance(parsed_workout, dict)
        assert "workout" in parsed_workout
        assert "exercises" in parsed_workout["workout"]
        assert isinstance(parsed_workout["workout"]["exercises"], list)

    @pytest.mark.skip(reason="not implemented yet")
    def test_invalid_json_response_raises_exception(self):
        """Test that an invalid JSON response raises an exception"""
        invalid_response = "This is not a valid JSON response"

        with pytest.raises(ValidationError):
            parse_workout_response(invalid_response)

    @pytest.mark.skip(reason="not implemented yet")
    def test_response_with_missing_fields_raises_exception(
        self, sample_generated_workout
    ):
        """Test that a response with missing fields raises an exception"""
        # Remove the 'exercises' field from the sample response
        incomplete_response = sample_generated_workout.copy()
        del incomplete_response["workout"]["workout_data"]

        with pytest.raises(ValidationError):
            parse_workout_response(incomplete_response)
