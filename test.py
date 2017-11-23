#  ____ ____ ____ ____ ____ ____ _________ ____ ____ ____ ____ _________ ____ ____ ____ ____
# ||I |||n |||s |||e |||r |||t |||       |||C |||o |||d |||e |||       |||H |||e |||r |||e ||
# ||__|||__|||__|||__|||__|||__|||_______|||__|||__|||__|||__|||_______|||__|||__|||__|||__||
# |/__\|/__\|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|


def minority_shape_intersect(first_minority_shape, second_minority_shape):
    return ()


#   *   )             )
# ` )  /(   (      ( /( (          (  (
#  ( )(_)) ))\ (   )\()))\   (     )\))(
# (_(_()) /((_))\ (_))/((_)  )\ ) ((_))\
# |_   _|(_)) ((_)| |_  (_) _(_/(  (()(_)
#   | |  / -_)(_-<|  _| | || ' \))/ _` |
#   |_|  \___|/__/ \__| |_||_||_| \__, |
#                                 |___/


SENSITIVITY = 0.001
tests = []


# Test X (On the instruction PDF)

text_x_calculations = minority_shape_intersect(
    [(4., 8.), (20.6, 10.), (9.4, 18.1)],
    [(12.5, 7.), (18.7, 16.2), (2., 12.), (12.5, 11.3)]
)

test_x_results = [
    (12.5, 11.3),
    (12.5, 9.024096385542167),
    (13.984606613454961, 9.202964652223491),
    (16.513454260733393, 12.955448257862459),
    (13.748900224891674, 14.954813230212277),
    (6.781560380848003, 13.202548119734228),
    (5.996175908221797, 11.733588272785214)
]

test_x = ("X", test_x_results, text_x_calculations)

tests.append(test_x)


# Test Uber Basic

test_uber_basic_calculations = minority_shape_intersect(
    [(-6, 6), (0, 6), (0, -6), (-6, -6)],
    [(-2, -2), (-2, 2), (0, 0)]
)

test_uber_basic_results = [
    (-2, -2),
    (-2, 2),
    (0, 0)
]

test_uber_basic = ("Uber Basic", test_uber_basic_results,
                   test_uber_basic_calculations)

tests.append(test_uber_basic)


# Insert your own cool named test here

# Right below this comment


# Ok thats enough

import datetime
print ""

for test in tests:

    start_time = datetime.datetime.now()

    name, results, calculations = test

    results_length = len(results)
    calculations_length = len(calculations)

    is_failed = False

    print "Test", name
    print "-" * 30

    if results_length != calculations_length:
        print "(!) Failed: Correct results has", results_length, "items, but calculations has", calculations_length
        is_failed = True
    else:
        print "(~) Passed: Correct results has", results_length, "items, calculations also has", calculations_length

    print ""

    for result in results:

        is_calculated = False

        for calculation in calculations:
            if abs(result[0] - calculation[0]) <= SENSITIVITY and abs(result[1] - calculation[1]) <= SENSITIVITY:
                is_calculated = True
                break

        if is_calculated:
            print "(~) Passed:", result
        else:
            print "(!) Failed:", result
            is_failed = True

    print ""

    finish_time = datetime.datetime.now()

    if is_failed:
        print "Test", name, "failed. (In " + str((finish_time - start_time).total_seconds() * 1000) + " milliseconds)"
    else:
        print "Test", name, "passed. (In " + str((finish_time - start_time).total_seconds() * 1000) + " milliseconds)"

    print ""