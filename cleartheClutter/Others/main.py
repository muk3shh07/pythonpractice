import os

def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(folderName,files):
    for file in files:
        os.replace(file,f"{folderName}/{file}")        

files = os.listdir()
# files.remove(main.py)
print(files)
createIfNotExist('Images')
createIfNotExist('Docs')
createIfNotExist('Video')
createIfNotExist('Others')

imgExt = [".png",".jpg",".jpeg"]
image = [file for file in files if os.path.splitext(file)[1].lower() in imgExt]
print(image)

docsExt = [".txt",".docs",".pdf"]
Docs = [file for file in files if os.path.splitext(file)[1].lower() in docsExt]
print(Docs)

mediaExt = [".mp3",".mp4",".flv"]
media = [file for file in files if os.path.splitext(file)[1].lower() in mediaExt]
print(media) 

others = []

for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in mediaExt) and (ext not in docsExt) and (ext not in imgExt) and os.path.isfile(file):
        others.append(file)
print(others)

move("Images", image)
move("Docs", Docs)
move("Video" , media)
move("Others", others)