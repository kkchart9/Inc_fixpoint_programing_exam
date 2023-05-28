import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--n', type=int, default=1)
args = parser.parse_args()

fail_server = {}
ans = {}
num = args.n

# 故障したサーバーリストにアドレスが存在するか確認
def IsfailServer(fail_server, address):
    return address in fail_server

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
            if IsfailServer(fail_server, add):
                cnt = fail_server[add][1]
                if cnt >= num:
                    time_out = int(fail_server[add][0])
                    fail_pre = int(time) - time_out
                    ans[add] = fail_pre
                    del fail_server[add]

for key, value in ans.items():
    print(f'{key}の故障期間は{value}です。')