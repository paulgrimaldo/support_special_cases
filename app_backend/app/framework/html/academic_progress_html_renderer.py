from flask import render_template

from app.domain.html_renderer import HtmlRenderer


class AcademicProgressHtmlRenderer(HtmlRenderer):

    def render(self, data):
        return render_template('academic_progress.html', **data)
