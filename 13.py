from ipaddress import*

ip = ip_address("193.18.135.201")
for m in range(32):
    net = ip_network(f"{ip}/{m}", 0)
    # print(net)
    k = 0
    for x in net:
        # k += 1
    # print(k)
        x = bin(int(x))[2:]
        if x.count("1") == 19:
            k += 1
    if k == 105:
        print(32 - bin(int(m)).count("1"))
        # break
    