#include <gtest/gtest.h>
#include <gmock/gmock.h>
#include "power_windowstests_mock.hpp"


MockHardware* mockHardware;
extern "C" {
#include "../power_windows_cntrl/power_window.h"

// Mock function that calls the mock object
int power_window_reporterror() {
    return mockHardware->power_window_reporterror();
}


}

   



/*Front left power window*/
// TEST(Example_test_t,frnt_left_power_windows)
// {
//     int ign_swt=Acc;
//     int power_windowswt=frnt_left;
//     int up_down_swt=up;
//     int result=1;
//     EXPECT_EQ(result,front_left_power_window(ign_swt,power_windowswt,up_down_swt));
   
// }

TEST(Example_test_t,frnt_left_power_windows1)
{
    int ign_swt=Acc;
    int power_windowswt=frnt_left;
    int up_down_swt=down;
    int result=1;
    EXPECT_NE(result,front_left_power_window(ign_swt,power_windowswt,up_down_swt));
   
}

TEST(Example_test_t,frnt_left_power_windows2)
{
    int ign_swt=0;
    int power_windowswt=frnt_left;
    int up_down_swt=up;
    int result=1;
    EXPECT_NE(result,front_left_power_window(ign_swt,power_windowswt,up_down_swt));
   
}



// TEST(ExampleTests_T, test_power_window_oor)
// {
//     MockHardware mock;
//     mockHardware = &mock;

//     EXPECT_CALL(mock, power_window_reporterror())
//         .Times(2)
//         .WillRepeatedly(::testing::Return(5));
    
//     int ignition_swt = 9;
//     int power_windowswt=frnt_left;
//     int up_down_swt=up;
//     int result=10;
//     EXPECT_EQ(result,front_left_power_window(ignition_swt,power_windowswt,up_down_swt));
//     EXPECT_EQ(result,front_left_power_window(ignition_swt,power_windowswt,up_down_swt));
// }

 
// //  int main(int argc, char **argv) {
// //     testing::InitGoogleTest(&argc, argv);
// //     return RUN_ALL_TESTS();
// // }
 


// /*Front right power window*/
// TEST(Example_test_t,frnt_right_power_windows)
// {
//     int ign_swt=Acc;
//     int power_windowswt=frnt_right;
//     int up_down_swt=down;
//     int result=2;
//     EXPECT_EQ(result,front_right_power_window(ign_swt,power_windowswt,up_down_swt));
   
// }



// TEST(ExampleTests_T, testfrnt_right_power_window_oor)
// {
//     MockHardware mock;
//     mockHardware = &mock;

//     EXPECT_CALL(mock, power_window_reporterror())
//         .Times(2)
//         .WillRepeatedly(::testing::Return(-5));
    
//     int ignition_swt = 10;
//     int power_windowswt=frnt_right;
//     int up_down_swt=down;
//     int result=-10;
//     EXPECT_EQ(result,front_right_power_window(ignition_swt,power_windowswt,up_down_swt));
//     EXPECT_EQ(result,front_right_power_window(ignition_swt,power_windowswt,up_down_swt));
// }

 
//  int main(int argc, char **argv) {
//     testing::InitGoogleTest(&argc, argv);
//     return RUN_ALL_TESTS();
// }
 


// /*Rear left power window*/
// TEST(Example_test_t,rear_left_power_windows)
// {
//     int ign_swt=Acc;
//     int power_windowswt=rear_left;
//     int up_down_swt=down;
//     int result=2;
//     EXPECT_EQ(result,rear_left_power_window(ign_swt,power_windowswt,up_down_swt));
   
// }




// TEST(ExampleTests_T, testrear_left_power_window_oor)
// {
//     MockHardware mock;
//     mockHardware = &mock;

//     EXPECT_CALL(mock, power_window_reporterror())
//         .Times(2)
//         .WillRepeatedly(::testing::Return(-5));
    
//     int ignition_swt = 10;
//     int power_windowswt=rear_left;
//     int up_down_swt=down;
//     int result=-10;
//     EXPECT_EQ(result,rear_left_power_window(ignition_swt,power_windowswt,up_down_swt));
//     EXPECT_EQ(result,rear_left_power_window(ignition_swt,power_windowswt,up_down_swt));
// }



// /*Rear right power window*/
// TEST(Example_test_t,rear_right_power_windows)
// {
//     int ign_swt=Acc;
//     int power_windowswt=rear_right;
//     int up_down_swt=up;
//     int result=1;
//     EXPECT_EQ(result,rear_right_power_window(ign_swt,power_windowswt,up_down_swt));
// }



// TEST(ExampleTests_T, testrear_right_power_window_oor)
// {
//     MockHardware mock;
//     mockHardware = &mock;

//     EXPECT_CALL(mock, power_window_reporterror())
//         .Times(2)
//         .WillRepeatedly(::testing::Return(-5));
    
//     int ignition_swt = 10;
//     int power_windowswt=rear_right;
//     int up_down_swt=down;
//     int result=-10;
//     EXPECT_EQ(result,rear_right_power_window(ignition_swt,power_windowswt,up_down_swt));
//     EXPECT_EQ(result,rear_right_power_window(ignition_swt,power_windowswt,up_down_swt));
// }

