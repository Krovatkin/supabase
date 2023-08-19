import os
import supa_secrets
from supabase import create_client, Client

url = supa_secrets.SUPABASE_URL
key = supa_secrets.SUPABASE_KEY
supabase: Client = create_client(url, key)

# res = supabase.auth.sign_up({
#   "email": supa_secrets.SUPABASE_EMAIL,
#   "password": supa_secrets.SUPABASE_PASS,
# })

data = supabase.auth.sign_in_with_password({"email": supa_secrets.SUPABASE_EMAIL, "password": supa_secrets.SUPABASE_PASS})