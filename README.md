# UE_Insertion_Automation_Script
When we play with **Open5gs**, we always need to register subscribers. But subscribers insertion in the HSS database of Open5gs is a time-consuming work. Here we have python scripts that can insert subscribers from a csv file to to database without any manual intervention.

**Note:** UEs inserted using these scripts are capable for both internet browsing and VoLTE.

# FILES

**UE.csv** – contains IMSI, OPC, Key and MSISDN of multiple subscribers.

**autoUE.py** -- A pyhton program which inserts data from UE.csv file for multiple subscribers to the MongoDB database of the HSS in Open5gs. This program does not insert all the subscribers automatically form the csv, rather it asks for user input for providing range from the rows of the csv file.

**autoBATCH.py** – Similar to AutoUE.py, this python program also inserts data from UE.csv file for multiple subscribers to the MongoDB database of the HSS in Open5gs. But it inserts all the available subscribers from the csv without for any user input.

**requirements.text** –  contains all the python modules for running the program.

# INSTRUCTION
Here is the instruction below to use this automation program successfully.

**1.** Keep these files i.e. UE.csv, autoUE.py/autoBATCH.py, requirements.text in a same directory or folder. Lets say it is UE_Insertion. Now, navigate to that directory from your terminal using cd command.

    cd UE_Insertion

**2.** Now install all the necessary python modules in your machine.

    pip install -r requirements.text

**3.** Now we are ready to insert UEs from UE.csv file. We have developed two different scripts for UE insertion, where one script inserts all the available UEs in the csv file, the another script inserts UEs row wise. 

## Row-Wise UE Insertion
This program does not insert all the subscribers automatically form the csv, rather it asks for user input for providing range from the rows of the csv file.
Run the python script autoUE.py

    python3 autoUE.py

The program will ask for the range of rows which you want to insert. If you put 10:15, it will insert 10th, 11th, 12th, 13th and 14th row from the csv file.

![image](https://github.com/AshiqRashid/UE_Insertion_Automation_Script/assets/136219283/6534ff36-3fe2-4162-969b-3108096f7aad)

So, subscribers are added successfully.

## Batch Operation
This python program inserts all the UEs from UE.csv file.
For inserting all the subscribers from the csv file use autoBATCH.py program. Run the program.

    python3 autoBATCH.py
    
# ADDITIONAL INFO

Along with registering IMSI, OPC, Key and MSISDN of the subscribers this program sets these below settings for each subscriber.

    AMF = 8000

    #Session: 1
    APN = internet
    IPv4
    5QI/QCI = 9
    ARP Priority Level = 8
    Capability = Disabled Vulnerability = Disabled
    Session-AMBR Downlink = 1 Gbps
    Session-AMBR Uplink = 1 Gbps

    #Session: 2
    APN = ims
    IPv4
    5QI/QCI = 5
    ARP Priority Level = 1
    Capability = Disabled Vulnerability = Disabled
    Session-AMBR Downlink = 3850 Kbps
    Session-AMBR Uplink = 1530 Kbps

    #PCC Rules: 1
    5QI/QCI = 1
    ARP Priority Level = 2
    Capability = Enabled Vulnerability = Enabled
    MBR Downlink = 128 Kbps
    MBR Uplink = 128 Kbps
    GBR Downlink = 128 Kbps
    GBR Uplink = 128 Kbps

    #PCC Rules: 2
    5QI/QCI = 2
    ARP Priority Level = 4
    Capability = Enabled Vulnerability = Enabled
    MBR Downlink = 128 Kbps
    MBR Uplink = 128 Kbps
    GBR Downlink = 128 Kbps
    GBR Uplink = 128 Kbps
