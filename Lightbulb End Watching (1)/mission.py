# Taken from mission Lightbulb Start Watching

# Taken from mission Lightbulb Intro

from datetime import datetime
from typing import List

def sum_light(els: List[datetime], start_watching: List[datetime] = datetime(1, 1, 1)) -> int:
    els = sorted(els + [start_watching])
    i = els.index(start_watching)
    return sum([(els[j + 1] - els[j]).total_seconds() for j in range(i + (i % 2 == 0), len(els), 2)])

if __name__ == '__main__':
    print("Example:")
    print(sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10 , 10),
        datetime(2015, 1, 12, 11, 0 , 0),
        datetime(2015, 1, 12, 11, 10 , 10),
    ]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_light(els=[
        datetime(2015, 1, 12, 10, 0 , 0),
        datetime(2015, 1, 12, 10, 10 , 10),
    ]) == 610

    assert sum_light([
        datetime(2015, 1, 12, 10, 0 , 0),
        datetime(2015, 1, 12, 10, 10 , 10),
        datetime(2015, 1, 12, 11, 0 , 0),
        datetime(2015, 1, 12, 11, 10 , 10),
    ]) == 1220

    assert sum_light([
        datetime(2015, 1, 12, 10, 0 , 0),
        datetime(2015, 1, 12, 10, 10 , 10),
        datetime(2015, 1, 12, 11, 0 , 0),
        datetime(2015, 1, 12, 11, 10 , 10),
        datetime(2015, 1, 12, 11, 10 , 10),
        datetime(2015, 1, 12, 12, 10 , 10),
    ]) == 4820

    assert sum_light([
        datetime(2015, 1, 12, 10, 0 , 0),
        datetime(2015, 1, 12, 10, 0 , 1),
    ]) == 1

    assert sum_light([
        datetime(2015, 1, 12, 10, 0 , 0),
        datetime(2015, 1, 12, 10, 0 , 10),
        datetime(2015, 1, 12, 11, 0 , 0),
        datetime(2015, 1, 13, 11, 0 , 0),
    ]) == 86410

    print("The first mission in series is completed? Click 'Check' to earn cool rewards!")


if __name__ == "__main__":
    print("Example:")
    print(
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            datetime(2015, 1, 12, 10, 0, 5),
        )
    )

    assert (
        sum_light(
            els=[
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            start_watching=datetime(2015, 1, 12, 10, 0, 5),
        )
        == 5
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            datetime(2015, 1, 12, 10, 0, 0),
        )
        == 10
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 11, 0, 0),
        )
        == 610
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 11, 0, 10),
        )
        == 600
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 10, 10, 0),
        )
        == 620
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
                datetime(2015, 1, 12, 11, 10, 11),
                datetime(2015, 1, 12, 12, 10, 11),
            ],
            datetime(2015, 1, 12, 12, 10, 11),
        )
        == 0
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
                datetime(2015, 1, 12, 11, 10, 11),
                datetime(2015, 1, 12, 12, 10, 11),
            ],
            datetime(2015, 1, 12, 12, 9, 11),
        )
        == 60
    )

    print("The second mission in series is done? Click 'Check' to earn cool rewards!")


from datetime import datetime
from typing import List, Optional

def sum_light(els: List[datetime], start_watching: Optional[datetime] = None, end_watching: Optional[datetime] = None) -> int:
    """
        how long the light bulb has been turned on
    """
    return 0


if __name__ == '__main__':
    print("Example:")
    print(sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ],
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 0, 10)))
    
    assert sum_light(els=[
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ],
    start_watching=datetime(2015, 1, 12, 10, 0, 0),
    end_watching=datetime(2015, 1, 12, 10, 0, 10)) == 10
    
    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ],
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 0, 7)) == 7
    
    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ],
    datetime(2015, 1, 12, 10, 0, 3),
    datetime(2015, 1, 12, 10, 0, 10)) == 7
    
    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ],
    datetime(2015, 1, 12, 10, 0, 10),
    datetime(2015, 1, 12, 10, 0, 20)) == 0
    
    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ],
    datetime(2015, 1, 12, 10, 30, 0),
    datetime(2015, 1, 12, 11, 0, 0)) == 0
    
    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ],
    datetime(2015, 1, 12, 10, 10, 0),
    datetime(2015, 1, 12, 11, 0, 0)) == 10
    
    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ],
    datetime(2015, 1, 12, 10, 10, 0),
    datetime(2015, 1, 12, 11, 0, 10)) == 20
    
    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ],
    datetime(2015, 1, 12, 9, 50, 0),
    datetime(2015, 1, 12, 10, 0, 10)) == 10
    
    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ],
    datetime(2015, 1, 12, 9, 0, 0),
    datetime(2015, 1, 12, 10, 5, 0)) == 300
    
    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ],
    datetime(2015, 1, 12, 11, 5, 0),
    datetime(2015, 1, 12, 12, 0, 0)) == 310
    
    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
    ],
    datetime(2015, 1, 12, 11, 5, 0),
    datetime(2015, 1, 12, 11, 10, 0)) == 300
    
    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
    ],
    datetime(2015, 1, 12, 10, 10, 0),
    datetime(2015, 1, 12, 11, 0, 10)) == 20
    
    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
    ],
    datetime(2015, 1, 12, 9, 10, 0),
    datetime(2015, 1, 12, 10, 20, 20)) == 610
    
    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
    ],
    datetime(2015, 1, 12, 9, 10, 0),
    datetime(2015, 1, 12, 10, 20, 20)) == 1220
    
    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
    ],
    datetime(2015, 1, 12, 9, 9, 0),
    datetime(2015, 1, 12, 10, 0, 0)) == 0
    
    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
    ],
    datetime(2015, 1, 12, 9, 9, 0),
    datetime(2015, 1, 12, 10, 0, 10)) == 10
    
    print("The third mission in series is completed? Click 'Check' to earn cool rewards!")