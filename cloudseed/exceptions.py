class CloudseedError(RuntimeError):
    '''An unexpected condition occurred'''


class NoProjectInConfig(CloudseedError):
    '''No provider defined in config'''


class ConfigNotFound(CloudseedError):
    '''Cloudseed config not found'''


class InvalidProfile(CloudseedError):
    '''Invalid Cloudseed profile'''


class UnknownConfigProvider(CloudseedError):
    '''Unable to load requester provider'''


class MissingConfigKey(KeyError, CloudseedError):
    '''Missing required config key'''
