import os,sys,subprocess,shutil,time
def check_pyinstaller():
    try:
        import PyInstaller
        return True
    except ImportError:
        try:
            subprocess.check_call([sys.executable,"-m","pip","install","pyinstaller"])
            return True
        except subprocess.CalledProcessError:return False
def check_files():
    required=["app.py","db.py","words.txt"]
    return all(os.path.exists(f) for f in required)
def safe_remove(path):
    if not os.path.exists(path):return
    try:shutil.rmtree(path)
    except PermissionError:
        print(f"Cannot remove {path} - close any running executables first")
        input("Press Enter after closing the executable...")
        try:shutil.rmtree(path)
        except PermissionError:
            print(f"Still cannot remove {path} - skipping cleanup")
def build():
    safe_remove("dist")
    safe_remove("build")
    try:
        separator=";" if os.name=='nt' else ":"
        cmd=[sys.executable,"-m","PyInstaller","--onefile","--windowed",f"--add-data=words.txt{separator}.","--name=TypeMaster","--clean","app.py"]
        subprocess.check_call(cmd)
        return True
    except subprocess.CalledProcessError:return False
if __name__=="__main__":
    if not check_pyinstaller():
        print("Failed to install PyInstaller")
        sys.exit(1)
    if not check_files():
        print("Missing files")
        sys.exit(1)
    if build():print("Build successful")
    else:print("Build failed")