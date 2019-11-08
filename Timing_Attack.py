import binascii
import os
import random
import timeit
import numpy


def string_compare(a, b):
    for i in range(0, len(b)):
        if a[i] == b[i]:
            continue
        else:
            return False
    return True


def better_string_compare(a, b):
    if len(a) != len(b):
        return False
    result = 0
    for x, y in zip(a, b):
        result |= ord(x) ^ ord(y)
    return result == 0


original_pass = '%030x' % random.randrange(16**1000000)
f = open("original_pass.txt", mode='w')
f.write(original_pass)
pass_len = len(original_pass)

ff = open("pass_guesses.txt", mode='w')

first_guess = '%030x' % random.randrange(16**1000000)
ff.write(first_guess)
ff.write('\n')

start1 = timeit.timeit()
string_compare(original_pass, first_guess)
stop1 = timeit.timeit()
timer1 = stop1 - start1

sec_guess = original_pass[0:len(original_pass)/2]+'%030x' % random.randrange(16**500000)
ff.write(sec_guess)
ff.write('\n')

start2 = timeit.timeit()
string_compare(original_pass, sec_guess)
stop2 = timeit.timeit()
timer2 = stop2 - start2

third_pass = original_pass[0:750000]+'%030x' % random.randrange(16**250000)
ff.write(third_pass)
ff.write('\n')

start3 = timeit.timeit()
string_compare(original_pass, third_pass)
stop3 = timeit.timeit()
timer3 = stop3 - start3

temp = binascii.b2a_hex(os.urandom(1))
fourth_guess = original_pass[0:pass_len]+temp[0:0]
ff.write(fourth_guess)
ff.write('\n')

start4 = timeit.timeit()
string_compare(original_pass, fourth_guess)
stop4 = timeit.timeit()
timer4 = stop4 - start4

ff.write(original_pass)

start5 = timeit.timeit()
string_compare(original_pass, original_pass)
stop5 = timeit.timeit()
timer5 = stop5 - start5

average = (timer1 + timer2 + timer3 + timer4 + timer5) / 5

array = [timer1, timer2, timer3, timer4, timer5]
arr = numpy.array(array)
deviation = numpy.std(arr)

variance = numpy.var(arr)

print (str(average) + ';' + str(deviation) + ';' + str(variance))

start_1 = timeit.timeit()
better_string_compare(original_pass, first_guess)
stop_1 = timeit.timeit()

timer_1 = stop_1 - start_1

start_2 = timeit.timeit()
better_string_compare(original_pass, sec_guess)
stop_2 = timeit.timeit()

timer_2 = stop_2 - start_2

start_3 = timeit.timeit()
better_string_compare(original_pass, third_pass)
stop_3 = timeit.timeit()

timer_3 = stop_3 - start_3

start_4 = timeit.timeit()
better_string_compare(original_pass, fourth_guess)
stop_4 = timeit.timeit()

timer_4 = stop_4 - start_4

start_5 = timeit.timeit()
better_string_compare(original_pass, original_pass)
stop_5 = timeit.timeit()

timer_5 = stop_5 - start_5

average2 = (timer_1 + timer_2 + timer_3 + timer_4 + timer_5) / 5

array_2 = [timer_1, timer_2, timer_3, timer_4, timer_5]
arr2 = numpy.array(array_2)
deviation2 = numpy.std(arr2)

variance2 = numpy.var(arr2)

print (str(average2) + ';' + str(deviation2) + ';' + str(variance2))
