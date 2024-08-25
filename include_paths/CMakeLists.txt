cmake_minimum_required(VERSION 3.29)
project(includes)

set(CMAKE_C_COMPILER "/usr/bin/clang-18")
set(CMAKE_CXX_COMPILER "/usr/bin/clang++-18")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -stdlib=libc++ -ftime-trace -g -O0")

add_executable(no_include_paths main.cpp)

add_executable(lots_of_include_paths main.cpp)

# Sorry if you don't have a Downloads or Pictures dir next to $HOME
target_include_directories(lots_of_include_paths
    PUBLIC
        $ENV{HOME}
        $ENV{HOME}/Downloads
        $ENV{HOME}/Pictures
        ${PROJECT_SOURCE_DIR}
        ${PROJECT_BINARY_DIR}
)
