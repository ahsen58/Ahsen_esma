from operation.GenderAnalysis import GenderAnalysis
from operation.AgeAnalysis import AgeAnalysis
from operation.WorkAnalysis import WorkAnalysis
from operation.StudentAnalysis import StudentAnalysis
from operation.PopulationSummary import PopulationSummary
from operation.ReportPrinter import ReportPrinter

class PopulationStatistics:
    def __init__(self, population_data_list):
        self.data = population_data_list
        self.toplam_kisi = len(self.data)
        self.gender  = GenderAnalysis(self.data)
        self.age     = AgeAnalysis(self.data)
        self.work    = WorkAnalysis(self.data)
        self.student = StudentAnalysis(self.data)
        self.summary = PopulationSummary(self.data)
        self.printer = ReportPrinter(self)

    def calculate_gender_percentages(self):
        return self.gender.calculate()

    def calculate_average_age(self):
        return self.age.average_age()

    def calculate_working_percentage(self):
        return self.work.working_percentage()

    def calculate_student_percentage(self):
        return self.student.student_percentage()

    def print_statistics_report(self):
        self.printer.print_report()
