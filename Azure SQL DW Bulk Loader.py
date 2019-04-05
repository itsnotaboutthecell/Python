'''
    Created By: Alex Powers
    Website: http://www.itsnotaboutthecell.com
    LinkedIn: https://www.linkedin.com/in/alexmpowers/
    Contact: alexmpowers@itsnotaboutthecell.com
    
    Accompanying Article: http://angryanalyticsblog.azurewebsites.net/index.php/2019/03/28/sync-your-on-prem-dw-to-azure-dw-with-3-adf-pipelines/
    
'''

def stringBuilder(partitionData, ID, ServerTableName, timeStamp = None, startYear = None, endYear = None):

    finalPath = ',' + '\'' + ServerTableName + '\',\'' + 'SELECT * FROM ' + ServerTableName + '\''
    if partitionData == 'n':
        print(ID + finalPath)
    else:
        concatPath = ''
        for i in range(int(startYear), int(endYear) + 1):
            for j in range(1,13):
                fullPath = str(ID) + finalPath + ' WHERE EXTRACT(YEAR FROM ' + timeStamp + ') = ' + str(i) + ' AND EXTRACT(MONTH FROM ' + timeStamp + ') = ' + str(j) + '\',\'' + 'N\'' + ' UNION ALL'
                concatPath = concatPath + '\n' + fullPath
                ID = int(ID) + 1

    print(concatPath[:-10])

partitionOption = input('Does the dataset need partitioned? (Y/N)\n').lower()
while not partitionOption in ('y','n'):
    partitionOption = input('Please enter the single character (Y/N).\nDoes the dataset need partitioned? (Y/N)\n').lower()

partitionID = input('Starting Partition ID?\n')
while not partitionID.isnumeric():
    partitionID = input('Please enter a numeric value.\nStarting Partition ID?\n')

sqlServerName = input ('Server Name?\n')
sqlTableName = input ('Table Name?\n')

serverAndTable = (sqlServerName + '.' + sqlTableName).upper()

if partitionOption == 'y':
    timeStamp = input ('TimeStamp Field?\n')
    startYear = input('Start Year?\n')
    while not startYear.isnumeric() or not len(startYear) == 4:
        startYear = input('Please enter the year in YYYY format.\nStart Year?\n')
    
    endYear = input('End Year?\n')
    while not endYear.isnumeric() or not len(endYear) == 4:
        endYear = input('Please enter the year in YYYY format.\nEnd Year?\n')

    stringBuilder(partitionOption, partitionID, serverAndTable, timeStamp, startYear, endYear)
    
else:
    stringBuilder(partitionOption, partitionID, serverAndTable)
    
input("Press Enter to exit...")
