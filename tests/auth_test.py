from discoauth import auth, permissions

TEST_DIS_APP_ID = "1172638888553103371"

async def test_url_build():
    url = await auth(TEST_DIS_APP_ID, ["identify", "guilds"], "https://tests.com", test=True).url()
    assert url == "https://discord.com/oauth2/authorize?response_type=code&client_id=1172638888553103371&scope=identify%20guilds&state=1&redirect_uri=https%3A%2F%2Ftests.com"

async def test_perm_build_perms():
    perms = permissions(3) # Check permissions_test.py for the permissions tests
    url = await auth(TEST_DIS_APP_ID, ["identify", "guilds", "bot"], "https://tests.com", perms, test=True).url()
    assert url == "https://discord.com/oauth2/authorize?response_type=code&client_id=1172638888553103371&scope=identify%20guilds%20bot&state=1&redirect_uri=https%3A%2F%2Ftests.com&permissions=8"

async def test_perm_build_value():
    perms = permissions(3) # Check permissions_test.py for the permissions tests
    url = await auth(TEST_DIS_APP_ID, ["identify", "guilds", "bot"], "https://tests.com", perms.value, test=True).url()
    assert url == "https://discord.com/oauth2/authorize?response_type=code&client_id=1172638888553103371&scope=identify%20guilds%20bot&state=1&redirect_uri=https%3A%2F%2Ftests.com&permissions=8"
