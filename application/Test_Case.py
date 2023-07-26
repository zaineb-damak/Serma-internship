import os
import pandas as pd
import json
from openpyxl import load_workbook
from Connected_Devices import *

#returns global station number corresponding to the given device id
def getGSNumber(phone_id):
    f = open('./application/resources/GlobalStation.json')
    data = json.load(f)
    for i in data:
         if(i['DeviceID'] == phone_id):
             return i['GSNumber']
    return('wrong id')


#returns global station number corresponding to the given device name
def getGSNumberByName(phone_name):
    f = open('./application/resources/GlobalStation.json')
    data = json.load(f)
    for i in data:
        if(i['DeviceName'] == phone_name):
            return i['GSNumber']
    return('wrong id')

#returns global station device name corresponding to the given device id
def getGSName(phone_id):
    f = open('./application/resources/GlobalStation.json')
    data = json.load(f)
    for i in data:
            if(i['DeviceID'] == phone_id):
                return i['DeviceName']
    return('wrong id')

#returns a list of device names in global station 
def deviceNames():
    f = open('./application/resources/GlobalStation.json')
    data = json.load(f)
    names=[]
    for i in data:
        names.append(i['DeviceName'])
    return names

#saves the changes in a new excel file
def newExcel(wb, row, column, data, new_file, save_path):
    ws = wb.active
    ws.cell(row=row, column=column+1).value = data
    wb.save(filename = save_path+'/'+new_file +'.xlsx')

def updateTestCase(file_path, IDList, new_file, save_file):
    global corresponding_phone
    #create a new dataframe
    df = pd.read_excel(file_path, header=56)
    #empty list linking the old phone number to the new phone number
    corresponding_phone = []
    #initiating variables which will be later used in newExcel
    excel_row = []
    columns = df.columns
    column = 0
    id_list = idList(IDList)
    #get the number of the column ['Action Field 3] in which changes will be made
    for k in range (0,len(columns)):
        if columns[k] == 'Action Field 3':
            column = k
            break
    #changing column action field into string
    df['Action Field 1 ( Tag Name/Request Name/ Picture Name)'] = df['Action Field 1 ( Tag Name/Request Name/ Picture Name)'].astype(str)
    #iterating through each row 
    for index,row in df.iterrows():
        #check if there is a phone being used
        if('Phone' in row['Action Field 1 ( Tag Name/Request Name/ Picture Name)']):
            #each iteration add to the list the index of the row in which we made changes 
            excel_row.append(index+58)
            #if Action Field 3 is empty we don't execute the rest of the instructions
            if pd.isnull(row['Action Field 3'])==True:
                continue
            #case 1: corresponding_phone is empty
            if (len(corresponding_phone) == 0 ):
                #add element to list [old gsnumber, new gsnumber]
                corresponding_phone.append([row['Action Field 3'],int(getGSNumber(id_list[0])),getGSName(id_list[0])])
                row['Action Field 3'] = int(getGSNumber(id_list[0]))
                df.loc[index,'Action Field 3']=row['Action Field 3'] 
                id_list.pop(0)
            else:
                found_matching_pair = False
                x = 0
                for i in range (0,len(corresponding_phone)):
                    x =  int(corresponding_phone[i][0])
                    
                    if(row['Action Field 3'] == int(corresponding_phone[i][0])):
                        found_matching_pair = True
                        x = i
                        break
                #case 2: phone number exists in corresponding_phone
                if (found_matching_pair == True):
                    #replace the old value with the new value in dataframe
                    row['Action Field 3'] = int(corresponding_phone[x][1])
                    df.loc[index,'Action Field 3'] = row['Action Field 3'] 
                #case 3: phone number doesn't exist in corresponding_phone
                else:
                    corresponding_phone.append([row['Action Field 3'],int(getGSNumber(id_list[0])),getGSName(id_list[0])])
                    row['Action Field 3'] = getGSNumber(id_list[0])
                    df.loc[index,'Action Field 3']  = row['Action Field 3'] 
                    id_list.pop(0)
        
        #changing the names of the devices
        names = deviceNames()

        if str(row['Action Field 3']).replace('"','') in  names:
            excel_row.append(index+58)
            old = getGSNumberByName(str(row['Action Field 3']).replace('"',''))
            exists = False
            for z in range(0,len(corresponding_phone)):
                if (int(old) == corresponding_phone[z][0]):
                    exists = True
                    l = z
                    break
            if exists == True:
                row['Action Field 3'] = corresponding_phone[l][2]
                df.loc[index,'Action Field 3']  = row['Action Field 3']
            if exists == False:
                corresponding_phone.append([int(old),int(getGSNumber(id_list[0])),getGSName(id_list[0])])
                row['Action Field 3'] = getGSName(id_list[0])
                df.loc[index,'Action Field 3']  = row['Action Field 3']
                id_list.pop(0)

        print(row['Action Field 3'])
    getChanges()
   
    #saving the changes in a new excel file
    wb = load_workbook(file_path)
    for j in range (0,len(excel_row)):
        newExcel(wb, excel_row[j] ,column,df.loc[excel_row[j]-58,'Action Field 3'], new_file, save_file)



#returns list of names of test cases in the execution plan
def getTestCases(execution_plan_file_path):
    df= pd.read_excel(execution_plan_file_path)
    file_name=[]
    for index, row in df.iterrows():
        file_name.append(row['Test Name'] + '.xlsx') 
    return(file_name)

#updates the test cases present in the execution plan
def executionPlan(execution_plan_file_path, idList, save_file):
    testcases = []
    testcases = getTestCases(execution_plan_file_path)
    i = 0
    for test in testcases:
        try:
            testName = []
            testName = testcases
            testName[i] = os.path.splitext(test)[0]
            updateTestCase('./application/resources/'+test, idList,testName[i]+'_updated', save_file )
            i = i+1
            pass
        except FileNotFoundError:
            pass

def getChanges():
    old=[]
    new=[]
    for ele in corresponding_phone:
        old.append(ele[0])
        new.append(ele[1])
        print(old, new)





listID=("List of devices attached R59RA00NL7D device LMG900EMf7a2d5d5 device R58M36NV1GD device R58N91KCNYY device 215cf1f7 device")
updateTestCase('E:/stage SERMA summer 2023/application/resources/test_case3.xlsx',listID,'sample','E:/stage SERMA summer 2023/Serma-internship/application')

#executionPlan('./application/resources/CAN.xlsx',listID,'E:/stage SERMA summer 2023/Serma-internship/application')
#print(getTestCases('./resources/CAN.xlsx'))



