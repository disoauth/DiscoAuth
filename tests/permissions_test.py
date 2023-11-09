from DisOAuth import permissions

def test_int():
    perms = permissions(3)
    assert perms.value == 8

def test_str():
    perms = permissions("administrator")
    assert perms.value == 8

def test_list_int():
    perms = permissions([3, 2, 1])
    assert perms.value == 14

def test_list_str():
    perms = permissions(["administrator", "ban_members", "kick_members"])
    assert perms.value == 14

def test_list_mix():
    perms = permissions([3, "ban_members", 1])
    assert perms.value == 14

