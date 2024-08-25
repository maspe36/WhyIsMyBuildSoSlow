cmake_minimum_required(VERSION 3.29)
project(includes)

set(CMAKE_C_COMPILER "/usr/bin/clang-18")
set(CMAKE_CXX_COMPILER "/usr/bin/clang++-18")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -stdlib=libc++ -ftime-trace -g -O0")

add_library(includes slow.cpp fast.cpp)
