class InvalidPermission(Exception):
    """Raised when a Invalid permission number or permission name is passed

    Attributes:
      permissionInt -- The invalid permission number
    """
    def __init__(self, 
                 permissionInt: int | None = None):
        if permissionInt is None:
            super().__init__("The permission number you passed is invalid")
        elif permissionInt is not None:
            super().__init__(f"The permission number you passed, {permissionInt}, is invalid")
