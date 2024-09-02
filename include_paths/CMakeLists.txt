cmake_minimum_required(VERSION 3.29)
project(includes)

function(target_include_generated_directories target num)
    set(gen_dicts)

    if(NOT num EQUAL 0)
        foreach (i RANGE 1 ${num})
            list(APPEND gen_dicts "generated/folder_${i}")
        endforeach ()
    endif ()

    # We always have this include directory. This is what we actually reference our header from.
    # But, this goes at the end. This is to hopefully simulate it as the last `-I` to try and
    # force the compiler to spend as much time searching as possible for a header.
    list(APPEND "generated/")

    target_include_directories(${target} PRIVATE ${gen_dicts})
endfunction()

set(CMAKE_C_COMPILER "/usr/bin/clang-18")
set(CMAKE_CXX_COMPILER "/usr/bin/clang++-18")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -stdlib=libc++ -ftime-trace -g -O0")

add_executable(one_include_path main.cpp)
target_include_generated_directories(one_include_path 0)

add_executable(ten_include_paths main.cpp)
target_include_generated_directories(ten_include_paths 10)

add_executable(hundred_include_paths main.cpp)
target_include_generated_directories(hundred_include_paths 100)
