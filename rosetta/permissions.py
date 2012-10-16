from rosetta.conf import settings as rosetta_settings

def user_filter(user, lang, pos):
    if (not rosetta_settings.ENABLE_PERMISSIONS) or user.is_superuser:
        return pos

    result = []
    for po in pos:
        if user.has_perm('rosetta.%s' % lang, po):
            result.append(po)
    return result