import json

from flask import render_template, request, send_file
from flask_cors import cross_origin

from app import create_app
from app.domain.special_case_data import SpecialCaseData
from app.framework.service.documents_service_facade import DocumentServiceFacade

app = create_app()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/v1/careers', methods=['GET'])
@cross_origin()
def get_careers():
    with open('app/data/data.json', encoding="UTF8") as json_file:
        data = json.load(json_file)
        return data


@app.route('/api/v1/generate-documentation', methods=['POST'])
@cross_origin()
def generate_documentation():
    parsed_request = request.get_json()

    print(str(parsed_request))

    special_case_data = SpecialCaseData(parsed_request)
    documents_service_facade = DocumentServiceFacade(special_case_data)

    zip_filename, in_memory_zip = documents_service_facade.generate_documents_and_zip()

    response = send_file(
        in_memory_zip,
        attachment_filename=zip_filename,
        as_attachment=True,
        mimetype="application/zip"
    )

    response.headers["x-suggested-filename"] = zip_filename
    response.headers["Access-Control-Expose-Headers"] = 'x-suggested-filename'
    return response


if __name__ == "__main__":
    app.run(debug=True)
