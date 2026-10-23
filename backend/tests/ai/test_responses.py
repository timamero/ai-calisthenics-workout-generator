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
        invalid_response = {
            "workout": {
                "name": "Sample Workout",
                "workout_data": "This should be a dict, but it's a string",
                "notes": "This is a summary",
            },
            "remaining_generations": 5,
        }

        with pytest.raises(ValidationError):
            parse_workout_response(invalid_response)

    @pytest.mark.skip(reason="not implemented yet")
    def test_response_with_missing_fields_raises_exception(self):
        """Test that a response with missing fields raises an exception"""
        # Remove the 'workout_data' field from the sample response
        incomplete_response = {
            "workout": {
                "name": "Sample Workout",
                # 'workout_data' is missing
                "notes": "This is a summary",
            },
            "remaining_generations": 5,
        }

        with pytest.raises(ValidationError):
            parse_workout_response(incomplete_response)

    @pytest.mark.skip(reason="not implemented yet")
    def test_response_without_exercise_element_raises_exception(
        self, sample_generated_workout
    ):
        """Test that a workout without an exercise element raises an exception"""
        workout_without_exercises = sample_generated_workout.copy()
        workout_without_exercises["workout"] = sample_generated_workout[
            "workout"
        ].copy()
        workout_data = sample_generated_workout["workout"]["workout_data"].copy()
        workout_data["data"] = []

        for item in sample_generated_workout["workout"]["workout_data"]["data"]:
            if item["type"] == "section":
                section = item.copy()
                section["items"] = [
                    nested_item
                    for nested_item in item["items"]
                    if nested_item["type"] != "exercise"
                ]
                section["items"] = [
                    nested_item
                    for nested_item in section["items"]
                    if nested_item["type"] != "superset"
                ]
                workout_data["data"].append(section)
            elif item["type"] == "superset":
                superset = item.copy()
                superset["exercises"] = []
                workout_data["data"].append(superset)

        workout_without_exercises["workout"]["workout_data"] = workout_data

        with pytest.raises(ValidationError):
            parse_workout_response(workout_without_exercises)
