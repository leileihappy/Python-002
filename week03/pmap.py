import os
import socket
import time
from multiprocessing import Pool
import sys,getopt


def run(f,ips):
    result = []
    if f == 'ping':
        result = pingCommand(ips)
    else:
        result = tcpCommand(ips)
    return result

def parseParam(argv):
    param = {}
    try:
        opts,arg = getopt.getopt(argv,"n:f:i:w:",["n=","f=","ip="])
        for opt,arg in opts:
            print(str(opt) +','+ str(arg))
            param[opt] = arg
    except getopt.GetoptError:
        print('pmap.py -n <threadCount> -f <ping/tcp> -ip <ip> -w <result>')
    return param
    
def parseip(param_ip):
    #例子 192.168.0.1-192.168.0.100
    #[192.168.0.1,192.168.0.2...]
    ipdata = []
    ips = param_ip.split('-')
    if len(ips)==1:
        ipdata.append(ips[0])
    else:
        start = ips[0].split('.')
        end = ips[1].split('.')
        print(start[3]+','+end[3])
        for num in range(int(start[3]),int(end[3])):
            #print('num='+str(num))
            ipdata.append(start[0]+'.'+start[1]+'.'+start[2]+'.'+str(num))
    return ipdata

def pingCommand(ips):
    realips = []
    for hostname in ips:
        response = os.system('ping -n 2 '+hostname)
        print(f'ping 返回值:{str(response)}')
        if response == 0:
            print(hostname, 'is up!')
            realips.append(hostname)
        else:
            print(hostname,'is down!')
    return realips

def tcpCommand(ips):
    ipports = []
    for ip in ips:
        for port in range(3305,3310):
            try:
                #print('尝试连接：'+ip+','+str(port))
                s = socket.socket()
                s.settimeout(0.2)   
                s.connect((ip,port))
                s.close()
                print('连接成功：'+ip+':'+str(port))
                ipports.append((ip,port))
            except Exception as e:
                #time.sleep(1)
                print(e)
    return ipports

if __name__ == '__main__':
    param = parseParam(sys.argv[1:])
    print(param)
    processCount = param.get('-n')
    ip = param.get('-i')
    f = param.get('-f')
    w = param.get('-w')
    ips = parseip(ip)
    resultData = []
    try:
        with Pool(processes=int(processCount)) as pool:
            result = pool.apply_async(run,(f,ips))
            resultData = result.get(timeout=600)
    except Exception as e:
        print(e)
    if w !=None:
        with open(w,'a+') as f:
            for s in resultData:
                if f == 'ping':
                    f.write(s+'\t\n')
                else:
                    f.write(str(s)+'\t\n')