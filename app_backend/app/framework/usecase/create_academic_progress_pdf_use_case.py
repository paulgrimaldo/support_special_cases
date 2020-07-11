from app.domain.pdf_generator import PdfGenerator
from app.domain.use_case import UseCase
from app.framework.html.academic_progress_html_renderer import AcademicProgressHtmlRenderer
from app.framework.pdf.default_pdf_generator import DefaultPdfGenerator


class CreateAcademicProgressPdfUseCase(UseCase):

    def __init__(self, pdf_generator: PdfGenerator = DefaultPdfGenerator(AcademicProgressHtmlRenderer())):
        super().__init__(pdf_generator)
