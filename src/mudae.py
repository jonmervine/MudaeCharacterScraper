from src.ahk import Ahk
from src.parser import Parser
from src.state import State
from src.writer import Writer


class Mudae:
    def __init__(self):
        self.state = State()
        self.state.start()

    def handle_message(self, embed):
        if self.state.get_last_command().startswith('$imab'):
            self.scrape_bundle_series(embed)
        else:
            Writer.write_scraped_data(self.state.get_current_filename(), embed.author.name)
            self.scrape_characters(embed.description)

        self.continuation_check(embed.footer)

    def handle_non_embed_message(self, message):
        bundles = Parser.get_bundles_from_series(message.content)
        for bundle in bundles:
            self.state.add_bundle(bundle)

        self.continuation_check(None)

    def handle_message_edit(self, embed):
        if self.state.get_last_command().startswith('$imab'):
            self.scrape_bundle_series(embed)
        else:
            self.scrape_characters(embed.description)

        self.continuation_check(embed.footer)

    def handle_my_message(self, message):
        self.state.set_last_command(message.content)

    def continuation_check(self, footer):
        if footer:
            current_page = Parser.get_footer_current(footer.text)
            total_pages = Parser.get_footer_total(footer.text)

            if current_page == '1':
                Ahk.ahk_click(total_pages)
            elif current_page == total_pages:
                self.state.get_next_command()
        else:
            self.state.get_next_command()

    def scrape_characters(self, description):
        output_text = Parser.sanitize_characters(description)
        Writer.write_scraped_data(self.state.get_current_filename(), output_text)

    def scrape_bundle_series(self, embed):
        series = Parser.get_series_from_bundle(embed.description)
        for show in series:
            self.state.add_series(show)
