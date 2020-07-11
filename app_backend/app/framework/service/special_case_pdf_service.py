from datetime import datetime

from app.domain.special_case_data import SpecialCaseData
from app.framework.usecase.create_academic_progress_pdf_use_case import CreateAcademicProgressPdfUseCase
from app.framework.usecase.create_registration_form_pdf_use_case import CreateRegistrationFormPdfUseCase
from app.framework.usecase.create_special_case_letter_pdf_use_case import CreateSpecialCaseLetterPdfUseCase


class SpecialCasePdfService:

    def __init__(self, special_case_data: SpecialCaseData):
        self.special_case_data = special_case_data

    def create_special_case_letter_pdf(self):
        date = datetime.today().strftime('%d/%m/%Y')
        city_with_date = "Santa Cruz de la sierra {}".format(date)
        student = self.special_case_data.student_data
        career = self.special_case_data.career_data
        special_case_classes = self.special_case_data.special_case_classes

        context = {
            'city_with_date': city_with_date,
            'career': career,
            'special_case_classes': special_case_classes,
            'student': student
        }

        use_case = CreateSpecialCaseLetterPdfUseCase()

        return use_case.invoke(context)

    def create_academic_progress_pdf(self):
        student = self.special_case_data.student_data
        classes = self.special_case_data.ordered_classes

        context = {
            'student': student,
            'classes': classes
        }

        use_case = CreateAcademicProgressPdfUseCase()

        return use_case.invoke(context)

    def create_registration_form_pdf(self):
        student = self.special_case_data.student_data
        career = self.special_case_data.career_data
        special_case_classes = self.special_case_data.special_case_classes

        context = {
            'career': career,
            'special_case_classes': special_case_classes,
            'student': student
        }

        use_case = CreateRegistrationFormPdfUseCase()

        return use_case.invoke(context)
