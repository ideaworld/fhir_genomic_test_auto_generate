'''
test code
@author: Bowen
'''

import csv
from create_test_case import *

possibles = globals().copy()
possibles.update(locals())

if __name__ == '__main__':
    # file_list = ['DiagnosticReport.csv', 'DiagnosticRequest.csv', 'Observation.csv', 'Sequence.csv', 'FamilyMemberHistory.csv']
    # types = []
    # for filename in file_list:
    #     csv_reader = csv.reader(open(filename, 'r'))
    #     for index, row in enumerate(csv_reader):
    #         if index == 0:
    #             continue
    #         if row[1].lower() not in types:
    #             types.append(row[1].lower())
    # non_function_types = ['resource','extension', 'id', 'identifier', 'backboneelement','meta','see observation.referencerange']
    print create_cases('codeableconcept', 3, None)
