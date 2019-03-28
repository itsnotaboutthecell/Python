'''
    Created By: Alex Powers
    Website: http://www.itsnotaboutthecell.com
    LinkedIn: https://www.linkedin.com/in/alexmpowers/
    Contact: alexmpowers@itsnotaboutthecell.com
'''

partitionID = input('Starting Partition ID?\n')
while not partitionID.isnumeric():
    partitionID = input('Please enter a numeric value.\nStarting Partition ID?\n')

sqlTableName = input ('Server and Table Name?\n')
while not '.' in sqlTableName:
    sqlTableName = input ('Please include a period between server and table name.\nServer and Table Name?\n')

timeStamp = input ('TimeStamp Field?\n')
    
startYear = input('Start Year?\n')
while not startYear.isnumeric() or not len(startYear) == 4:
    startYear = input('Please enter the year in YYYY format.\nStart Year?\n')
    
endYear = input('End Year?\n')
while not endYear.isnumeric() or not len(endYear) == 4:
    endYear = input('Please enter the year in YYYY format.\nEnd Year?\n')

finalPath = ''
for i in range(int(startYear), int(endYear) + 1):
    for j in range(1,13):
        fullPath = str(partitionID) + ',' + '\'' + sqlTableName + '\',\'' + 'SELECT * FROM ' + sqlTableName + ' WHERE EXTRACT(YEAR FROM ' + timeStamp + ') = ' + str(i) + ' AND EXTRACT(MONTH FROM ' + timeStamp + ') = ' + str(j) + '\'' + ' UNION ALL'
        finalPath = finalPath + '\n' + fullPath
        partitionID = int(partitionID) + 1

print(finalPath[:-10])
input("Press Enter to exit...")
