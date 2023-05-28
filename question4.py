import argparse
import ipaddress
from collections import defaultdict
import ipaddress

parser = argparse.ArgumentParser()
parser.add_argument('--n', type=int, default=2)
parser.add_argument('--m', type=int, default=1)
parser.add_argument('--t', type=int, default=1)


args = parser.parse_args()

fail_server = {}
ans = {}
overload_ans = defaultdict(list)
num = args.n
server_inf = defaultdict(list)
overload_cnt = args.m
overload_time = args.t
subnet_list = defaultdict(set)

# 故障したサーバーリストにアドレスが存在するか確認
def IsfailServer(fail_server, address):
    return address in fail_server

# 過負荷状態のサーバーの期間を取得する
def OverloadCondition(overload_list, time):
    overload_sum = 0
    for data in overload_list:
        overload_sum += data[1]
    overload_ave = overload_sum // len(overload_list)
    if overload_ave > time:
        if len(overload_list) > 1:
            return [overload_list[0][0], overload_list[-1][0]]
        else:
            return [overload_list[0][0]]
    else:
        return False


with open('log.txt') as file:
    for line in file:
        log = line.replace('\n', '').split(',')
        time = log[0]
        add = log[1]
        res = log[2]

        if res == '-':
            if IsfailServer(fail_server, add):
                fail_server[add][1] += 1
            if not IsfailServer(fail_server, add):
                fail_server[add] = [time, 1]

        else:
            server_inf[add].append([time, int(res)])
            if IsfailServer(fail_server, add):
                cnt = fail_server[add][1]
                if cnt >= num:
                    time_out = int(fail_server[add][0])
                    fail_pre = int(time) - time_out
                    ans[add] = fail_pre
                    del fail_server[add]

        overload_len = len(server_inf[add])
        if overload_len < overload_cnt:
            res_data = server_inf[add]
        else:
            res_data = server_inf[add][-overload_cnt:]

        overload = OverloadCondition(res_data, overload_time)
        if overload == False:
            continue
        else:
            overload_ans[add].append(overload)


        subnet = ipaddress.ip_network(add, strict=False)
        subnet_list[subnet].add(add)



print('--------------------------------------')

for key, value in ans.items():
    print(f'{key} の故障期間は {value} です。')

print('--------------------------------------')

for key, values in overload_ans.items():
    for value in values:
        if len(value) > 1:
            print(f'{key} の過負荷状態期間は {value[0]} ~ {value[1]} です。')
        else:
            print(f'{key} の過負荷状態期間は {value[0]} です。')

print('--------------------------------------')
ans_subnet_list = defaultdict(set)
ans_subnet_list_time = defaultdict(int)

for ans_add, time in ans.items():
    ans_sub = ipaddress.ip_network(ans_add, strict=False)
    ans_subnet_list[ans_sub].add(ans_add)
    ans_subnet_list_time[ans_add] = time


for sub in subnet_list:
    if len(subnet_list[sub]) == len(ans_subnet_list[sub]):
        print(f'サブネット: {sub}')
        for sub_add in ans_subnet_list[sub]:
            print(f'{sub_add} の故障期間は {ans_subnet_list_time[sub_add]} です。')

print('--------------------------------------')
