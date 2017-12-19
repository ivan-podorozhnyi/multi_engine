import argparse

from metrics import CpuMetrics, MemoryMetrics
from multiprocessing.dummy import Pool as ThreadPool
import time


class Engine:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.metrics = []
        self.pool = ThreadPool(4)

    def apply_arguments(self):
        self.parser.add_argument("-cpu",
                                 help="Check cpu load.", action="store_true")
        self.parser.add_argument("-mem",
                                 help="Check memory load.", action="store_true")
        self.parser.add_argument("-pause",
                                 help="Pause between checks", type=int)
        self.parser.add_argument("-time",
                                 help="Total time", type=int)

    def run_metrics(self):
        args = self.parser.parse_args()
        self.append_metrics(args)

        if args.time:
            execution_time = 0
            while execution_time < args.time:
                execution_time += args.pause
                time.sleep(args.pause)
                self.append_metrics(args)

        results = self.pool.map(lambda x: x.check(), self.metrics)
        print(results)

    def append_metrics(self, args):
        if args.cpu:
            self.metrics.append(CpuMetrics())
            # CpuMetrics().check()
            # print("CPU")
        if args.mem:
            self.metrics.append(MemoryMetrics())
            # MemoryMetrics().check()
            # print("Memory")


def main():
    engine = Engine()
    engine.apply_arguments()
    engine.run_metrics()


if __name__ == '__main__':
    main()
