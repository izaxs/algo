class MSG:
    def __init__(self, msg: str):
        # message format: req|1.0.0.2, req|255.255.234.0, resp|1.0.0.2|200, resp|255.255.234.0|523
        seg = msg.split('|')
        self.addr = seg[1]
        if len(seg) == 2:
            self.isReq = True
            self.status = 200
        elif len(seg) == 3:
            self.isReq = False
            self.status = int(seg[2])

def route_decision(events: list[str]) -> list[str]:
    BASE_COUNT, REFRESH_LO, REFRESH_HI = 3, 1, 1
    failMap: dict[str, tuple[int, int]] = {} # key: ip, value: tuple of [remaining failover, failover cap]
    decisions: list[str] = []
    for event in events:
        msg = MSG(event)
        cur, cap = failMap.setdefault(msg.addr, (0, BASE_COUNT))
        print(f'{event}: begin -- cur: {cur}, cap: {cap}')
        if msg.isReq:
            if cur == 0:
                decisions.append('direct')
            else:
                decisions.append('failover')
                if cur == 1:
                    cap = BASE_COUNT
                failMap[msg.addr] = (cur-1, cap)
        elif msg.status == 200:
            if cur > 0 or cap > BASE_COUNT:
                failMap[msg.addr] = (0, BASE_COUNT)
        elif msg.status == 523:
            if REFRESH_LO <= cur <= REFRESH_HI:
                cap = cap*2
            failMap[msg.addr] = (cap, cap)
        else:
            raise Exception()
        print(f'{event}: after -- cur: {failMap[msg.addr][0]}, cap: {failMap[msg.addr][1]}')
    return decisions

rq1 = 'req|1.0.0.2'
rs1p = 'resp|1.0.0.2|200'
rs1f = 'resp|1.0.0.2|523'

rq2 = 'req|255.255.234.0'
rs2p = 'resp|255.255.234.0|200'
rs2f = 'resp|255.255.234.0|523'

events = [rq1, rq2, rs1p, rq1, rs1f, rq2, rs1f, rq1, rq1, rq1, rs1f, rq1, rq1, rq1, rq1]

print(route_decision(events))
