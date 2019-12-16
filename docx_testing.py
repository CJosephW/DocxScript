from docx import Document
from docx import table
import os



# GET HEADER INFORMATION (Title, task, task #, etc)
titleLocation = (0, 0)
evaluatorInstructionsLocation = (1, 0)
taskLocation = (2, 0)
performanceOutcomeLocation = (3, 0)
candidateDirectivesLocation = (4, 0)

#GET TASKS
for filename in os.listdir("path"):
    document = Document(#'path' +filename)
    table = document.tables[0]

    for row in range(7, len(table.rows) - 1): # get tasks remove last row
        print(table.cell(row, 1).text)
        print(table.cell(*taskLocation).text)
