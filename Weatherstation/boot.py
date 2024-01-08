# boot.py as provided by @Freenove in their esp32 ultimate starter kit

import uos as os
import uerrno as errno
iter = os.ilistdir()
IS_DIR = 0x4000
IS_REGULAR = 0x8000

while True:
    try:
        entry = next(iter)
        filename = entry[0]
        file_type = entry[1]
        if filename == 'boot.py':
            continue
        else:
            print("===============================")
            print(filename,end="")
            if file_type == IS_DIR:
                print(", File is a directory")
                print("===============================")
            else:
                print("\n===============================\n")
                exec(open(filename).read(),globals())
    except StopIteration:
        break
