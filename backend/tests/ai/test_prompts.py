class TestBuildUserPrompt:
    """Tests build_user_prompt function"""

    def test_prompt_includes_equipment(self):
        """Test that prompt includes equipment"""
        pass

    def test_prompt_includes_fitness_level(self):
        """Test that prompt includes fitness_level"""
        pass

    def test_prompt_includes_target_muscles(self):
        """Test that prompt includes target_muscles"""
        pass

    def test_prompt_includes_duration_minutes(self):
        """Test that prompt includes duration_minutes"""
        pass

    def test_prompt_includes_trimmed_additional_notes(self):
        """Test that prompt includes trimmed additional_notes"""
        pass

    def test_none_additional_notes_render_as_none_in_prompt(self):
        """Test that when additional_notes=None it is rendered as None"""
        pass

    def test_empty_additional_notes_render_as_none_in_prompt(self):
        """
        Test that providing an empty string for additional_notes
        is rendered as None.
        """
        pass

    def test_whitespace_additional_notes_render_as_none_in_prompt(self):
        """
        Test that providing only whitespace for additional_notes
        results in an empty value after the 'Additional notes:' header.
        """
        pass

    def test_prompt_includes_available_exercises_json(self):
        """Test that prompt includes json of available exercises to build workout"""
        pass

    def test_prompt_includes_workout_structure_instructions(self):
        """
        Test that prompt includes instruction for building workout in the workout data
        json schema
        """
        pass

    def test_workout_structure_includes_workout_data_json_schema(
        self,
    ):
        """
        Test that prompt includes workout data json of how sections, supersets, and
        exercises are structured in generated workout
        """
        pass
