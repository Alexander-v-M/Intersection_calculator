from configparser import ConfigParser

config_settings = ConfigParser()
config_settings.read('settings.ini')

class ReadWriteSettings:

    @staticmethod
    def edit_style(to_change: str, to_what: str):

        if to_change == "appearance":
            config_settings.set('style', 'appearance', f'{to_what}')
        else:
            if to_change == "theme":
                config_settings.set('style', 'theme', f'{to_what}')

        with open('settings.ini', 'w') as configfile_style:
            config_settings.write(configfile_style)

    @staticmethod
    def get_style(style_type: str):
        if style_type == "theme":
            return config_settings.get('style', f'{style_type}')

        if style_type == "appearance":
            return config_settings.get('style', f'{style_type}')
