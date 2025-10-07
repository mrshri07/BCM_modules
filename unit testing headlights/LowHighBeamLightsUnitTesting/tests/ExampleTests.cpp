#include <gtest/gtest.h>


extern "C" {
#include "../Example.hpp"
}


//low beam and high beam test cases

TEST(ExampleTests_T, low_beam_light)
{
    int ignition_swt=1;
    int pos_lig_swt=1;
    int low_beam_swt=2;
    int result=2;
    EXPECT_EQ(result,(ignition_swt,pos_lig_swt,low_beam_swt));
    //EXPECT_EQ(result,(ignition_swt,head_light_swt));
}

TEST(ExampleTests_T, low_beam_light1)
{
    int ignition_swt=1;
    int pos_lig_swt=1;
    int low_beam_swt=2;
    int result=3;
    EXPECT_NE(result,(ignition_swt,pos_lig_swt,low_beam_swt));
    //EXPECT_EQ(result,(ignition_swt,head_light_swt));
}


//high beam and high beam test cases
TEST(ExampleTests_T, high_beam_light)
{
    int ignition_swt=1;
    int pos_lig_swt=1;
    int low_beam_swt=2;
    int high_beam_swt=3;
    int result=3;
    EXPECT_EQ(result,(ignition_swt,pos_lig_swt,low_beam_swt, high_beam_swt));

}

TEST(ExampleTests_T, high_beam_light1)
{
    int ignition_swt=1;
    int pos_lig_swt=1;
    int low_beam_swt=2;
    int high_beam_swt=3;
    int result=2;
    EXPECT_NE(result,(ignition_swt,pos_lig_swt,low_beam_swt, high_beam_swt));

}
