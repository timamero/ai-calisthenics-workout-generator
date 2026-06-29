class TestGenerateWorkout:
    """Tests for generate_workout function."""

    async def test_generate_workout_valid_request(
        self, client, sample_generated_workout
    ):
        """Test the successful creation of a generated workout."""

        parameters = {
            "equipment": ["pull up bar"],
            "fitness_level": "beginner",
            "target_muscles": ["upper back"],
            "duration_minutes": 30,
            "additional_notes": "additional notes",
        }

        response = await client.request("POST", "/generate-workout/", json=parameters)

        assert response.status_code == 200
        assert (
            response.json()["workout"]["name"]
            == sample_generated_workout["workout"]["name"]
        )
        assert response.json()["workout"]["equipment"] == parameters["equipment"]

    async def test_generate_workout_validation_error(self, client):
        """Test that invalid request payloads return a 422 response."""

        parameters = {
            "equipment": "pull up bar",
            "fitness_level": "beginner",
            "target_muscles": "upper back",
            "duration_minutes": "PT30M",
            "additional_notes": "additional notes",
        }

        response = await client.request("POST", "/generate-workout/", json=parameters)

        assert response.status_code == 422
