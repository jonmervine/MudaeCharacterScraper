import queue

from src.ahk import Ahk
from src.parser import Parser
from src.writer import Writer


class State:
    current_filename = None
    next_bundles = None
    last_command = None

    def __init__(self):
        self.next_bundles = queue.Queue()

    def start(self):
        self.add_bundle('Trigger')
        self.get_next()

    def get_current_filename(self):
        return self.current_filename

    def __set_current_filename(self, command):
        series = Parser.get_series_from_command(command)
        raw_command = Parser.get_raw_command(command)[1:].strip()

        filename = series + '/' + raw_command + '.txt'
        self.current_filename = filename

    def get_last_command(self):
        return self.last_command

    def set_last_command(self, last_command):
        self.last_command = last_command

    def add_bundle(self, bundle_name):
        Writer.create_directory(bundle_name)
        self.next_bundles.put('$imaawg ' + bundle_name)
        self.next_bundles.put('$imaawg- ' + bundle_name)
        self.next_bundles.put('$imaahg ' + bundle_name)
        self.next_bundles.put('$imaahg- ' + bundle_name)

    def get_next(self):
        command = self.next_bundles.get()
        self.__set_current_filename(command)
        Ahk.ahk_type(command)
