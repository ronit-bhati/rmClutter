import os

def createDir(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(dirName, files):
    for file in files:
        os.replace(file, f"{dirName}/{file}")

if __name__ == "__main__":
    files = os.listdir()
    files.remove('rmClutter.py')

    createDir('images')
    createDir('media')
    createDir('docs')
    createDir('executables')
    createDir('zip-files')
    createDir('code')
    createDir('others')

    imgExts = ['.png', '.jpg', '.jpeg', '.svg', '.gif', '.raw', '.ico']
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]

    mediaExts = ['.mp4', '.mkv', '.mov', '.wnv', '.flv', '.avi', '.avchd', '.webm', 'mp4']
    media = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]

    docExts = ['.doc', '.docx', '.odt', '.pdf', '.xls', '.xlsx', '.ods', '.ppt', '.pptx', '.txt', '.md', '.odg', '.odp']
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]

    executableExts = ['.exe', '.deb', '.osx', '.ex', '.apk', '.bat', '.cmd', '.msi', '.sh', '.jar', '.appimage']
    executables = [file for file in files if os.path.splitext(file)[1].lower() in executableExts]

    zipExts = ['.zip', '.7z', '.rar', '.zipx', '.tar', '.gz']
    zipFiles = [file for file in files if os.path.splitext(file)[1].lower() in zipExts]

    codeExts = ['.py', '.htm', '.html', '.c', '.p', '.css', '.js', '.cc', '.go', 'swift', 'r', '.ru', '.db', '.sqlite', '.sqlite3', '.dbms', '.java']
    code = [file for file in files if os.path.splitext(file)[1].lower() in codeExts]

    otherExts = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if ext not in imgExts and ext not in mediaExts and ext not in docExts and ext not in executableExts and ext not in zipExts and ext not in codeExts and os.path.isfile(file):
            otherExts.append(file)

move('images', images)
move('media', media)
move('docs', docs)
move('executables', executables)
move('zip-files', zipFiles)
move('code', code)
move('others', otherExts)