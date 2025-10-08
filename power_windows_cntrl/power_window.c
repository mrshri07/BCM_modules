
#include <stdio.h>
//#include "frnt_left_pow_window.h"
#include "power_window.h"
int ign_swt;
int power_windowswt;
int up_down_swt;
int frnt_left_windowswt;
int stop;
int power_window_positions[9] = {0, 1, 2, 3, 4, 5, 6, 7, 8};
int front_left_power_window(int ign_swt,int power_windowswt,int up_down_swt) 
{
    if (ign_swt == Acc) 
    {
        if (up_down_swt == neutral) 
        {
            printf("Front left power window is in neutral state.\n");
            return 0;
        } 
        else if (up_down_swt == down) 
        {
            for (int i = 8; i >= 0; i--) 
            {
                printf("%d ", power_window_positions[i]);
              
                if (stop == power_window_positions[i])
                 {
                    printf("\nWindow stopped at position %d\n", power_window_positions[i]);
                    break;
                   
                }
            }
            
            if (stop == 0) {
                printf("\nFront left power window is fully down\n");
            }
             return 2;
        } 
        else if (up_down_swt == up)
        {
            for (int i = 0; i <= 8; i++) 
            {
                printf("%d ", power_window_positions[i]);
                
                if (stop == power_window_positions[i] && stop != 0)
                 {
                    printf("\nWindow stopped at position %d\n", power_window_positions[i]);
                    break;
             
                }
            }
           
            if (stop == 0) {
                printf("\nFront left power window is fully up\n");
            }
            return 1;
        }
         else
          {
            // return power_window_reporterror();
            // return -1;
            printf("Invalid input\n");
         
        }
        printf("\n");
    }
     else 
     {
         if(power_window_reporterror() >0)
         {
            return 10;
         }
         else{
            return -10;
         }
        printf("Ignition is off. Power windows cannot be operated.\n");
        return 0;
         
       
    }
}

//front right power window

int front_right_power_window(int ign_swt,int power_windowswt,int up_down_swt)
 {
    if (ign_swt == Acc ) 
    {
        if (up_down_swt == neutral) 
        {
            printf("Front right power window is in neutral state.\n");
            return 0;
        } 
        else if (up_down_swt == down) 
        {
            for (int i = 8; i >= 0; i--)
             {
                printf("%d ", power_window_positions[i]);
                if (stop == power_window_positions[i])
                 {
                    printf("\nWindow stopped at position %d\n", power_window_positions[i]);
                    break;
                }
            }
           
            if (stop == 0)
             {
                printf("\nFront right power window is fully down\n");
            }
             return 2;
        } 
        else if (up_down_swt == up) 
        {
            for (int i = 0; i <= 8; i++) 
            {
                printf("%d ", power_window_positions[i]);
                if (stop == power_window_positions[i] && stop != 0) 
                {
                    printf("\nWindow stopped at position %d\n", power_window_positions[i]);
                    break;
                }
            }
           // return 2;
            if (stop == 0) 
            {
                printf("\nFront right power window is fully up\n");
            }
             return 1;
        } 
        else {
        
            printf("Invalid input\n");
           // return -1;
        }
        printf("\n");
    } 
    else {

         if(power_window_reporterror() > 0)
         {
            return 10;
         }
         else{
            return-10;
         }
        printf("Ignition is off. Power windows cannot be operated.\n");
        return 0;
       // return -3;
        }
}


//rear left power window

int rear_left_power_window(int ign_swt,int power_windowswt,int up_down_swt) {
    if (ign_swt == Acc )
     {
        if (up_down_swt == neutral) 
        {
            printf("Rear left power window is in neutral state.\n");
            return 0;
        } 
        else if (up_down_swt == down)
         {
            for (int i = 8; i >= 0; i--) 
            {
                printf("%d ", power_window_positions[i]);
                if (stop == power_window_positions[i]) {
                    printf("\nWindow stopped at position %d\n", power_window_positions[i]);
                    break;
                }
            }
           // return 1;
            if (stop == 0) {
                printf("\nRear left power window is fully down\n");
            }
             return 2;
        } 
        else if (up_down_swt == up) 
        {
            for (int i = 0; i <= 8; i++) 
            {
                printf("%d ", power_window_positions[i]);
                if (stop == power_window_positions[i] && stop != 0) {
                    printf("\nWindow stopped at position %d\n", power_window_positions[i]);
                    break;
                }
            }
            //return 2;
            if (stop == 0) {
                printf("\nRear left power window is fully up\n");
            }
             return 1;
        }
         else
          {
            // power_window_reporterror();
            printf("Invalid input\n");
           // return -1;

        }
        printf("\n");
    } else 
    {
          if(power_window_reporterror() > 0)
         {
            return 10;
         }
         else{
            return-10;
         }
        printf("Ignition is off. Power windows cannot be operated.\n");
        return 0;
        }
}



//rear right power window
int rear_right_power_window(int ign_swt,int power_windowswt,int up_down_swt) 
{
    if (ign_swt == Acc )
     {
        if (up_down_swt == neutral) 
        {
            printf("Rear right power window is in neutral state.\n");
            return 0;
        } 
        else if (up_down_swt == down) 
        {
            for (int i = 8; i >= 0; i--)
             {
                printf("%d ", power_window_positions[i]);
                if (stop == power_window_positions[i]) 
                {
                    printf("\nWindow stopped at position %d\n", power_window_positions[i]);
                    break;
                }
            }
            //return 1;
            if (stop == 0) 
            {
                printf("\nRear right power window is fully down\n");
            }
             return 2;
        }
         else if (up_down_swt == up)
          {
            for (int i = 0; i <= 8; i++) 
            {
                printf("%d ", power_window_positions[i]);
                if (stop == power_window_positions[i] && stop != 0)
                 {
                    printf("\nWindow stopped at position %d\n", power_window_positions[i]);
                    break;
                }
            }
            //return 2;
            if (stop == 0) {
                printf("\nRear right power window is fully up\n");
            }
             return 1;
        } 
        else 
        {
            printf("Invalid input\n");
            //return -1;
        }
        printf("\n");
    } 
    else 
    {
          if(power_window_reporterror() > 0)
         {
            return 10;
         }
         else{
            return-10;
         }
        printf("Ignition is off. Power windows cannot be operated.\n");
      return 0;
    }
}


