# Name of the test executable
set(TestName ExampleTest)
 
# Source files for the test
set(Sources
    ExampleTest.cpp
)
 
# Create the test executable
add_executable(${TestName} ${Sources})
 
# Link it with gtest, gtest_main, and the main Example library
target_link_libraries(${TestName} gtest gtest_main Example)
 
# Register the test with CTest
add_test(NAME ${TestName} COMMAND ${TestName})
 
