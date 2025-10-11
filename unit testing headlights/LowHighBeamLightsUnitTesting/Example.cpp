#include "Example.hpp"

#include <stdio.h>

enum ignition_swt {OFF, ACC, ON, START};
enum Head_light_swt {pos_lig = 1, low_beam_light , high_beam_light };

int ignition_lwr;
int head_light_swt;
int low_beam_swt;
int high_beam_swt;
int pos_lig_swt;
void check_low_beam_light(int ignition_swt, int pos_lig_swt, int low_beam_swt);
void check_high_beam_light(int ignition_swt, int pos_lig_swt, int low_beam_swt, int high_beam_swt);
int main()
{
    printf("Enter ignition switch (0 for OFF, 1 for ACC, 2 for ON, 3 for START): ");
    scanf("%d", &ignition_swt);
    printf("Enter head light switch (1 for Position Light): ");
   // scanf("%d", &head_light_swt);
    scanf("%d", &pos_lig_swt);
    printf("Enter head light switch (2 for Low Beam Light): ");
    scanf("%d", &low_beam_swt);
    printf("Enter head light switch (3 for High Beam Light): ");
    scanf("%d", &high_beam_swt);
    check_low_beam_light(ignition_swt, pos_lig_swt, low_beam_swt);
    check_high_beam_light(ignition_swt, pos_lig_swt, low_beam_swt, high_beam_swt);
    return 0;
}
void check_low_beam_light(int ignition_swt, int pos_lig_swt, int low_beam_lig)
{
    if (ignition_swt == ACC)
    {
        //if (head_light_swt == pos_lig)s
         if (pos_lig_swt == pos_lig)
        {
            printf("Position Light is ON\n");
            if (low_beam_swt == low_beam_light)
            {
                printf("Low Beam Light is ON\n");
            }
            else
            {
                printf("Low Beam Light is OFF\n");
            }
        }
        else
        {
            printf("Position Light is OFF\n");
        }
    }
    else
    {
        printf("Vehicle is below living mode\n");
    }
}
void check_high_beam_light(int ignition_swt, int pos_lig_swt, int low_beam_swt, int high_beam_swt)
{
    if (ignition_swt == ACC)
    {
       // if (head_light_swt == pos_lig && low_beam_swt == low_beam_light)
        if (pos_lig_swt == pos_lig && low_beam_swt == low_beam_light)
        {
            if (high_beam_swt == high_beam_light)
            {
                printf("High Beam Light is ON\n");
            }
            else
            {
                printf("High Beam Light is OFF\n");
            }
        }
    }
}
