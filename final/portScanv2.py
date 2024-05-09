import nmap
import time

def scan_ip(ip):
    nmScan = nmap.PortScanner()

    start_time = time.time()
    try:
        nmScan.scan(ip, '1-1024')
    except nmap.PortScannerError as e:
        print("Nmap scan failed:", e)
        return None

    end_time = time.time()
    scan_time = end_time - start_time
    print("Scan time:", scan_time, "seconds")

    results = []
    for host in nmScan.all_hosts():
        print("Host : {} ({})".format(host, nmScan[host].hostname()))
        print("State : {}".format(nmScan[host].state()))

        for proto in nmScan[host].all_protocols():
            print("----------")
            print("Protocol : {}".format(proto))

            for port in sorted(nmScan[host][proto].keys()):
                state = nmScan[host][proto][port]['state']
                if state != "closed":
                    name = nmScan[host][proto][port]['name']
                    print("Port : {:<5}\tState : {}\tName : {}".format(port, state, name))
                    results.append((port, state, name))

    return results

# Ejemplo de uso de la función
