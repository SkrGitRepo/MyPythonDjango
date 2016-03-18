'''
Created on Feb 26, 2016

@author: sumkuma2
'''
import re
'''
tree_data = []
final_data_person = [['Ramiz Deliver'], ['Vinoth Manickam'], ['Ramiz Ali'], ['Adarataiah Arumoolla'], ['Satish Rajkumar'], ['Vinoth'], ['Ramiz Ali'], ['Vinoth Manickam'], ['Satish Rajkumar'], ['Ramiz Deliver'], ['Vinoth Manickam'], ['Ramiz Ali'], ['Satish Rajkumar'], ['Kindly Plan'], ['Vinoth'], ['Rgds Jags']]
e[0] = 
if __name__ == '__main__':
    for person in final_data_person:
        a=re.sub(person[0],'',)
        print("============================")
        print(a)
        print("========================")
        tree_data+=[a]
        '''
name = '''Hi Ramiz,

Order-SS: 100862015-14 is re-interfaced to OTM.

Kindly check and plan in OTM.

Thanks,
Vinoth M

From: Ramiz Ali -X (ramali - INFOSYS LIMITED at Cisco)
Sent: Monday, August 17, 2015 7:15 PM
To: Vinoth Manickam -X (vinmanic - INFOSYS LIMITED at Cisco); Remedy7 Notification; Chakravarthy Chandra -X (chakchan - INFOSYS LIMITED at Cisco); Bhushan Ashtikar -X (bashtika - INFOSYS LIMITED at Cisco); JAGADEESH Hv (jaghv)
Cc: sclss-stabilizationcoreteam@external.cisco.com; Satish Rajkumar -X (sarajkum - INFOSYS LIMITED at Cisco)
'''
#a=re.sub(r'Thanks [\s\w\W]+[\:]*',' ',name,re.I)
#a=re.sub(r'Thank you.[\s\w\W]+[:]',' ',a,re.I)

a=re.sub(r'Thanks,[\s\w\W]+[:]*',' ',name,flags=re.I)
a=re.sub(r'hi[\s\w]+[,]',' ',a,flags=re.I)
print(a)
