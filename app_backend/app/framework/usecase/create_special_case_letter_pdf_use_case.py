from app.domain.pdf_generator import PdfGenerator
from app.domain.use_case import UseCase
from app.framework.html.special_case_letter_html_renderer import SpecialCaseLetterHtmlRenderer
from app.framework.pdf.default_pdf_generator import DefaultPdfGenerator


class CreateSpecialCaseLetterPdfUseCase(UseCase):

    def __init__(self, pdf_generator: PdfGenerator = DefaultPdfGenerator(SpecialCaseLetterHtmlRenderer())):
        super().__init__(pdf_generator)
