import reflex as rx
from ATS_web.keys.keys import URL, PASS


user=f"postgres.{URL} password=[{PASS}] host=aws-0-us-west-1.pooler.supabase.com port=6543 dbname=postgres"

config = rx.Config(
    app_name="ATS_web",
    db_url=user
)