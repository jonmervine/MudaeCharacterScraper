class Parser:
    @staticmethod
    def get_footer_total(footer):
        return footer.split('/')[1].strip()

    @staticmethod
    def get_footer_current(footer):
        return footer.split('/')[0].split(' ')[1].strip()

    @staticmethod
    def sanitize_characters(description):
        return description.replace('**', '').replace('💞', '')

    @staticmethod
    def get_series_from_command(command):
        return command.split(' ', 1)[1]

    @staticmethod
    def get_raw_command(command):
        return command.split(' ', 1)[0]
