import zipfile
from io import BytesIO


class Zipper:

    def __init__(self):
        self.zip_in_memory = BytesIO()
        self.zipper = zipfile.ZipFile(self.zip_in_memory, 'w')

    def add_file(self, file_data):
        filename = file_data[0]
        data = file_data[1]

        zip_info = zipfile.ZipInfo(filename)
        zip_info.compress_type = zipfile.ZIP_DEFLATED

        self.zipper.writestr(zip_info, data)

        return self

    def get_zip_in_memory(self):
        self.zipper.close()

        self.zip_in_memory.seek(0)

        return self.zip_in_memory
