cmake_minimum_required(VERSION 3.0)

project(hamming_it_up)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

add_subdirectory(cpp/hamming)
add_subdirectory(cpp/test)
# add_executable(hamming main.cpp)
# 
# install(TARGETS practice_project RUNTIME DESTINATION bin)
