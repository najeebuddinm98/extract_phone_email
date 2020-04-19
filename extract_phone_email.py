#extracting Indian phone numbers and emails from the clipboard or input and saving in a text file

import pyperclip, re, os, datetime

#DO: getting the data
try:
    clipData=pyperclip.paste()
except ModuleNotFoundError:
    print('Pyperclip module is not found. Continue the process below')
    clipData=''
finally:
    if len(clipData)==0:
        print('Couldn\'t find data in clipboard.')
        text=input('Enter your text here: \n')
    else:
        text=clipData

#DO: Pattern formation  
phoneRegex=re.compile('''(
(\+91 | 91)?                    #Indian country code
\d{10}                          #actual number
)''',re.VERBOSE)

emailRegex=re.compile(r'''
[a-zA-Z0-9_.+]+                 #name part
@                               #symbol
[a-zA-Z0-9_.+]+                 #domain part
''',re.VERBOSE)

#DO: finding the phone numbers and emails
print('Finding now')
extractedPhone=phoneRegex.findall(text)
email=emailRegex.findall(text)

#DEBUG: print(extractedPhone)
#DEBUG: print(email)

#DO: filter phone numbers from extracted contents as regex groups them up
phone=[]
for i in extractedPhone:
    phone.append(i[0])

#DEBUG: print('\n'.join(phone))
#DEBUG: print('\n'.join(email))

#DO: saving the data
currentDir=os.getcwd()
mainDir=currentDir+'\\extractedfiles'

if not os.path.exists(mainDir): #checking if folder already exists
    os.mkdir(mainDir)

filePath=mainDir+'\\phone_emails.txt'

file=open(filePath,'a') #append mode so that previous data isnt overwritten
file.write('\nOn '+str(datetime.datetime.now())+',')
file.write('\nPhone Numbers: \n'+'\n'.join(phone)+'\n\n'+'Email Ids: \n'+'\n'.join(email))
file.close()

print('The file phone_emails.txt has been updated in the extractedfiles directory in the path '+currentDir)



