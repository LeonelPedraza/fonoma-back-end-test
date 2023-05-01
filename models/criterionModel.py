from enum import Enum

class CriterionModel(str, Enum):
    completed='completed'
    pending='pending'
    canceled='canceled'
    all='all'