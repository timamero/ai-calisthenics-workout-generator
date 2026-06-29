import pytest
from httpx import AsyncClient, ASGITransport
from unittest.mock import Mock, patch

from app.main import app


@pytest.fixture
async def client():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as ac:
        yield ac


@pytest.fixture
def mock_supabase_client():
    """Mock Supabase client with chainable query builder."""
    mock_client = Mock()
    mock_table = Mock()
    mock_query = Mock()

    # Setup the chain: client.table().select()
    mock_client.table.return_value = mock_table
    mock_table.select.return_value = mock_query

    # Setup chainable methods (or_, eq, ilike)
    mock_query.or_.return_value = mock_query
    mock_query.eq.return_value = mock_query
    mock_query.ilike.return_value = mock_query
    mock_query.order.return_value = mock_query

    return mock_client, mock_table, mock_query


@pytest.fixture
def mock_get_exercises_supabase_client(mock_supabase_client):
    """Patch get_supabase_client to return our mock."""
    mock_client, _, _ = mock_supabase_client
    with patch("app.db.exercises.get_supabase_client", return_value=mock_client):
        yield mock_client


@pytest.fixture
def mock_get_set_progressions_supabase_client(mock_supabase_client):
    """Patch get_supabase_client to return our mock."""
    mock_client, _, _ = mock_supabase_client
    with patch("app.db.set_progressions.get_supabase_client", return_value=mock_client):
        yield mock_client


@pytest.fixture
def sample_generated_workout():
    """Sample generated workout data."""
    return {
        "workout": {
            "name": "Stub calisthenics workout",
            "equipment": "pull up bar",
            "fitness_level": "beginner",
            "target_muscles": "upper back",
            "duration_minutes": "PT30M",
            "additional_notes": "additional notes",
            "workout_data": [],
        },
        "remaining_generations": 20,
    }


@pytest.fixture
def sample_exercises():
    """Sample exercise data."""
    return [
        {
            "id": 1,
            "name": "Push-up",
            "target_muscles": ["chest", "triceps"],
            "required_equipment": None,
            "emphasis": "strength",
            "difficulty": "beginner",
            "tags": ["upper body"],
            "instructions": ["Lower body to ground", "Push back up"],
            "default_tracking_types": ["reps"],
        },
        {
            "id": 2,
            "name": "Pull-up",
            "target_muscles": ["back", "biceps"],
            "required_equipment": ["pull-up bar"],
            "emphasis": "strength",
            "difficulty": "intermediate",
            "tags": ["upper body"],
            "instructions": ["Pull body up", "Lower down"],
            "default_tracking_types": ["reps"],
        },
    ]


@pytest.fixture
def sample_set_progressions():
    """Sample set progressions data based on provided payload."""
    return [
        {
            "id": 1,
            "created_at": "2025-10-09T18:42:45.389275+00:00",
            "updated_at": None,
            "name": "Ring Height",
            "value_type": "int",
            "value_options": None,
            "value_int_difficulty_direction": "descending",
            "value_int_unit": "in",
            "display_order": 1,
            "description": "Height of ring from the floor.",
            "measure_instructions": None,
            "type": "challenge",
        },
        {
            "id": 2,
            "created_at": "2025-10-09T18:42:45.389275+00:00",
            "updated_at": None,
            "name": "Hand width",
            "value_type": "int",
            "value_options": None,
            "value_int_difficulty_direction": "ascending",
            "value_int_unit": "in",
            "display_order": 2,
            "description": "Distance between hands.",
            "measure_instructions": None,
            "type": "challenge",
        },
        {
            "id": 3,
            "created_at": "2025-10-09T18:42:45.389275+00:00",
            "updated_at": None,
            "name": "Lean Angle (Horizontal)",
            "value_type": "int",
            "value_options": None,
            "value_int_difficulty_direction": "ascending",
            "value_int_unit": "deg",
            "display_order": 3,
            "description": "Angle of arm relative to floor.",
            "measure_instructions": None,
            "type": "challenge",
        },
        {
            "id": 4,
            "created_at": "2025-10-09T18:42:45.389275+00:00",
            "updated_at": None,
            "name": "Resistance Band",
            "value_type": "options",
            "value_options": ["Extra Light", "Light", "Medium", "Heavy", "Extra Heavy"],
            "value_int_difficulty_direction": None,
            "value_int_unit": None,
            "display_order": 4,
            "description": None,
            "measure_instructions": None,
            "type": "challenge",
        },
        {
            "id": 5,
            "created_at": "2025-10-09T18:42:45.389275+00:00",
            "updated_at": None,
            "name": "Weight",
            "value_type": "int",
            "value_options": None,
            "value_int_difficulty_direction": "ascending",
            "value_int_unit": "lb",
            "display_order": 5,
            "description": None,
            "measure_instructions": None,
            "type": "challenge",
        },
        {
            "id": 6,
            "created_at": "2025-10-09T18:42:45.389275+00:00",
            "updated_at": None,
            "name": "Weight",
            "value_type": "int",
            "value_options": None,
            "value_int_difficulty_direction": "ascending",
            "value_int_unit": "kg",
            "display_order": 6,
            "description": None,
            "measure_instructions": None,
            "type": "challenge",
        },
        {
            "id": 7,
            "created_at": "2025-10-09T18:42:45.389275+00:00",
            "updated_at": None,
            "name": "Resistance Band",
            "value_type": "options",
            "value_options": ["Extra Heavy", "Heavy", "Medium", "Light", "Extra Light"],
            "value_int_difficulty_direction": None,
            "value_int_unit": None,
            "display_order": 7,
            "description": None,
            "measure_instructions": None,
            "type": "assist",
        },
        {
            "id": 8,
            "created_at": "2025-10-09T18:42:45.389275+00:00",
            "updated_at": None,
            "name": "Lean Angle (Vertical)",
            "value_type": "int",
            "value_options": None,
            "value_int_difficulty_direction": "descending",
            "value_int_unit": "deg",
            "display_order": 8,
            "description": "Angle of legs relative to floor.",
            "measure_instructions": None,
            "type": "assist",
        },
        {
            "id": 11,
            "created_at": "2025-10-09T18:42:45.389275+00:00",
            "updated_at": None,
            "name": "Bar Height",
            "value_type": "int",
            "value_options": None,
            "value_int_difficulty_direction": "descending",
            "value_int_unit": "in",
            "display_order": 9,
            "description": None,
            "measure_instructions": None,
            "type": "challenge",
        },
        {
            "id": 12,
            "created_at": "2025-10-09T18:42:45.389275+00:00",
            "updated_at": None,
            "name": "Elevated Feet Height",
            "value_type": "int",
            "value_options": None,
            "value_int_difficulty_direction": "ascending",
            "value_int_unit": "in",
            "display_order": 11,
            "description": "Distance of feet from floor.",
            "measure_instructions": None,
            "type": "challenge",
        },
        {
            "id": 13,
            "created_at": "2025-10-09T18:42:45.389275+00:00",
            "updated_at": None,
            "name": "Bench Height",
            "value_type": "int",
            "value_options": None,
            "value_int_difficulty_direction": "descending",
            "value_int_unit": "in",
            "display_order": 12,
            "description": None,
            "measure_instructions": None,
            "type": "assist",
        },
        {
            "id": 14,
            "created_at": "2025-10-09T18:42:45.389275+00:00",
            "updated_at": None,
            "name": "Distance From Wall",
            "value_type": "int",
            "value_options": None,
            "value_int_difficulty_direction": "ascending",
            "value_int_unit": "in",
            "display_order": 13,
            "description": None,
            "measure_instructions": None,
            "type": "assist",
        },
        {
            "id": 15,
            "created_at": "2025-10-09T18:42:45.389275+00:00",
            "updated_at": None,
            "name": "Lean Distance",
            "value_type": "int",
            "value_options": None,
            "value_int_difficulty_direction": "ascending",
            "value_int_unit": "in",
            "display_order": 15,
            "description": "Distance of forward lean",
            "measure_instructions": "Place tape on the floor where your fingertips "
            "are. Measure the distance from the tape to where your nose, or marker "
            "on your shirt, touches the ground at the bottom of the rep.",
            "type": "challenge",
        },
    ]
