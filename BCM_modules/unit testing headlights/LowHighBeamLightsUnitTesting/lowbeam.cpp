#include "lowbeam.hpp"
#include "Example02.hpp"

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