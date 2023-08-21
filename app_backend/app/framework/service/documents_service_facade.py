from datetime import datetime

from app.domain.special_case_data import SpecialCaseData
from app.framework.service.special_case_pdf_service import SpecialCasePdfService
from app.shared.zipper import Zipper

ZIP_FILENAME_TEMPLATE = 'Caso especial - {}, {}.zip'
REGISTRATION_FORM_FILENAME = 'Boleta de inscripción.pdf'
ACADEMIC_PROGRESS_FILENAME = 'Malla curricular.pdf'
SPECIAL_CASE_LETTER_FILENAME = 'Carta de caso especial.pdf'


class DocumentServiceFacade:

    def __init__(self, special_case_data: SpecialCaseData):
        self.special_case_data = special_case_data

    def generate_documents_and_zip(self):
        pdf_service = SpecialCasePdfService(self.special_case_data)

        academic_progress_pdf = pdf_service.create_academic_progress_pdf()
        letter_pdf = pdf_service.create_special_case_letter_pdf()
        registration_form_pdf = pdf_service.create_registration_form_pdf()

        zipper = Zipper()

        zipper \
            .add_file((ACADEMIC_PROGRESS_FILENAME, academic_progress_pdf)) \
            .add_file((REGISTRATION_FORM_FILENAME, registration_form_pdf)) \
            .add_file((SPECIAL_CASE_LETTER_FILENAME, letter_pdf))

        # zipper \
        #     .add_file((ACADEMIC_PROGRESS_FILENAME, academic_progress_pdf)) \
        #     .add_file((SPECIAL_CASE_LETTER_FILENAME, letter_pdf))

        return self.__generate_zip_filename(), zipper.get_zip_in_memory()

    def __generate_zip_filename(self):
        student_name = self.special_case_data.student_data["name"]
        date_time = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

        return ZIP_FILENAME_TEMPLATE.format(student_name, date_time)
