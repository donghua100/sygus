import os
import subprocess
filepath = "bv"
# filepath = "easycase"


def get_files_name(path):
    filevec = []
    for root,dirs,files in os.walk(path):
        # print("root: ",root)
        # print("dirs: ",dirs)
        # print("files: ",files)
        for file in files:
            filevec.append(root + '/' + file)
    return filevec


filevec = get_files_name(filepath)
print("total files: ",len(filevec))
for file in filevec:
    filename = file.split('/')[-1]
    fout = open("output/{}.txt".format(filename),"w",encoding='utf-8')
    fout.write("the file is : {}\n".format(file))
    print("the file is ",file)
    # ./sygus-apdr -e bmc -k 20 --synmode 1 -v 0 
    # ./sygus-apdr --synmode 1 -v 0
    proc = subprocess.Popen(["./sygus-apdr -e bmc -k 200 --synmode 1 -v 0 {}".format(file)],shell=True,
                                stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding='utf-8',
                                universal_newlines=True)
    print("start..")
    try:
        outs, errs = proc.communicate(timeout=60)
        if outs:
            fout.write(outs)
            print(outs)
        else:
            fout.write("no output\n")
            print("no output")
    except subprocess.TimeoutExpired:
        proc.kill()
        outs, errs = proc.communicate()
        fout.write("timeout: \n")
        if outs:
            fout.write(outs)
            print(outs)
        else:
            fout.write("no output\n")
            print("no output")
    print("end...")
    fout.close()