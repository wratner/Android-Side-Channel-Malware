CS_463_MP2
==========

- Currently getting .pcap's for accessing the same condition multiple times.
- Wireshark filter I am using: ip.src == 192.17.200.250 && tcp.dstport == 80
- Data points:

SENT: Condition request (GET):

File | Size | Packet number | Time (offset = 0)
--- | --- | --- | ---
abcess.pcap | 860 | 41 | 7.002959
abcess_compare.pcap | 879 | 50 | 7.495650
abcess_compare2.pcap | 814 | 45 | 0
acute_kidney_failure.pcap | 886 | 25 | 0
acute_kidney_failure_compare.pcap | 904 | 27 | 0
acute_kidney_failure_compare2.pcap | 615 | 29 | 0

SENT: Ad request (GET):

File | Size | Packet number | Time offset
--- | --- | --- | ---
abcess.pcap | 615 | 38 | -0.009758
abcess_compare.pcap | 615 | 47 | -0.006227
abcess_compare2.pcap | 615 | 46 | 
acute_kidney_failure.pcap | 615 | 26 | 
acute_kidney_failure_compare.pcap | 615 | 29 | 
acute_kidney_failure_compare2.pcap | 615 | 29 | 

RECEIVED: First HTTP/1.1 200 OK:

File | Size | Packet number | Time offset
--- | --- | --- | ---
abcess.pcap | 597 | 44 | 0.033624
abcess_compare.pcap | 597 | 53 | 0.034845
abcess_compare2.pcap |  |  | 
acute_kidney_failure.pcap |  |  | 
acute_kidney_failure_compare.pcap |  |  | 
acute_kidney_failure_compare2.pcap |  |  | 

SENT: Symptom checker request (POST):

File | Size | Packet number | Time offset
--- | --- | --- | ---
abcess.pcap | 512 | 53 | 0.255509
abcess_compare.pcap | 512 | 58 | 0.045477
abcess_compare2.pcap |  |  | 
acute_kidney_failure.pcap |  |  | 
acute_kidney_failure_compare.pcap |  |  | 
acute_kidney_failure_compare2.pcap |  |  | 

RECEIVED: ??? [TCP segment of a reassembled PDU]

File | Size | Packet number | Time offset
--- | --- | --- | ---
abcess.pcap | 1470 | 54 | 0.319761
abcess_compare.pcap | 1470 | 62 | 0.13559
abcess_compare2.pcap |  |  | 
acute_kidney_failure.pcap |  |  | 
acute_kidney_failure_compare.pcap |  |  | 
acute_kidney_failure_compare2.pcap |  |  | 

RECEIVED: Second HTTP/1.1 200 OK:

File | Size | Packet number | Time offset
--- | --- | --- | ---
abcess.pcap | 555 | 56 | 0.320057
abcess_compare.pcap | 385 | 64 | 0.136681
abcess_compare2.pcap |  |  | 
acute_kidney_failure.pcap |  |  | 
acute_kidney_failure_compare.pcap |  |  | 
acute_kidney_failure_compare2.pcap |  |  | 

SENT: Ad image request:

File | Size | Packet number | Time offset | Ad image
--- | --- | --- | --- | ---
abcess.pcap | 740 | 66 | 0.513392 | /getImage.php5?apid=141673&mode=live&acid=1847699&auid=mmid_bd99de1730d4bb6f36bcd3ac5ccaf0b44c_014499b058bd&osid=81&urid=Yfa8VfZV8iCn1tMPg_BGWWOR&ri=81&mmid=8079&orut=1394148223&mtpid=91178
abcess_compare.pcap | 634 | 82 | 0.29721 | /2/standard/ad/std/7828/203885/Sprint_Consumer_Rambo_Buddies_320x50N.jpg?cId=7828&eId=25041&aId=203885&type=event&key=standard&value=null&phbust=1394149767
abcess_compare2.pcap |  |  |  | 
acute_kidney_failure.pcap |  |  |  | 
acute_kidney_failure_compare.pcap |  |  |  | 
acute_kidney_failure_compare2.pcap |  |  |  | 

RECEIVED: Third HTTP/1.1 200 OK:

File | Size | Packet number | Time offset
--- | --- | --- | ---
abcess.pcap | 1229 | 70 | 0.545813
abcess_compare.pcap | 1229 | 71 | 0.152204
abcess_compare2.pcap |  |  | 
acute_kidney_failure.pcap |  |  | 
acute_kidney_failure_compare.pcap |  |  | 
acute_kidney_failure_compare2.pcap |  |  | 

SENT: Symptom checker response (POST):

File | Size | Packet number | Time offset
--- | --- | --- | ---
abcess.pcap | 526 | 101 | 1.174592
abcess_compare.pcap | 526 | 108 | 0.346267
abcess_compare2.pcap |  |  | 
acute_kidney_failure.pcap |  |  | 
acute_kidney_failure_compare.pcap |  |  | 
acute_kidney_failure_compare2.pcap |  |  | 

SENT: Second symptom checker request (POST):

File | Size | Packet number | Time offset
--- | --- | --- | ---
abcess.pcap | 546 | 119 | 1.490335
abcess_compare.pcap | 546 | 126 | 0.562257
abcess_compare2.pcap |  |  | 
acute_kidney_failure.pcap |  |  | 
acute_kidney_failure_compare.pcap |  |  | 
acute_kidney_failure_compare2.pcap |  |  | 

# Getting some metrics on the packets:
1. `cd sig_checker`
- `./PktReader.py`

# Generating a guess for a packet dump:
- `./main.py fileName` - e.g. `./main.py testFiles/acute1.text`

