from sys import maxsize
from multiprocessing import Process
from kirim_data import kirim_data


def runThreadProcess():
    for k in range(maxsize):
        process = Process(target=kirim_data, args=(k,))
        process.start()
        process.join()


if __name__ == '__main__':
    runThreadProcess()
