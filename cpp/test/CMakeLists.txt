
add_executable(test_hamming test_hamming.cpp main.cpp)
target_include_directories(test_hamming PRIVATE "/c/Users/u52450/src/doctest")
target_link_libraries(test_hamming hamming)
# install(TARGETS test_hamming RUNTIME DESTINATION bin)
