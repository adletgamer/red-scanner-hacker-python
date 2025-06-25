import nmap 
from scapy.all import ARP, Ether, srp
#ipconfig

scanner=nmap.PortScanner()
ip_range= '192.168.100.14' #Se adapta segun tu red

arp = ARP(pdst=ip_range)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")  
packet = ether / arp

print("[*]Escaneando red local ...")
scanner.scan(hosts=ip_range,arguments='-sn') #Se utiliza para descubrir el host

for host in scanner.all_hosts():
    state=scanner[host].state()
    host_name=scanner[host].hostname()
    print(f"[+] Host detectado: {host} ({host_name})- Estado: {state}")

target= input("\n Ingresa la IP que deseas escanear: ")
scanner.scan(target, arguments='-p 1-1024 -sT')

print(f"\n [*] Escaneando puertos en {target} ...\n")
for proto in scanner[target].all_protocols():
    ports =scanner[target][proto].keys()
    for port in ports:
        state= scanner[target][proto][port]['state']
        print(f"-> Puerto {port}: {state}")

print("\n [*] Enviando solicitudes ARP \n")
result=srp(packet, timeout=3, verbose=0)[0]

for sent, received in result:
    print(f"[+] {received.psrc} esta activo ")  
