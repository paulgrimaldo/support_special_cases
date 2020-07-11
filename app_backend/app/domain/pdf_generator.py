from .html_renderer import HtmlRenderer


class PdfGenerator:
    def __init__(self, html_renderer: HtmlRenderer):
        self.html_renderer = html_renderer

    def generate(self, data):
        pass
