import os
def remove_dir(d):  # Remove file or tree

    try:
        if os.stat(d)[0] & 0x4000:  # Dir
            for file in os.ilistdir(d):
                if file[0] != '.' and file[0] != '..':
                    remove_dir("/".join((d, file[0])))  # File or Dir
            os.rmdir(d)
        else:  # File
            os.remove(d)
    except:
        print("rm of '%s' failed" % d)
