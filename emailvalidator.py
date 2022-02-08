import re

strRegex = "^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"

strSourceDataFileName = "C:\\Users\\llrow\\Desktop\\email-validator\\EmailDataToProcess\\EmailData.txt"
strValidDataFileName = "C:\\Users\\llrow\\Desktop\\email-validator\\EmailDataToProcess\\ValidEmailData.txt"
strInvalidDataFileName = "C:\\Users\\llrow\\Desktop\\email-validator\\EmailDataToProcess\\InvalidEmailData.txt"

# Open files for writing
ValidDataStream = open(strValidDataFileName, 'w')
InvalidDataStream = open(strInvalidDataFileName, 'w')

# Read a line of text from the source file
objSourceDataStream = open(strSourceDataFileName, 'r')

strHeaderRow = objSourceDataStream.readline()
ValidDataStream.write(strHeaderRow)
InvalidDataStream.write(strHeaderRow)

for strLine in objSourceDataStream:
    if(re.search(strRegex,strLine)):
        print('Valid')
        ValidDataStream.write(strLine)
    else:
        print('Invalid')
        InvalidDataStream.write(strLine)

objSourceDataStream.close()
ValidDataStream.close()
InvalidDataStream.close()