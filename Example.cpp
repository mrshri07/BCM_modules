#include"Example.hpp"
#include <stdio.h>
 
int mirror_fold();
int mirror_selection();
int mirror_control();
 
enum ignition_switch {OFF, ACC, ON, START};
enum fold_unfold_mirror_switch {FOLD = 0, UNFOLD = 1};
enum selection_mirror_switch {NEUTRAL = 0, LEFT = 1, RIGHT = 2};
enum control_mirror_switch {UP = 0, DOWN = 1, LEFT_CONTROL = 2, RIGHT_CONTROL = 3};
 
int Fold_Unfold_Mirror, selection_Mirror, control_Mirror;
int ignition_swt;
 
int main()
 {
    printf("Enter ignition switch (0 for OFF, 1 for ACC, 2 for ON, 3 for START): ");
    scanf("%d", &ignition_swt);
    printf("Enter Fold Unfold Switch (0 for FOLD, 1 for UNFOLD): ");
    scanf("%d", &Fold_Unfold_Mirror);
    printf("Enter selection switch (0 for NEUTRAL, 1 for LEFT, 2 for RIGHT): ");
    scanf("%d", &selection_Mirror);
    printf("Enter control switch (0 for UP, 1 for DOWN, 2 for LEFT, 3 for RIGHT): ");
    scanf("%d", &control_Mirror);
 
    mirror_fold();
    mirror_selection();
    mirror_control();
 
    return 0;
}
 
int mirror_fold() 
{
    if (ignition_swt == ACC)
     {
        if (Fold_Unfold_Mirror == UNFOLD)
        {
            printf("Unfold is activated\n");
        } 
        else 
        {
            printf("Fold is activated\n");
        }
    }
     else 
     {
        printf("Vehicle is below living mode\n");
     }
 
    return 0;
}
 
int mirror_selection()
 {
    if (ignition_swt == ACC)
     {
        if (Fold_Unfold_Mirror == FOLD) 
        {
            printf("Cannot select mirror while fold is activated\n");
        }
         else
          {
            if (selection_Mirror == LEFT)
            {
                printf("LEFT mirror is activated\n");
            } 
            else if (selection_Mirror == RIGHT)
            {
                printf("RIGHT mirror is activated\n");
            } 
            else
            {
                printf("NEUTRAL is activated\n");
            }
        }
    } 
    else 
    {
        printf("Vehicle is below living mode\n");
    }
 
    return 0;
}
 
int mirror_control()
 {
    if (ignition_swt == ACC)
     {
        if (Fold_Unfold_Mirror == FOLD)
        {
            printf("Cannot control mirror while fold is activated\n");
        } 
        else
         {
            if (control_Mirror == UP) 
            {
                printf("Mirror moved UP\n");
            }
             else if (control_Mirror == DOWN) 
             {
                printf("Mirror moved DOWN\n");
             }
             else if (control_Mirror == LEFT)
              {
                printf("Mirror moved LEFT\n");
             } 
            else if (control_Mirror == RIGHT)
             {
                printf("Mirror moved RIGHT\n");
             }
        }
    } 
    else 
    {
        printf("Vehicle is below living mode\n");
    }
 
    return 0;
}
 
