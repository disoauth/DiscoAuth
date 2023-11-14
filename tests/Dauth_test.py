from discoauth import AuthUrl
from discoauth.deprecated.url import permissions

TEST_DIS_APP_ID = "1172638888553103371"

async def test_url_build():
    url = await AuthUrl(TEST_DIS_APP_ID, ["identify", "guilds"], "https://tests.com", test=True).makeUrl()
    assert url == "https://discord.com/oauth2/authorize?response_type=code&client_id=1172638888553103371&scope=identify%20guilds&state=1&redirect_uri=https%3A%2F%2Ftests.com"

async def test_perm_build_perms():
    perms = permissions(3) # Check permissions_test.py for the permissions tests
    url = await AuthUrl(TEST_DIS_APP_ID, ["identify", "guilds", "bot"], "https://tests.com", perms, test=True).makeUrl()
    assert url == "https://discord.com/oauth2/authorize?response_type=code&client_id=1172638888553103371&scope=identify%20guilds%20bot&state=1&redirect_uri=https%3A%2F%2Ftests.com&permissions=8"

async def test_perm_build_value():
    perms = permissions(3)
    url = await AuthUrl(TEST_DIS_APP_ID, ["identify", "guilds", "bot"], "https://test.com", perms.value, test=True).makeUrl()
    assert url == "https://discord.com/oauth2/authorize?response_type=code&client_id=1172638888553103371&scope=identify%20guilds%20bot&state=1&redirect_uri=https&3A&3F%2Ftests.com&permissions=8"
