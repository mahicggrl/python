import os
from os import path

class CountyrName():
    def openfile(self):
        content =r"C:\Temp\docs\Countries.txt"
        with open(content, 'r') as fh:
            for line in fh:
                country = line.split(",")[3]
                fName = line.split(",")[0]
                lName = line.split(",")[1]
                email = line.split(",")[5]
                cpath = "C:\\Temp\\task4\\Country"
                epath = path.exists(cpath)
                if not epath:
                    os.mkdir(cpath)
                if (country == 'Australia' or country == 'UK') and (email.split('@')[1].split(".")[0] == 'gmail' or email.split('@')[1].split('.')[0] == 'hotmail'):
                    chkCd = cpath +"\\" + country
                    #print(chkCd)
                    echkCdn = path.exists(chkCd)
                    if echkCdn == False:
                        os.mkdir(chkCd)
                    mailpath = chkCd + "\\"+email.split('@')[1].split(".")[0]+".txt"
                    cMailPath = path.exists(mailpath)
                    if cMailPath == False:
                        with open(os.path.join(mailpath), 'w'):
                            pass
                    result = fName, ", ", lName, ", ", country, ", ", email
                    for ab in result:
                        with open(mailpath, "a") as file:
                            file.write(ab)

CN = CountyrName()
CN.openfile()