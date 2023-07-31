
import subprocess

#adb_command = 'adb devices"'
#output = subprocess.check_output(adb_command, shell=True)
#output_str = output.decode('utf-8')



#returns a list of id od the connected devices
#takes as parameter: string which is the return of the 'adb devices' command
def idList(str):
    id_list = []
    words = str.split()
    for word in words:
        if(word[0].isupper() or word[0].isdigit()):
            id_list.append(word)

    id_list.pop(0)
    return id_list



