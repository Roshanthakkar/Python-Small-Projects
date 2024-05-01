# this is progrma koi bhi text ko find kar sakte hai using os module.

import os

def isBinod(filename):
    with open(filename,"r") as f:
        fileContent=f.read()
        
    #Detect all forms of binod like bInoD
    if "binod" in fileContent.lower():
        return True
    else:
        return False
    
if __name__ == "__main__":
 # Listing the contents of this folder 
   
    dir_contents=os.listdir()
  
    nBinod=0
    # for each the txt file ,run isBinod for them
    print(dir_contents)
    for item in dir_contents:
        if item.endswith('txt'):
            print(f"Detecting Binod in {item}")
            flag=isBinod(item)
            if(flag):
                print(f"Binod found in{item}")
                nBinod+=1
            else:
                print(f"Binod is not found in {item}")
                
    print("**********Binod Detector Summary*********") 
    print(f"{nBinod} files found with binod hidden into item")