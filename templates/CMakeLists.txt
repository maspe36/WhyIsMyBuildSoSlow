cmake_minimum_required(VERSION 3.29)
project(templates)

set(CMAKE_C_COMPILER "/usr/bin/clang-18")
set(CMAKE_CXX_COMPILER "/usr/bin/clang++-18")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -stdlib=libc++ -ftime-trace -g -O0")

add_executable(templates a.cpp b.cpp main.cpp)
target_compile_options(templates PRIVATE "-ftemplate-depth=8192")

# Exact same source code, but with an explicit template instantiation in a precompiled header
add_executable(templates_pch a.cpp b.cpp main.cpp)
target_precompile_headers(templates_pch PRIVATE pch.h)
target_compile_options(templates_pch PRIVATE "-ftemplate-depth=8192")

# Exact same source code again but now lets also build a library that doesn't depend on the pch header
add_executable(templates_pch_with_foo a.cpp b.cpp main.cpp)
target_precompile_headers(templates_pch_with_foo PRIVATE pch.h)
target_compile_options(templates_pch_with_foo PRIVATE "-ftemplate-depth=8192")

add_library(foo foo.cpp)
target_link_libraries(templates_pch_with_foo PRIVATE foo)
