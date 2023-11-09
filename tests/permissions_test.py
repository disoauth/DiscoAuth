from DisOAuth import permissions

def test_int():
    perms = permissions(3)
    assert perms.administrator == True
    assert perms.stream == False
    assert perms.value == 8

def test_str():
    perms = permissions("administrator")
    assert perms.administrator == True
    assert perms.stream == False
    assert perms.value == 8

def test_list_int():
    perms = permissions([3, 2, 1])
    assert perms.administrator == True
    assert perms.ban_members == True
    assert perms.kick_members == True
    assert perms.stream == False
    assert perms.connect == False
    assert perms.use_vad == False
    assert perms.value == 14

def test_list_str():
    perms = permissions(["administrator", "ban_members", "kick_members"])
    assert perms.administrator == True
    assert perms.ban_members == True
    assert perms.kick_members == True
    assert perms.stream == False
    assert perms.connect == False
    assert perms.use_vad == False
    assert perms.value == 14

def test_list_mix():
    perms = permissions([3, "ban_members", 1])
    assert perms.administrator == True
    assert perms.ban_members == True
    assert perms.kick_members == True
    assert perms.stream == False
    assert perms.connect == False
    assert perms.use_vad == False
    assert perms.value == 14

def test_dict_int():
    perms = permissions({3: True, 2: False, 1: True})
    assert perms.value == 10

def test_dict_str():
    perms = permissions({"administrator": True, "ban_members": False})
