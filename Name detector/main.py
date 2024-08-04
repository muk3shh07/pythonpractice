
import os 



def isMukesh(filename):
    with open(filename, "r") as f:
        fileContent = f.read()
    if "mukesh" in fileContent.lower():
        return True
    else:
        return False

if __name__=="__main__":
    dirContent = os.listdir()
    nMukesh = 0
    for item in dirContent:
        if item.endswith("txt"):
            print(f"Detecting Mukesh in {item}")
            flag=isMukesh(item)
            if(flag):
                print(f"Mukesh found in {item}")
                nMukesh+=1
            else:
                print(f"Mukesh not found in {item}")        
    print("*****Mukesh Detector Summary****")
    print(f"{nMukesh} files found with mukesh in it!!!")            