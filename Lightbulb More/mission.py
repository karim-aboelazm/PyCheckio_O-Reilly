from datetime import datetime, timedelta
from typing import List, Optional, Union, Tuple

def sum_light(els: List[Union[datetime, Tuple[datetime, int]]],
        start_watching: Optional[datetime] = None,
        end_watching: Optional[datetime] = None,
        operating: Optional[timedelta] = None,
        req: Optional[int] = None) -> int:
    if start_watching == None: start_watching = datetime(1970,1,1)
    if end_watching == None: end_watching = datetime(9999,12,31)
    sw = start_watching
    ew = end_watching
    if req == None: req = 1

    els = [x if type(x)==tuple else (x,1) for x in els]
    els.append((ew,1))
    els.sort()
    bulbs = [x[1] for x in els]
    bulbs = set(bulbs) # set of bulbs
    ons = dict.fromkeys(bulbs,-1)
    lt = min([x[0] for x in els])
    if operating != None:
        rt = dict.fromkeys(bulbs, operating.total_seconds())
    else:
        rt = dict.fromkeys(bulbs, (datetime(9999,12,31) - datetime(1970,1,1)).total_seconds())
    ot = 0

    for dt, n in els:
        print(dt,n)
        if sum([ons[x]==1 for x in bulbs])>=req:
            print(ons)
            print(rt)
            print([min(rt[i], max((min(dt,ew)-max(lt,sw)).total_seconds(),0)) for i in bulbs if ons[i]==1])
            print(sorted([min(rt[i], max((min(dt,ew)-max(lt,sw)).total_seconds(),0)) for i in bulbs if ons[i]==1],reverse=True))
            ot += sorted([min(rt[i], max((min(dt,ew)-max(lt,sw)).total_seconds(),0)) for i in bulbs if ons[i]==1],reverse=True)[req-1]
            for i in bulbs:
                if ons[i] == 1:
                    rt[i] = max(0,rt[i] - (dt - lt).total_seconds())
            lt = dt
            ons[n] = ons[n]*-1
        elif sum([ons[x]==1 for x in bulbs])>=1:
            for i in bulbs:
                if ons[i] == 1:
                    rt[i] = max(0,rt[i] - (dt - lt).total_seconds())
            lt = dt
            ons[n] = ons[n]*-1
        else:
            lt = dt
            ons[n] = ons[n]*-1
    return ot


if __name__ == '__main__':
    print("Example:")

    print(sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        (datetime(2015, 1, 12, 10, 0, 50), 3),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
    ], req=3))

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        (datetime(2015, 1, 12, 10, 0, 0), 2),
        datetime(2015, 1, 12, 10, 0, 10),
        (datetime(2015, 1, 12, 10, 1, 0), 2),
    ]) == 60

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
        (datetime(2015, 1, 12, 11, 0, 0), 2),
        (datetime(2015, 1, 12, 11, 1, 0), 2),
    ]) == 70

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
    ]) == 30
    
    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
    ]) == 40

    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
        (datetime(2015, 1, 12, 10, 1, 0), 3),
        (datetime(2015, 1, 12, 10, 1, 20), 3),
    ]) == 60

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        (datetime(2015, 1, 12, 10, 0, 0), 2),
        datetime(2015, 1, 12, 10, 0, 10),
        (datetime(2015, 1, 12, 10, 1, 0), 2),
    ], datetime(2015, 1, 12, 10, 0, 50)) == 10
    
    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
    ], datetime(2015, 1, 12, 10, 0, 30)) == 20
    
    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
    ], datetime(2015, 1, 12, 10, 0, 20)) == 30
    
    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
    ], datetime(2015, 1, 12, 10, 0, 10)) == 30
    
    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
    ], datetime(2015, 1, 12, 10, 0, 50)) == 0
    
    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
    ], datetime(2015, 1, 12, 10, 0, 30)) == 20
    
    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
    ], datetime(2015, 1, 12, 10, 0, 20)) == 30
    
    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
        (datetime(2015, 1, 12, 10, 1, 20), 2),
        (datetime(2015, 1, 12, 10, 1, 40), 2),
    ], datetime(2015, 1, 12, 10, 0, 20)) == 50
    
    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        (datetime(2015, 1, 12, 10, 0, 0), 2),
        datetime(2015, 1, 12, 10, 0, 10),
        (datetime(2015, 1, 12, 10, 1, 0), 2),
    ], datetime(2015, 1, 12, 10, 0, 30), datetime(2015, 1, 12, 10, 1, 0)) == 30
    
    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        (datetime(2015, 1, 12, 10, 0, 0), 2),
        datetime(2015, 1, 12, 10, 0, 10),
        (datetime(2015, 1, 12, 10, 1, 0), 2),
    ], datetime(2015, 1, 12, 10, 0, 20), datetime(2015, 1, 12, 10, 1, 0)) == 40
    
    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        (datetime(2015, 1, 12, 10, 0, 0), 2),
        datetime(2015, 1, 12, 10, 0, 10),
    ], datetime(2015, 1, 12, 10, 0, 0), datetime(2015, 1, 12, 10, 0, 30)) == 30
    
    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
    ], datetime(2015, 1, 12, 10, 0, 0), datetime(2015, 1, 12, 10, 1, 0)) == 40
    
    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
    ], datetime(2015, 1, 12, 10, 0, 0), datetime(2015, 1, 12, 10, 0, 10)) == 0
    
    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
    ], datetime(2015, 1, 12, 10, 0, 10), datetime(2015, 1, 12, 10, 0, 20)) == 10
    

    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
    ], datetime(2015, 1, 12, 10, 0, 10), datetime(2015, 1, 12, 10, 0, 20)) == 10
    
    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
    ], datetime(2015, 1, 12, 10, 0, 10), datetime(2015, 1, 12, 10, 0, 30)) == 20    

    assert sum_light(els=[
        (datetime(2015, 1, 11, 0, 0, 0), 3),
        datetime(2015, 1, 12, 0, 0, 0),
        (datetime(2015, 1, 13, 0, 0, 0), 3),
        (datetime(2015, 1, 13, 0, 0, 0), 2),
        datetime(2015, 1, 14, 0, 0, 0),
        (datetime(2015, 1, 15, 0, 0, 0), 2),
    ], start_watching=datetime(2015, 1, 10, 0, 0, 0), end_watching=datetime(2015, 1, 16, 0, 0, 0)) == 345600

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ], operating=timedelta(seconds=100)) == 10

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ], operating=timedelta(seconds=5)) == 5

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
        (datetime(2015, 1, 12, 10, 0, 0), 2),
        (datetime(2015, 1, 12, 10, 1, 0), 2),
    ], operating=timedelta(seconds=100)) == 60

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 30),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        (datetime(2015, 1, 12, 10, 1, 0), 2),
    ], operating=timedelta(seconds=100)) == 60

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 30),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        (datetime(2015, 1, 12, 10, 1, 0), 2),
    ], operating=timedelta(seconds=20)) == 40

    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
        (datetime(2015, 1, 12, 10, 1, 0), 3),
        (datetime(2015, 1, 12, 10, 1, 20), 3),
    ], operating=timedelta(seconds=10)) == 30

    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
        (datetime(2015, 1, 12, 10, 1, 20), 2),
        (datetime(2015, 1, 12, 10, 1, 40), 2),
    ], start_watching=datetime(2015, 1, 12, 10, 0, 20), operating=timedelta(seconds=100)) == 50

    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
        (datetime(2015, 1, 12, 10, 1, 20), 2),
        (datetime(2015, 1, 12, 10, 1, 40), 2),
    ], start_watching=datetime(2015, 1, 12, 10, 0, 20), operating=timedelta(seconds=10)) == 20

    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
    ], start_watching=datetime(2015, 1, 12, 10, 0, 10), end_watching=datetime(2015, 1, 12, 10, 0, 30),
    operating=timedelta(seconds=20)) == 20

    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
    ], start_watching=datetime(2015, 1, 12, 10, 0, 10), end_watching=datetime(2015, 1, 12, 10, 0, 30),
    operating=timedelta(seconds=10)) == 20

    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
    ], start_watching=datetime(2015, 1, 12, 10, 0, 10), end_watching=datetime(2015, 1, 12, 10, 0, 30),
    operating=timedelta(seconds=5)) == 10

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        (datetime(2015, 1, 12, 10, 0, 0), 2),
        datetime(2015, 1, 12, 10, 0, 10),
        (datetime(2015, 1, 12, 10, 1, 0), 2),
    ], req=1) == 60

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        (datetime(2015, 1, 12, 10, 0, 0), 2),
        datetime(2015, 1, 12, 10, 0, 10),
        (datetime(2015, 1, 12, 10, 1, 0), 2),
    ], req=2) == 10

    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
    ], req=1) == 40

    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
    ], req=2) == 20

    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
    ], req=3) == 0

    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 50), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
    ], req=3) == 10

    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
    ], datetime(2015, 1, 12, 10, 0, 0), datetime(2015, 1, 12, 10, 1, 0), req=2) == 20

    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
    ], datetime(2015, 1, 12, 10, 0, 0), datetime(2015, 1, 12, 10, 1, 0), req=2, operating=timedelta(seconds=15)) == 10

    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
        (datetime(2015, 1, 12, 10, 1, 20), 2),
        (datetime(2015, 1, 12, 10, 1, 40), 2),
    ], start_watching=datetime(2015, 1, 12, 10, 0, 20), operating=timedelta(seconds=100), req=2) == 20

    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
        (datetime(2015, 1, 12, 10, 1, 20), 2),
        (datetime(2015, 1, 12, 10, 1, 40), 2),
    ], start_watching=datetime(2015, 1, 12, 10, 0, 20), operating=timedelta(seconds=100), req=3) == 0

    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 0), 4),
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
        (datetime(2015, 1, 12, 10, 1, 20), 2),
        (datetime(2015, 1, 12, 10, 1, 40), 2),
    ], start_watching=datetime(2015, 1, 12, 10, 0, 20), operating=timedelta(seconds=100), req=3) == 20

    print("The forth mission in series is completed? Click 'Check' to earn cool rewards!")
