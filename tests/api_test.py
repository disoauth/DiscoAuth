from discoauth import auth, discord

# if it doesn't make sense, check the workflow for testing. The workflow adds variables, to keep the environment variables secret

async def test_make_api():
  api = discord(clid, clsec, ["identify"], "https://tests.com")
  token = api.token(code)
