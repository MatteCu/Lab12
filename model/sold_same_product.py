from dataclasses import dataclass


@dataclass
class SoldTheSame:
    id:int
    ret1:int
    ret2:int
    prod:int
    def __hash__(self):
        return hash(self.id)
