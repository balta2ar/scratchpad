cmake_minimum_required(VERSION 3.1)
project(robot)
add_executable(${PROJECT_NAME} robot.cpp)

set(THREADS_PREFER_PTHREAD_FLAG ON)
find_package(Threads REQUIRED)
target_link_libraries(${PROJECT_NAME} Threads::Threads)

# add_library(robot robot.cpp)
# target_include_directories(robot PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
# target_link_libraries(robot LINK_PUBLIC robot)

# include_directories("${PROJECT_BINARY_DIR}")
