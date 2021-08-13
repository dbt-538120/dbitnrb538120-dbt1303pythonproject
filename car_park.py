print('\t\tWelcome to abc parking')
car=input("car price : ")
car=int(car)
bike=input("bike price : ")
bike=int(bike)
truck=input("truck price :")
truck=int(truck)
bicycle=input("bicycle price :")
bicycle=int(bicycle)
bus=input("bus price : ")
bus=int(bus)
maxx=input("Enter the maximum parking slot : ")
print('\n**************************************')
maxx=int(maxx)
total=0
tcar=pcar=tbike=pbike=ttruck=ptruck=tbicycle=pbicycle=tbus=pbus=tslot=0
tslot=maxx
while maxx :
    print(f'Total slots::{tslot}\t\tFree Slots::{maxx}\n')
    vehicle=input("Enter 1 for Car\nEnter 2 for Bike\nEnter 3 for truck\nEnter 4 for bicycle\nEnter 5 for bus\nEnter 6 for view record\nEnter 7 to delete record\n")
    print('\n**********************************')
    vehicle=int(vehicle)
    if vehicle==1:
        total+=car
        tcar+=1
        pcar+=car
    elif vehicle==2:
        total+=bike
        tbike+=1
        pbike+=bike
    
    elif vehicle==3:
        total+=truck
        ttruck+=1
        ptruck+=truck
    elif vehicle==4:
        total+=bicycle
        tbicycle+=1
        pbicycle+=bicycle
    elif vehicle==5:
        total+=bus
        tbus+=1
        pbus+=bus
    elif vehicle==6:
        print(f'Total cars:{tcar}\t\tcars total price:{pcar}\nTotal Bikes:{tbike}\t\tbikes total price:{pbike}\nTotal trucks:{ttruck}\t\ttrucks total price:{ptruck}\nTotal bus:{tbus}\t\tbus total price:{pbus} ')
        print('\n**********************************')
        maxx+=1
    elif vehicle==7:
        tcar=pcar=tbike=ttruck=ptruck=tbicycle=pbicycle=tbus=pbus=0
        maxx=tslot+1
    maxx-=1
    if maxx==0:
        print('Slots are full')
print(f'total::{total}')


