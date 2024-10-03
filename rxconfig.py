import reflex as rx

user="postgres.rmjugqvvncicutdrbypg password=[QpcnGWmMbrOKCe0M] host=aws-0-us-west-1.pooler.supabase.com port=6543 dbname=postgres"

config = rx.Config(
    app_name="ATS_web",
    db_url=user
)