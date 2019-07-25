import requests
import time
'''
r = requests.get("https://a.jd.com//ajax/queryServerData.html")

print(r.elapsed.microseconds)

print(r.elapsed.total_seconds())

print(r.elapsed.total_seconds())
'''

def print_func_time(function):
    '''
    计算程序运行时间
    :param function:
    :return:
    '''


    def func_time(*args, **kwargs):
        t0 = time.clock()
        result = function(*args, **kwargs)
        t1 = time.clock()

        print("Total running time: %s s" % (str(t1 - t0)))
        return result

    return func_time

@print_func_time
def test():
    print(123)

test()