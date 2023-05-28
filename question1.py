fail_server = {}
ans = {}

def IsfailServer(fail_server, address):
    return address in fail_server

with open('log.txt') as file:
    for line in file:
        log = line.replace('\n', '').split(',')
        time = log[0]
        add = log[1]
        res = log[2]

        if res == '-':
            if not IsfailServer(fail_server, add):
                fail_server[add] = time
        else:
            if IsfailServer(fail_server, add):
                time_out = int(fail_server[add])
                fail_pre = int(time) - time_out
                ans[add] = fail_pre
                del fail_server[add]

for key, value in ans.items():
    print(f'{key}の故障期間は{value}です。')




