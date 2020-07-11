import pdfkit

from app.domain.html_renderer import HtmlRenderer
from app.framework.config.wkhtmltopdf_config import config as wkhtmltopdf_config
from app.framework.config.wkhtmltopdf_config import pdf_options


class DefaultPdfGenerator:
    def __init__(self, html_renderer: HtmlRenderer):
        self.html_renderer = html_renderer

    def generate(self, data):
        rendered_html = self.html_renderer.render(data)

        return pdfkit.from_string(rendered_html, False, configuration=wkhtmltopdf_config, options=pdf_options)
