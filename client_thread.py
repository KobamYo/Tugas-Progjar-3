from threading import Thread
from kirim_data import kirim_data
import sys


def client():
    try:
        for i in range(sys.maxsize):
            kirim_data(i)

    except Exception:
        print("limit reached")


if __name__ == "__main__":
    client()
