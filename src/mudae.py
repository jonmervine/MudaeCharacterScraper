from src.ahk import Ahk
from src.parser import Parser
from src.state import State
from src.writer import Writer


class Mudae:
    def __init__(self):
        self.state = State()
        self.state.start()

    def handle_message(self, embed):
        Writer.write_scraped_data(self.state.get_current_filename(), embed.author.name)
        self.scrape_characters(embed.description)

        if embed.footer:
            Ahk.ahk_click(Parser.get_footer_total(embed.footer.text))
        else:
            self.state.get_next()

    def handle_message_edit(self, embed):
        self.scrape_characters(embed.description)

        self.continuation_check(embed.footer)

    def scrape_characters(self, description):
        output_text = Parser.sanitize_characters(description)
        Writer.write_scraped_data(self.state.get_current_filename(), output_text)

    def continuation_check(self, footer):
        if footer:
            current_page = Parser.get_footer_current(footer.text)
            total_pages = Parser.get_footer_total(footer.text)

            if current_page == total_pages:
                self.state.get_next()

    def handle_my_message(self, message):
        self.state.set_last_command(message.content)
