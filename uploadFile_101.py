
import dropbox
import os


class TransferData:
    def __init__(self, access_token):
        self.aT = access_token

    def upload_file(self, file_from):
        db = dropbox.Dropbox(self.aT)
        fileName = os.path.split(
            file_from)[0]

        dropbox_file = '/CloudStorage/'+fileName

        with open(file_from, "rb") as f:
            db.files_upload(f.read(), dropbox_file,
                            mode=dropbox.files.WriteMode.overwrite)


AToken = "bWuLqYBHEZsAAAAAAAAAAfru7bdvS17K115uXHOA-qtwX_ASzzTVe_LCa7QRKyhF"

cloudStoring = TransferData(AToken)

fileFrom = input("Please Give the File Path To Transfer ")

while(os.path.isfile(fileFrom) == False):
    print("Pls Give The Path Of A File")
    fileFrom = input("Please Give the File Path To Transfer ")

cloudStoring.upload_file(fileFrom)

print("Files Have Been Stored On Dropbox ")
print("Thanks for using me !!")

print("BYE!!!")
##def main():
  ##  new_user = TransferData()
    ##print("May I leve sir (GIVE YOUR ANSWER IN )  ")
   ## print("1. if YES write '1'    ")
   ## print("2. if NO write '2'    ")
    ##activity = int(input("Enter activity number:-  "))
 
    
  ##  if (activity == 2):
    ##        new_user = print("Thanks you are a good user")
    ## elif (activity == 1):
     ##   upload = int(input("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~PROGRAM IS AGAIN STARTTING~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"))
      ##  new_user.upload_file(upload)
   ## else:
     ##   print("Thanks for using me !!")

    ## print("BYE!!!")

##main()

