from .pdf_generator import PdfGenerator


class UseCase:

    def __init__(self, pdf_generator: PdfGenerator):
        self.pdf_generator = pdf_generator

    def invoke(self, data):
        return self.pdf_generator.generate(data)
