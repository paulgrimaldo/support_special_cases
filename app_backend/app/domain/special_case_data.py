def _is_special_case_class(class_data):
    return "type" in class_data and class_data["type"] == "special_case"


class SpecialCaseData:

    def __init__(self, data):
        self.data = data
        self.ordered_classes = {}
        self.special_case_classes = list()
        self.student_data = None
        self.career_data = None
        self.init()

    def init(self):
        self.__transform_ordered_classes()
        self.__transform_special_case_classes()
        self.__transform_student_data()
        self.__transform_career_data()

    def __transform_ordered_classes(self):
        for semester_key, semester_classes in self.data["career_data"]["classes"].items():
            dict_element = {semester_key: semester_classes}

            dict_element.update(self.ordered_classes)

            self.ordered_classes = dict_element

    def __transform_special_case_classes(self):
        for semester_classes in self.ordered_classes.values():

            for class_data in semester_classes:

                if _is_special_case_class(class_data):
                    self.special_case_classes.append(class_data)

    def __transform_student_data(self):
        self.student_data = self.data["student"]

    def __transform_career_data(self):
        self.career_data = {
            'name': self.data["career_data"]["name"],
            'director': self.data["career_data"]["director"]
        }
