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

    return mock_client, mock_table, mock_query


@pytest.fixture
def mock_get_supabase_client(mock_supabase_client):
    """Patch get_supabase_client to return our mock."""
    mock_client, _, _ = mock_supabase_client
    with patch("app.db.exercises.get_supabase_client", return_value=mock_client):
        yield mock_client


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
