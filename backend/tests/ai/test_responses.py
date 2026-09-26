import pytest
from pydantic import ValidationError

from app.ai.responses import parse_workout_response
from app.schemas.generate_workout import GenerateWorkoutResponseSchema


class TestParseWorkoutResponse:
    """Tests parse_workout_response function"""

    @pytest.mark.skip(reason="not implemented yet")
    def test_valid_json_response_is_expected_structure(self, sample_generated_workout):
        """Test that a valid JSON response is parsed correctly"""
        parsed_workout = parse_workout_response(sample_generated_workout)

        validated = GenerateWorkoutResponseSchema.model_validate(parsed_workout)

        assert isinstance(validated, GenerateWorkoutResponseSchema)
        assert "workout" in validated.model_dump()
        assert "remaining_generations" in validated.model_dump()

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
        # Remove the 'workout_data' field from the sample response
        incomplete_response = sample_generated_workout.copy()
        del incomplete_response["workout"]["workout_data"]

        with pytest.raises(ValidationError):
            parse_workout_response(incomplete_response)
