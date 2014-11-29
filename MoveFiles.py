import shutil
import os

src = "/Projects/InPho/"
dest = "/Projects/Rikers Calls Dev/"

DANYsrc = '\\DANY.NYCNET\DANYXDrive\Rikers Calls\'
DANYdest = '\\DANY.NYCNET\DANYXDrive\Rikers Calls\Rikers Calls Dev\'

def CopyFlacFiles(src, dest):

        # get an array of unique BAC's in all .flac's
        for file in files:
            if os.path

        import os
        for root, dirs, files in os.walk(".", topdown=False):
            for name in files:
                print(os.path.join(root, name))
            for name in dirs:
                print(os.path.join(root, name))

        # create the file location on the X drive
        if not os.path.exists(dest):
            os.makedirs(dest)

        # copy the files from the CD to X drive
        src_files = os.listdir(src)
        
        # copy loop with counter for status bar
        for file_name in src_files:
            full_file_name = os.path.join(self.src, file_name)
            if (os.path.isfile(full_file_name)):
                extension = os.path.splitext(full_file_name)[1]
                if (extension == ".flac"):
                    try:
                        shutil.copy2(full_file_name, dest)
                        self.status = str(count) + "/" + str(numfiles) + " calls have been copied"
                        app.statusVariable.set(self.status)
                        app.update()
                        count += 1
                    except IOError,e:
                        if (e.errno == 13):
                            self.status = str(count) + "/" + str(numfiles) + " calls have been copied"
                            app.statusVariable.set(self.status)
                            app.update()
                            count += 1
                            continue
                        else:
                            tkMessageBox.showerror("Copy error", str(e))
        
