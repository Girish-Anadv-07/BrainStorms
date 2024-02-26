import os
rootdir = "./"
with open("_Sidebar.md", "w") as file:
    file.write("# **Projects**"+"\n\n")
    file.write("***"+"\n\n")
    for subdir, dirs, files in os.walk(rootdir):    
        if subdir[12:]!='':
            file.write("* ## **"+ subdir[12:] +"**" + "\n")
            print(subdir)
        for file_name in files:
            file.write("\t"+"* ### ["+ file_name[:-3] + "](" + file_name[:-3].replace(" ", "%20") + ")" + "\n")
    file.close()