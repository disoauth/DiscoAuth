class UserObj:
    def __init__(self,
                 response) -> None:
        r = response
        self.id = r['id']
        self.username = r['username']
        self.discriminator = r['discriminator']
        if 'global_name' in r:
            self.global_name = r['global_name']
        if 'avatar' in r:
            self.avatar = r['avatar']
        if 'bot' in r:
            self.bot = r['bot']
        else:
            self.bot = False
        if 'system' in r:
            self.system = r['system']
        else:
            self.system = False
        self.mfa_enabled = r['mfa_enabled']
        self.banner = r['banner']
        self.accent_color = r['accent_color']
        self.locale = r['locale']
        if 'verified' in r:
            self.verified = r['verified']
        else:
            self.verified = None
        if 'email' in r:
            self.email = r['email']
        else:
            self.email = None
        self.flags = r['flags']
        self.premium_type = r['premium_type']
        self.public_flags = r['public_flags']
        if 'avatar_decoration' in r:
            self.avatar_decoration = r['avatar_decoration']

    def __getitem__ (self, key):
        return getattr(self, key)


class GuildObj:
    def __init__(self,
                 response) -> None:
        r = response
        self.id = r['id']
        self.name = r['name']
        if "icon" in r:
            self.icon = r['icon']
            self.icon_url = f"https://cdn.discordapp.com/icons/{self.id}/{self.icon}.png"
        else:
            self.icon = None
            self.icon_url = None
        if "splash" in r:
            self.splash = r['splash']
        else:
            self.splash = None
        if "discovery_splash" in r:
            self.discovery_splash = r['discovery_splash']
        if "owner" in r:
            self.owner = r['owner']
        else:
            self.owner = None
        self.onwer_id = r['owner_id']
        if "permissions" in r:
            self.permissions = r['permissions']
            self.perms = r['permissions']
        else:
            self.permisssion = None
            self.perms = None
        if "region" in r:
            self.region = r['region']
        else:
            self.region = None
        if "afk_channel_id" in r:
            self.afk_channel_id = r['afk_channel_id']
        else:
            self.afk_channel_id = None
        if "afk_timeout" in r:
            self.afk_timeout = r['afk_timeout']
        else:
            self.afk_timeout = None
        if "widget_enabled" in r:
            self.widget_enabled = True
        else:
            self.widget_enabled = False
        if "widget_channel_id" in r:
            self.widget_channel_id = r['widget_channel_id']
        else:
            self.widget_channel_id = None
        self.verification_level = r['verification_level']
        self.default_message_notifications = r['default_message_notifications']
        self.explicit_content_filter = r['explicit_content_filter']
        self.roles = r['roles']
        self.emojis = r['emojis']
        self.features = r['features']
        self.mfa_level = r['mfa_level']
        if "application_id" in r:
            self.application_id = r['application_id']
        else:
            self.application_id = None
        if "system_channel_id" in r:
            self.system_channel_id = r['system_channel_id']
        else:
            self.system_channel_id = None
        if "system_channel_flags" in r:
            self.system_channel_flags = r['system_channel_flags']
        else:
            self.system_channel_flags = None
        if "rules_channel_id" in r:
            self.rules_channel_id = r['rules_channel_id']
        else:
            self.rules_channel_id = None
        if "max_presences" in r:
            self.max_presences = r['max_presences']
        else:
            self.max_presences = None
        if "max_members" in r:
            self.max_members = r['max_members']
        else:
            self.max_members = None
        if "vanity_url_code" in r:
            self.vanity_url_code = r['vanity_url_code']
        else:
            self.vanity_url_code = None
        if "description" in r:
            self.description = r['description']
        else:
            self.description = None
        if "banner" in r:
            self.banner = r['banner']
        else:
            self.banner = None
        self.premium_tier = r['premium_tier']
        if "premium_subscription_count" in r:
            self.premium_subscription_count = r['premium_subscription_count']
        else:
            self.premium_subscription_count = None
        if "preferred_locale" in r:
            self.preferred_locale = r['preferred_locale']
        else:
            self.preferred_locale = None
        if "public_updates_channel_id" in r:
            self.public_updates_channel_id = r['public_updates_channel_id']
        else:
            self.public_updates_channel_id = None
        if "max_video_channel_users" in r:
            self.max_video_channel_users = r['max_video_channel_users']
        else:
            self.max_video_channel_users = None
        if "max_stage_video_channel_users" in r:
            self.max_stage_video_channel_users = r['max_stage_video_channel_users']
        else:
            self.max_stage_video_channel_users = None
        if "approximate_member_count" in r:
            self.approximate_member_count = r['approximate_member_count']
        else:
            self.approximate_member_count = None
        if "approximate_presence_count" in r:
            self.approximate_presence_count = r['approximate_presence_count']
        else:
            self.approximate_presence_count = None
        if "welcome_screen" in r:
            self.welcome_screen = r['welcome_screen']
        else:
            self.welcome_screen = None
        if "nsfw_level" in r:
            self.nsfw_level = r['nsfw_level']
        else:
            self.nsfw_level = None
        if "stickers" in r:
            self.stickers = r['stickers']
        else:
            self.stickers = None
        if "premium_progress_bar_enabled" in r:
            self.premium_progress_bar_enabled = r['premium_progress_bar_enabled']
        else:
            self.premium_progress_bar_enabled = False
        if "safety_alerts_channel_id" in r:
            self.safety_alerts_channel_id = r['safety_alerts_channel_id']
        else:
            self.safety_alerts_channel_id = None

    def __getitem__(self, key):
        return getattr(self, key)
