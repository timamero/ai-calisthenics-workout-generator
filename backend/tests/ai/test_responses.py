import json

import pytest

from app.ai.responses import parse_workout_response
from app.schemas.generate_workout import GenerateWorkoutResponseSchema


class TestParseWorkoutResponse:
    """Tests parse_workout_response function"""

    @pytest.mark.skip(reason="not implemented yet")
    def test_valid_json_response_is_expected_structure(
        self, sample_generated_workout_json
    ):
        """Test that a valid JSON response is parsed correctly"""
        parsed_workout = parse_workout_response(sample_generated_workout_json)

        assert isinstance(parsed_workout, GenerateWorkoutResponseSchema)
        assert parsed_workout.workout.name == "Stub calisthenics workout"
        assert parsed_workout.remaining_generations == 20

    @pytest.mark.skip(reason="not implemented yet")
    def test_malformed_json_response_raises_descriptive_exception(self):
        """Test that malformed JSON raises a descriptive exception"""
        malformed_response = '{"workout": '

        with pytest.raises(ValueError, match="JSON"):
            parse_workout_response(malformed_response)

    @pytest.mark.skip(reason="not implemented yet")
    def test_response_with_invalid_field_type_raises_descriptive_exception(
        self, sample_generated_workout
    ):
        """Test that an invalid field type raises a descriptive exception"""
        invalid_response = sample_generated_workout.copy()
        invalid_response["workout"] = sample_generated_workout["workout"].copy()
        invalid_response["workout"]["workout_data"] = "not an object"

        with pytest.raises(ValueError, match="workout_data"):
            parse_workout_response(json.dumps(invalid_response))

    @pytest.mark.skip(reason="not implemented yet")
    def test_response_with_missing_workout_data_raises_descriptive_exception(
        self, sample_generated_workout
    ):
        """Test that missing workout data raises a descriptive exception"""
        incomplete_response = sample_generated_workout.copy()
        incomplete_response["workout"] = sample_generated_workout["workout"].copy()
        del incomplete_response["workout"]["workout_data"]

        with pytest.raises(ValueError, match="workout_data"):
            parse_workout_response(json.dumps(incomplete_response))

    @pytest.mark.skip(reason="not implemented yet")
    def test_response_with_no_exercise_element_raises_descriptive_exception(
        self, sample_workout_without_exercises
    ):
        """Test that a workout without any exercise raises a descriptive exception"""
        with pytest.raises(ValueError, match="exercise"):
            parse_workout_response(json.dumps(sample_workout_without_exercises))

    @pytest.mark.skip(reason="not implemented yet")
    def test_section_nested_exercise_is_accepted(self, sample_generated_workout):
        """Test that an exercise nested in a section is accepted"""
        section_response = sample_generated_workout.copy()
        section_response["workout"] = sample_generated_workout["workout"].copy()
        section_response["workout"]["workout_data"] = {
            "data": [sample_generated_workout["workout"]["workout_data"]["data"][1]]
        }

        parsed_workout = parse_workout_response(json.dumps(section_response))

        assert isinstance(parsed_workout, GenerateWorkoutResponseSchema)

    @pytest.mark.skip(reason="not implemented yet")
    def test_superset_nested_exercise_is_accepted(self, sample_generated_workout):
        """Test that an exercise nested in a superset is accepted"""
        superset_response = sample_generated_workout.copy()
        superset_response["workout"] = sample_generated_workout["workout"].copy()
        superset_response["workout"]["workout_data"] = {
            "data": [sample_generated_workout["workout"]["workout_data"]["data"][2]]
        }

        parsed_workout = parse_workout_response(json.dumps(superset_response))

        assert isinstance(parsed_workout, GenerateWorkoutResponseSchema)
