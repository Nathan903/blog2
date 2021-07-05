killswitch=False
def read_text_file(file_path):
    with open(file_path, 'r', encoding="utf-8") as f:
        lines = f.readlines()
    with open(file_path, 'w', encoding="utf-8") as f:
        killswitch=False
        for line in lines:
            if ("""<a href="http:/""") in line:
                print(line)
            elif ("https:\/\/pillboxshsid.com" in line) and not("schema.org" in line):
                #print(line.replace("https:\/\/pillboxshsid.com",""))
                f.write(line.replace("https:\/\/pillboxshsid.com",""))
            elif ("http:" in line) and not("schema.org" in line):
                print(line)
                f.write(line.replace("http:","https:"))
            else:
                f.write(line)

from pathlib import Path
txt_folder = Path().rglob('*index.html')
files = [x for x in txt_folder]
print(files)
print("#############")

# iterate through all file
for f in files:
    read_text_file(f)
