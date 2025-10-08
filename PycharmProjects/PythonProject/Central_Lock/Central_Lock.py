from dataclasses import dataclass, field
from typing import Dict, Tuple

# --- Configuration Constants ---
MAX_LOCK_SPEED = 5.0    # km/h - Maximum speed at which locking is allowed
MAX_UNLOCK_SPEED = 50.0 # km/h - Maximum speed at which unlocking is allowed

# --- Central Lock System Implementation ---
@dataclass
class CentralLockSystem:
    power_on: bool = True
    speed_kmh: float = 0.0
    doors: Dict[str, bool] = field(default_factory=lambda: {
        "front_left": False,
        "front_right": False,
        "rear_left": False,
        "rear_right": False
    })  # True means door is open
    locked: bool = False
    sensors_ok: bool = True
    child_lock_engaged: bool = False

    # --- Helper Methods ---
    def is_any_door_open(self) -> bool:
        """Check if any door is open."""
        return any(self.doors.values())

    # --- Preconditions ---
    def preconditions_for_lock(self) -> Tuple[bool, str]:
        """Check all conditions before locking."""
        if not self.power_on:
            return False, "Power is off"
        if not self.sensors_ok:
            return False, "Sensor error"
        if self.is_any_door_open():
            return False, "One or more doors are open"
        if self.speed_kmh > MAX_LOCK_SPEED:
            return False, f"Vehicle speeding ({self.speed_kmh} km/h) - cannot lock above {MAX_LOCK_SPEED} km/h"
        return True, "OK"

    def preconditions_for_unlock(self) -> Tuple[bool, str]:
        """Check all conditions before unlocking."""
        if not self.power_on:
            return False, "Power is off"
        if not self.sensors_ok:
            return False, "Sensor error"
        if self.speed_kmh > MAX_UNLOCK_SPEED:
            return False, f"Vehicle speeding ({self.speed_kmh} km/h) - cannot unlock above {MAX_UNLOCK_SPEED} km/h"
        return True, "OK"

    # --- Actions ---
    def lock_all(self) -> Tuple[bool, str]:
        ok, msg = self.preconditions_for_lock()
        if ok:
            self.locked = True
            return True, "Locked"
        return False, msg

    def unlock_all(self) -> Tuple[bool, str]:
        ok, msg = self.preconditions_for_unlock()
        if ok:
            self.locked = False
            return True, "Unlocked"
        return False, msg

    # --- Simulation Controls ---
    def set_speed(self, speed_kmh: float):
        self.speed_kmh = speed_kmh

    def set_power(self, on: bool):
        self.power_on = on

    def set_sensor_status(self, ok: bool):
        self.sensors_ok = ok

    def open_door(self, door_name: str):
        if door_name in self.doors:
            self.doors[door_name] = True

    def close_door(self, door_name: str):
        if door_name in self.doors:
            self.doors[door_name] = False


# --- Test Cases ---
def run_tests():
    passed = 0
    failed = 0

    def expect(condition, test_name):
        nonlocal passed, failed
        if condition:
            print(f"✅ PASS: {test_name}")
            passed += 1
        else:
            print(f"❌ FAIL: {test_name}")
            failed += 1

    # Test 1: Lock when all doors closed and stationary
    cls = CentralLockSystem()
    cls.set_speed(0)
    ok, msg = cls.lock_all()
    expect(ok and cls.locked and msg == "Locked", "Lock when all doors closed & stationary")

    # Test 2: Lock fails if door open
    cls = CentralLockSystem()
    cls.open_door("rear_left")
    ok, msg = cls.lock_all()
    expect(not ok and not cls.locked and "open" in msg.lower(), "Lock fails if any door open")

    # Test 3: Lock fails if speed too high
    cls = CentralLockSystem()
    cls.set_speed(MAX_LOCK_SPEED + 10)
    ok, msg = cls.lock_all()
    expect(not ok and not cls.locked and "speeding" in msg.lower(), "Lock fails at high speed")

    # Test 4: Unlock fails if power off
    cls = CentralLockSystem(locked=True)
    cls.set_power(False)
    ok, msg = cls.unlock_all()
    expect(not ok and cls.locked and "power" in msg.lower(), "Unlock fails if power off")

    # Test 5: Unlock fails if high speed
    cls = CentralLockSystem(locked=True)
    cls.set_speed(MAX_UNLOCK_SPEED + 10)
    ok, msg = cls.unlock_all()
    expect(not ok and cls.locked and "speeding" in msg.lower(), "Unlock fails at high speed")

    # Test 6: Sensor failure prevents locking/unlocking
    cls = CentralLockSystem()
    cls.set_sensor_status(False)
    ok_lock, msg1 = cls.lock_all()
    ok_unlock, msg2 = cls.unlock_all()
    expect(not ok_lock and not ok_unlock, "Sensor failure blocks commands")

    # Test 7: Normal unlock at 0 km/h
    cls = CentralLockSystem(locked=True)
    cls.set_speed(0)
    ok, msg = cls.unlock_all()
    expect(ok and not cls.locked and msg == "Unlocked", "Unlock at stationary speed")

    # --- Summary ---
    print("\n--- TEST SUMMARY ---")
    print(f"✅ Passed: {passed}")
    print(f"❌ Failed: {failed}")
    if failed == 0:
        print("🎯 All test cases passed successfully!")


# --- Run all tests ---
if __name__ == "__main__":
    run_tests()
