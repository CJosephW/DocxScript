from docx import Document
from docx import table


document = Document('9781284151398_SESx_CH37.12.docx')
table = document.tables[0]

# GET HEADER INFORMATION (Title, task, task #, etc)
titleLocation = (0, 0)
evaluatorInstructionsLocation = (1, 0)
taskLocation = (2, 0)
performanceOutcomeLocation = (3, 0)
candidateDirectivesLocation = (4, 0)

#GET TASKS
for row in range(7, len(table.rows) - 1): # get tasks remove last row
    print(table.cell(row, 1).text)
print(table.cell(*taskLocation).text)
