from abc import abstractmethod, ABC


class Metrics(ABC):

    @abstractmethod
    def check(self):
        pass


class CpuMetrics(Metrics):
    def __init__(self):
        self._cpu_load = 0

    def check(self):
        return "cpu tested successfully "


class MemoryMetrics(Metrics):
    def __init__(self):
        self._cpu_load = 0

    def check(self):
        return "memory tested successfully "
