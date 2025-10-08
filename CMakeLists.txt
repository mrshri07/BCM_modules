cmake_minimum_required(VERSION 3.14)
 
set(This Example)
project(${This} C CXX)
 
set(CMAKE_C_STANDARD 99)
set(CMAKE_CXX_STANDARD 11)
 
# REMOVE FetchContent — not needed for local googletest
# include(FetchContent)
# FetchContent_Declare(
#   googletest
#   URL https://github.com/google/googletest/archive/refs/heads/main.zip
# )
# FetchContent_MakeAvailable(googletest)
 
# Use local googletest directory
# Use local googletest directory
add_subdirectory(googletest)
 
enable_testing()
 
set(Headers
    Example.hpp
)
set(Sources
    Example.cpp
)
 
add_library(${This} STATIC ${Sources} ${Headers})
 
# Let test folder handle its own linking
add_subdirectory(test)
 
 
