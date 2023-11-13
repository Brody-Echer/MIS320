## This executes all scripts to populate the db
appraiser = 'fakeAppraiserdata.py'
employee = 'fakeEmpdata.py'
house = 'fakeHousedata.py'
intern = 'fakeInternData.py'
lender = 'fakeLenderData.py'
manager = 'fakeManagerData.py'
photograper = 'fakephotodata.py'
realtor = 'fakeRealtorData.py'

list = []
list = [appraiser,
employee
,house 
,intern 
,lender 
,manager 
,photograper 
,realtor]

for i in list:
    with open("home/Brody/Documents/MIS 320/320project/" +i) as file:
        exec(file.read())