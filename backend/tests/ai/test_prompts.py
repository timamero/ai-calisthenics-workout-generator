import json

import pytest

from app.ai.prompts import build_user_prompt


def _build_prompt(**overrides) -> str:
    """Build a user prompt with sensible defaults, applying any overrides."""
    defaults = {
        "equipment": ["pull-up bar", "resistance bands"],
        "fitness_level": "beginner",
        "target_muscles": ["chest", "back"],
        "duration_minutes": 45,
        # TODO: Update exercise object to match Exercise model
        "available_exercises": [
            {
                "id": 1,
                "name": "Push-up",
                "target_muscles": ["chest", "triceps"],
                "required_equipment": None,
                "difficulty": "beginner",
            }
        ],
    }
    defaults.update(overrides)
    return build_user_prompt(**defaults)


class TestBuildUserPrompt:
    """Tests build_user_prompt function"""

    def test_prompt_includes_equipment(self):
        """Test that prompt includes equipment"""
        equipment = ["pull-up bar", "parallettes"]
        prompt = _build_prompt(equipment=equipment)

        assert "User equipment: pull-up bar, parallettes" in prompt

    def test_prompt_includes_fitness_level(self):
        """Test that prompt includes fitness_level"""
        prompt = _build_prompt(fitness_level="intermediate")

        assert "User fitness level: intermediate" in prompt

    def test_prompt_includes_target_muscles(self):
        """Test that prompt includes target_muscles"""
        target_muscles = ["chest", "shoulders", "triceps"]
        prompt = _build_prompt(target_muscles=target_muscles)

        assert "Target muscle groups:" in prompt
        assert "chest, shoulders, triceps" in prompt

    def test_prompt_includes_duration_minutes(self):
        """Test that prompt includes duration_minutes"""
        prompt = _build_prompt(duration_minutes=30)

        assert "Desired duration: 30 minutes" in prompt

    def test_prompt_includes_trimmed_additional_notes(self):
        """Test that prompt includes trimmed additional_notes"""
        prompt = _build_prompt(additional_notes="  avoid overhead pressing  ")

        assert "Additional notes: avoid overhead pressing" in prompt

    def test_none_additional_notes_render_as_none_in_prompt(self):
        """Test that when additional_notes=None it is rendered as None"""
        prompt = _build_prompt(additional_notes=None)

        assert "Additional notes: None" in prompt

    def test_empty_additional_notes_render_as_none_in_prompt(self):
        """
        Test that providing an empty string for additional_notes
        is rendered as None.
        """
        prompt = _build_prompt(additional_notes="")

        assert "Additional notes: None" in prompt

    def test_whitespace_additional_notes_render_as_none_in_prompt(self):
        """
        Test that providing only whitespace for additional_notes
        results in an empty value after the 'Additional notes:' header.
        """
        prompt = _build_prompt(additional_notes="   \t  ")

        additional_notes_line = next(
            line
            for line in prompt.splitlines()
            if line.strip().startswith("Additional notes:")
        )
        assert additional_notes_line.strip() == "Additional notes:"

    @pytest.mark.skip
    def test_prompt_includes_available_exercises_json(self, sample_exercises):
        """Test that prompt includes json of available exercises to build workout"""
        prompt = _build_prompt(available_exercises=sample_exercises)

        assert "Available exercises (JSON):" in prompt
        assert json.dumps(sample_exercises, indent=2) in prompt

    @pytest.mark.skip
    def test_prompt_includes_workout_structure_instructions(self):
        """
        Test that prompt includes instruction for building workout in the workout data
        json schema
        """
        prompt = _build_prompt()

        assert "warm up" in prompt.lower()
        assert "cool down" in prompt.lower()
        assert "superset" in prompt.lower()
        assert "section" in prompt.lower()

    @pytest.mark.skip
    def test_workout_structure_includes_workout_data_json_schema(
        self,
    ):
        """
        Test that prompt includes workout data json of how sections, supersets, and
        exercises are structured in generated workout
        """
        prompt = _build_prompt()

        assert "workout_data_json_schema" in prompt
        assert '"type": "section"' in prompt
        assert '"type": "superset"' in prompt
        assert '"type": "exercise"' in prompt
