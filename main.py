import os

def createIfNotExists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
         
def move(foldername, files):
    for file in files:
        os.replace(file,f"{foldername}/{file}")

files = os.listdir()
files.remove("main.py")
# print(files)
createIfNotExists('Images')
createIfNotExists('Docs')
createIfNotExists('HTML')
createIfNotExists('Others')
createIfNotExists('medias')

imgExts=[".png",".jpeg",".jpg"]
images=[file for file in files if os.path.splitext(file)[1].lower() in imgExts ]

docExts=[".txt",".docx",".doc",".pdf"]
docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]

mediaExts=[".mp3",".mp4",".flv"]
medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]
# print(docs)

Others=[]
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in mediaExts) and (ext not in docExts) and (ext not in imgExts) and os.path.isfile(file):
        Others.append(file)

# print(Others)
move("Images", images)
move("Docs", docs)
move("Others", Others)
move("Medias", medias)




