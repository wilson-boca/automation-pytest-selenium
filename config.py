class Config:
    def __init__(self, env):

        supported_envs = ['dev', 'qa']

        if env.lower() not in supported_envs:
            raise Exception(f'{env} is not supported')

        self.base_url = {
            'dev': 'https://mydev-env.com',
            'qa': 'https://myqa-env.com'
        }[env]

        self.app_port = {
            'dev': 8080,
            'qa': 8081
        }[env]
