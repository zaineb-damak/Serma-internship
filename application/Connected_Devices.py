
import subprocess

#adb_command = 'adb devices"'
#output = subprocess.check_output(adb_command, shell=True)
#output_str = output.decode('utf-8')

   
def idList(str):
    id_list = []
    words = str.split()
    for word in words:
        if(word[0].isupper() or word[0].isdigit()):
            id_list.append(word)

    id_list.pop(0)
    return id_list

#print(idList("List of devices attached R59RA00NL7D device LMG900EMf7a2d5d5 device R58M36NV1GD device 0786286166 device"))


