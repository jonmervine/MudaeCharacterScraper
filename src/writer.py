import os
import pathlib


class Writer:
    @staticmethod
    def write_scraped_data(filename, text):
        filepath = os.path.join('../resources/', filename)

        if not pathlib.Path(filepath).parent.absolute().exists():
            os.makedirs(pathlib.Path(filepath).parent.absolute(), exist_ok=True)

        with open(filepath, 'a', encoding='utf-8') as outfile:
            outfile.write(text)
            outfile.write('\n')