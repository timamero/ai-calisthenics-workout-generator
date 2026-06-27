from supabase import create_client, Client

from app.core.config import settings

url: str = settings.supabase_url

if settings.environment == "production":
    key: str = settings.supabase_anon_key
elif settings.environment == "local":
    key: str = settings.supabase_service_role_key


def get_supabase_client() -> Client:
    return create_client(url, key)
