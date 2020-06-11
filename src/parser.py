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
        series = command.split(' ', 1)[1]
        return Parser.__sanitize_for_windows(series)

    @staticmethod
    def get_raw_command(command):
        return command.split(' ', 1)[0]

    @staticmethod
    def get_series_from_bundle(data):
        lines = data.split('\n')
        series = []
        for line in lines:
            series.append(line[2:].split(' (*')[0])

        return series

    @staticmethod
    def get_bundles_from_series(data):
        lines = data.split('\n')
        lines.pop(0)
        bundles = []
        for line in lines:
            bundles.append(line[5:].split('**')[0])

        return bundles

    @staticmethod
    def __sanitize_for_windows(series_name):
        return series_name.replace('<', '').replace('>', '').replace(':', '').replace('/', '').replace('\\', '').replace('|', '').replace('?', '').replace('*', '')