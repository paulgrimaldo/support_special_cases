from flask import render_template

from app.domain.html_renderer import HtmlRenderer


class RegistrationFormHtmlRenderer(HtmlRenderer):

    def render(self, data):
        return render_template('special_case_registration_form.html', **data)
