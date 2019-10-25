ip_add = []
q_ip_add = []
subnet = []
q_subnet = []

N = int(input())

for i in range(N):
    subnet_read = [str(i) for i in input().split()]
    subnet += subnet_read

for i in range(len(subnet)):
    q_subnet += subnet[i].split('.')

for i in range(len(q_subnet)):
    q_subnet[i] = bin(int(q_subnet[i]))[2::].zfill(8)

M = int(input())

for i in range(M):
    ip_add_read = [str(i) for i in input().split()]
    ip_add += ip_add_read

for i in range(len(ip_add)):
    q_ip_add += ip_add[i].split('.')

for i in range(len(q_ip_add)):
    q_ip_add[i] = bin(int(q_ip_add[i]))[2::].zfill(8)

for i in range(M):
    result = 0
    ip_counter = 0
    ip_check_a = ''
    ip_check_b = ''
    q_subnet_check = q_subnet
    while ip_counter < 4:
        ip_check_a += q_ip_add[ip_counter]
        ip_counter += 1
    while ip_counter < 8:
        ip_check_b += q_ip_add[ip_counter]
        ip_counter += 1
    q_ip_add = q_ip_add[8::]
    for j in range(N):
        subnet_counter = 0
        subnet_check = ''
        while subnet_counter < 4:
            subnet_check += q_subnet_check[subnet_counter]
            subnet_counter += 1
        q_subnet_check = q_subnet_check[4::]
        if int(ip_check_a, 2) & int(subnet_check) == int(ip_check_b, 2) & int(subnet_check):
            result += 1
    print(result)
