#include <gmock/gmock.h>
// Mock class for the hardware interface
class MockHardware {
public:
    MOCK_METHOD(int, power_window_reporterror, (), (const)); /*Mock function without arguments and return nothing*/
};

// Global pointer to the mock object
extern MockHardware* mockHardware;