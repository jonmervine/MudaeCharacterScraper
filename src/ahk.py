class Ahk:
    @staticmethod
    def ahk_type(message):
        with open('../ahk/Commands.txt', 'a', encoding='utf-8') as ahkCommands:
            ahkCommands.write('_TYPE: ' + message + '\n')

    @staticmethod
    def ahk_click(clicks):
        with open('../ahk/Commands.txt', 'a', encoding='utf-8') as ahkCommands:
            ahkCommands.write('_CLICK: ' + clicks + '\n')
