from .attractions import Attraction

class WaterTank(Attraction):
    def __init__(self, name, description):
        super().__init__(name, description)
