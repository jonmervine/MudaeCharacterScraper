import os


class Writer:
    @staticmethod
    def write_scraped_data(filename, text):
        with open(os.path.join('../resources/', filename), 'a', encoding='utf-8') as outfile:
            outfile.write(text)
            outfile.write('\n')

    @staticmethod
    def create_directory(bundle_name):
        path_to_series = os.path.join('../resources', bundle_name)
        os.makedirs(path_to_series, exist_ok=True)
