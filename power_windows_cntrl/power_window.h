#ifndef MAIN_HEADER_H
#define MAIN_HEADER_H

enum ign_switch {Off, Acc, Ign, Crank};
enum power_window {frnt_left = 1, frnt_right, rear_left, rear_right};
enum window {neutral,up, down};


int front_left_power_window(int ign_swt,int power_windowswt,int up_down_swt);
int front_right_power_window(int ign_swt,int power_windowswt,int up_down_swt);
int rear_left_power_window(int ign_swt,int power_windowswt,int up_down_swt);
int rear_right_power_window(int ign_swt,int power_windowswt,int up_down_swt);

 

#endif 

