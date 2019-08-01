import ipaddress

network = input()
net_obj = ipaddress.ip_address(network)


for i in net_obj.hosts():
    print(i)

print('hit enter to escape')
input()