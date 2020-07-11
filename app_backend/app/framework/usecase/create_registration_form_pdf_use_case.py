from app.domain.pdf_generator import PdfGenerator
from app.domain.use_case import UseCase
from app.framework.html.registration_form_html_renderer import RegistrationFormHtmlRenderer
from app.framework.pdf.default_pdf_generator import DefaultPdfGenerator


class CreateRegistrationFormPdfUseCase(UseCase):

    def __init__(self, pdf_generator: PdfGenerator = DefaultPdfGenerator(RegistrationFormHtmlRenderer())):
        super().__init__(pdf_generator)
