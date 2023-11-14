import pytest.mark.parametrize as param

from discoauth import permissions


def check(perms, value: int | None = None):
    assert perms.value == value
    assert perms.administrator is True
    assert perms.stream is False

@param("input,expected", [
    (3, 8),
    ("administrator", 8),
    ([3, 2, 1], 14),
    (["administrator", "ban_members", "kick_members"], 14),
    ([3, "ban_members", 1], 14),
])
def test_base(input, expected):
    perms = permissions(input)
    check(perms, expected)

@param("input,expected",[
    ({3: True, 2: False, 1: True}, 10),
    ({"administrator": True, "ban_members": False, "kick_members": True}, 10) 
]
def test_dict(input, expected):
    perms = permissions(input)
    assert perms.value == expected

async def test_up_int():
    perms = permissions()
    assert perms.value == 0
    await perms.update(3)
    check(perms, 8)


async def test_up_str():
    perms = permissions()
    await perms.update("administrator")
    check(perms, 8)

async def test_up_list():
    perms = permissions()
    await perms.update([3, "ban_members", 1])
    check(perms, 14)

async def test_add_int():
    perms = permissions()
    await perms.add(3)
    check(perms, 8)

async def test_add_str():
    perms = permissions()
    await perms.add("administrator")
    check(perms, 8)

async def test_add_list():
    perms = permissions()
    await perms.add([3, "ban_members", 1])
    check(perms, 14)

async def test_rm_int():
    perms = permissions(3)
    await perms.remove(3)
    assert perms.value == 0
    assert perms.administrator is False

async def test_rm_str():
    perms = permissions("administrator")
    await perms.remove("administrator")
    assert perms.value == 0
    assert perms.administrator is False

async def test_rm_list():
    perms = permissions([3, "ban_members", 1])
    await perms.remove("ban_members")
    assert perms.value == 10
    assert perms.ban_members is False

async def test_group_all():
    perms = permissions()
    await perms.all()
    assert perms.value == 114349209288703

async def test_group_none():
    perms = permissions()
    await perms.all()
    assert perms.value == 114349209288703
    await perms.none()
    assert perms.value == 0

async def test_group_gen():
    perms = permissions()
    await perms.general()
    assert perms.value == 1879573680

async def test_group_allChannel():
    perms = permissions()
    await perms.allChannel()
    assert perms.value == 4937936797521

async def test_group_membership():
    perms = permissions()
    await perms.membership()
    assert perms.value == 1099712954375

async def test_group_text():
    perms = permissions()
    await perms.text()
    assert perms.value == 70903468128320

async def test_group_voice():
    perms = permissions()
    await perms.voice()
    assert perms.value == 40132223697664

async def test_group_stage():
    perms = permissions()
    await perms.stage()
    assert perms.value == 4294967296

async def test_group_stage_mod():
    perms = permissions()
    await perms.stage_moderator()
    assert perms.value == 20971536

async def test_group_elevated():
    perms = permissions()
    await perms.elevated()
    assert perms.value == 1118570553406

async def test_group_advanced():
    perms = permissions()
    await perms.advanced()
    assert perms.value == 8
