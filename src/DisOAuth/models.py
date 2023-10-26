class UserObj:
    def __init__(self,
                 response) -> None:
        r = response
        self.id = r['id']
        self.username = r['username']
        self.discriminator = r['discriminator']
        if 'global_name' in r:
            self.global_name = r.global_name
        if 'avatar' in r:
            self.avatar = r.avatar
        if 'bot' in r:
            self.bot = r.bot
        else:
            self.bot = False
        if 'system' in r:
            self.system = r.system
        else:
            self.system = False
        self.mfa_enabled = r.mfa_enabled
        self.banner = r.banner
        self.accent_color = r.accent_color
        self.locale = r.locale
        if 'verified' in r:
            self.verified = r.verified
        else:
            self.verified = None
        if 'email' in r:
            self.email = r.email
        else:
            self.email = None
        self.flags = r.flags
        self.premium_type = r.premium_type
        self.public_flags = r.public_flags
        self.avatar_decoration = r.avatar_decoration

    def __getitem__ (self, key):
        return getattr(self, key)