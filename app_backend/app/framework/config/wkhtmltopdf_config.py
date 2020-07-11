import os

import pdfkit

dirname = os.path.dirname(__file__)
config = pdfkit.configuration(wkhtmltopdf=os.path.join(dirname, "../../../lib/windows/wkhtmltopdf/bin/wkhtmltopdf.exe"))

pdf_options = {
    'page-size': 'Letter',
}
