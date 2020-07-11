from flask import render_template

from app.domain.html_renderer import HtmlRenderer


class SpecialCaseLetterHtmlRenderer(HtmlRenderer):

    def render(self, data):
        return render_template('special_case_letter.html', **data)
