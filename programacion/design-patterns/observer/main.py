from random import randint

from abs_clases import Publisher, Suscriber


class UVSolarSystem(Publisher):
    
    def emit_value(self):
        value = randint(0, 100)
        self.notify_suscribers(value)

class UVTracker(Suscriber):
    
    def update(self, value) -> None:
        print(f"UVTracker: {value}")
        print("Doing funny stuff with this value :D")

class UVPlantTracker (Suscriber):

    def update(self, value) -> None:
        print(f"UVPlantTracker: {value}")
        print("Doing funny stuff for the plants with this value :D")

if __name__ == "__main__":
    print("Stage 1".center(50, "="))
    
    # define the publisher
    solar_system = UVSolarSystem()
    
    solar_system.emit_value()

    print("Stage 2".center(50, "="))
    # first suscriber
    uv_tracker = UVTracker()
    
    solar_system.add_suscriber(uv_tracker)
    solar_system.emit_value()
    
    print("Stage 3".center(50, "="))
    # second suscriber
    uv_plant_tracker = UVPlantTracker()
    
    solar_system.add_suscriber(uv_plant_tracker)
    solar_system.emit_value()
    
    print("Stage 4".center(50, "="))
    # remove the first suscriber
    solar_system.remove_suscriber(uv_tracker)
    solar_system.emit_value()
    