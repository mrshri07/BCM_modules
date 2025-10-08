#include <gtest/gtest.h>


extern "C" {
#include "../Example.hpp"
}

/* Mirror is UNFOLD*/
TEST(ExampleTests_T, mirror_fold)
{
     int ignition_swt = 1;//1 for ACC Mode
     int Fold_Unfold_Mirror = 1;//1 for UNFOLD Mirror
     int result = 1;
     EXPECT_EQ(result,(ignition_swt, Fold_Unfold_Mirror));
}

TEST(ExampleTests_T, mirror_fold1)
{
     int ignition_swt = 1;//1 for ACC Mode
     int Fold_Unfold_Mirror = 1;//1 for UNFOLD Mirror
     int result = 0;
     EXPECT_NE(result,(ignition_swt, Fold_Unfold_Mirror));
}





// /*Mirror Selection is LEFT*/
// TEST(ExampleTests_T, mirror_selection)
// {
//       int ignition_swt = 1;
//       int Fold_Unfold_Mirror = 1;
//       int selection_Mirror = 1;//1 for LEFT Mirror
//       int result = 1;
//       EXPECT_EQ(result, (ignition_swt, Fold_Unfold_Mirror, selection_Mirror));
// }

// TEST(ExampleTests_T, mirror_selection1)
// {
//       int ignition_swt = 1;
//       int Fold_Unfold_Mirror = 1;
//       int selection_Mirror = 1;//1 for LEFT Mirror
//       int result = 0;
//       EXPECT_NE(result, (ignition_swt, Fold_Unfold_Mirror, selection_Mirror));
// }

// /*Mirror Selection is RIGHT*/
// /*TEST(ExampleTests_T, mirror_selection1)
// {
//       int ignition_swt = 1;
//       int Fold_Unfold_Mirror = 1;
//       int selection_Mirror = 2;
//       int result = 2;
//       EXPECT_EQ(result, (ignition_swt, Fold_Unfold_Mirror, selection_Mirror));
// }*/

// /*Mirror Control is UP */
// TEST(ExampleTests_T, mirror_control)
// {
//       int ignition_swt = 1;
//       int Fold_Unfold_Mirror = 1;// 1 for Mirror is UNFOLD
//       int selection_Mirror = 1;//1 for LEFT Mirror
//       int control_Mirror = 0;//0 for Mirror moved to UP
//       int result = 0;
//       EXPECT_EQ(result, (ignition_swt, Fold_Unfold_Mirror, selection_Mirror, control_Mirror));
// }

// TEST(ExampleTests_T, mirror_control1)
// {
//       int ignition_swt = 1;
//       int Fold_Unfold_Mirror = 1;// 1 for Mirror is UNFOLD
//       int selection_Mirror = 1;//1 for LEFT Mirror
//       int control_Mirror = 0;//0 for Mirror moved to UP
//       int result = 1;
//       EXPECT_NE(result, (ignition_swt, Fold_Unfold_Mirror, selection_Mirror, control_Mirror));
// }

// /*Mirror Control is DOWN */
// TEST(ExampleTests_T, mirror_control2)
// {
//       int ignition_swt = 1;
//       int Fold_Unfold_Mirror = 1;// 1 for Mirror is UNFOLD
//       int selection_Mirror = 1;//1 for LEFT Mirror
//       int control_Mirror = 1;//1 for Mirror moved to DOWN
//       int result = 1;
//       EXPECT_EQ(result, (ignition_swt, Fold_Unfold_Mirror, selection_Mirror, control_Mirror));
// }

// TEST(ExampleTests_T, mirror_control3)
// {
//       int ignition_swt = 1;
//       int Fold_Unfold_Mirror = 1;// 1 for Mirror is UNFOLD
//       int selection_Mirror = 1;//1 for LEFT Mirror
//       int control_Mirror = 1;//1 for Mirror moved to DOWN
//       int result = 0;
//       EXPECT_NE(result, (ignition_swt, Fold_Unfold_Mirror, selection_Mirror, control_Mirror));
// }

// /*Mirror Control is LEFT  */
// TEST(ExampleTests_T, mirror_control4)
// {
//       int ignition_swt = 1;
//       int Fold_Unfold_Mirror = 1;// 1 for Mirror is UNFOLD
//       int selection_Mirror = 1;//1 for LEFT Mirror
//       int control_Mirror = 2;//2 for Mirror moved to LEFT
//       int result = 2;
//       EXPECT_EQ(result, (ignition_swt, Fold_Unfold_Mirror, selection_Mirror, control_Mirror));
// }

// TEST(ExampleTests_T, mirror_control5)
// {
//       int ignition_swt = 1;
//       int Fold_Unfold_Mirror = 1;// 1 for Mirror is UNFOLD
//       int selection_Mirror = 1;//1 for LEFT Mirror
//       int control_Mirror = 2;//2 for Mirror moved to LEFT
//       int result = 1;
//       EXPECT_NE(result, (ignition_swt, Fold_Unfold_Mirror, selection_Mirror, control_Mirror));
// }

// /*Mirror Control is RIGHT */
// TEST(ExampleTests_T, mirror_control6)
// {
//       int ignition_swt = 1;
//       int Fold_Unfold_Mirror = 1;// 1 for Mirror is UNFOLD
//       int selection_Mirror = 1;//1 for LEFT Mirror
//       int control_Mirror = 3;//3 for Mirror moved to RIGHT
//       int result = 3;
//       EXPECT_EQ(result, (ignition_swt, Fold_Unfold_Mirror, selection_Mirror, control_Mirror));
// }

// TEST(ExampleTests_T, mirror_control7)
// {
//       int ignition_swt = 1;
//       int Fold_Unfold_Mirror = 1;// 1 for Mirror is UNFOLD
//       int selection_Mirror = 1;//1 for LEFT Mirror
//       int control_Mirror = 3;//3 for Mirror moved to RIGHT
//       int result = 2;
//       EXPECT_NE(result, (ignition_swt, Fold_Unfold_Mirror, selection_Mirror, control_Mirror));
// }



// /* When Ignition is OFF then Side view Mirror does not work*/
// TEST(ExampleTests_T, mirror_control8)
// {
//       int ignition_swt = 0;//0 for Ignition OFF
//       int Fold_Unfold_Mirror = 1;// give any value (0 or 1)When iginition is OFF
//       int selection_Mirror = 1;// give any value (0,1,2)When iginition is OFF
//       int control_Mirror = 3;// give any value (0,1,2,3)When iginition is OFF
//      int result;
//       if(ignition_swt == 0)
//       {
//            result = 0;
//       }
//       else {
//           result = Fold_Unfold_Mirror && selection_Mirror && control_Mirror;
//       }

//       EXPECT_EQ(result, (ignition_swt));
// }




// TEST(ExampleTests_T, mirror_control9)
// {
//       int ignition_swt = 0;//0 for Ignition OFF
//       int Fold_Unfold_Mirror = 1;// give any value (0 or 1)When iginition is OFF
//       int selection_Mirror = 1;// give any value (0,1,2)When iginition is OFF
//       int control_Mirror = 3;// give any value (0,1,2,3)When iginition is OFF
//      int result;
//       if(ignition_swt == 0)
//       {
//            result = 1;
//       }
//       else {
//           result = Fold_Unfold_Mirror && selection_Mirror && control_Mirror;
//       }

//       EXPECT_NE(result, (ignition_swt));
// }



// /*When Mirror is FOLD, Selection And Control mirror does not work even Iginition is ON*/
// TEST(ExampleTests_T, mirror_control10)
// {
//       int ignition_swt = 1;//Ignition is ACC mode
//       int Fold_Unfold_Mirror = 0;//Mirror is FOLD
//       int selection_Mirror = 1;//give any value(0,1,2) when mirror is FOLD
//       int control_Mirror = 1;//give any value(0,1,2,3) when mirror is FOLD
//       int result ;
//      if(ignition_swt == 1)
//       {
//           if(Fold_Unfold_Mirror == 0)
//           {
//            result = 0;
//           }
//           else{
//                result =  selection_Mirror && control_Mirror;
//           }
//       }
     
//      EXPECT_EQ(result, (Fold_Unfold_Mirror));
// }


// TEST(ExampleTests_T, mirror_control11)
// {
//       int ignition_swt = 1;
//       int Fold_Unfold_Mirror = 0;//Mirror is FOLD
//       int selection_Mirror = 1;//give any value(0,1,2) when mirror is FOLD
//       int control_Mirror = 1;//give any value(0,1,2,3) when mirror is FOLD
//       int result ;
//      if(ignition_swt == 1)
//       {
//           if(Fold_Unfold_Mirror == 0)
//           {
//            result = 1;
//           }
//           else{
//                result =  selection_Mirror && control_Mirror;
//           }
//       }
     
//      EXPECT_NE(result, (Fold_Unfold_Mirror));
// }



