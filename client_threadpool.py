from sys import maxsize
from concurrent.futures import ThreadPoolExecutor, as_completed
from kirim_data import kirim_data


def runThreadpool():
    pools = []
    try:
        with ThreadPoolExecutor() as executor:
            for k in range(maxsize):
                pools = [executor.submit(kirim_data, nama=f"thread ke -{k}")]

            for pool in as_completed(pools):
                pool.result()
    except Exception:
        print("limit reached")


if __name__ == '__main__':
    runThreadpool()
