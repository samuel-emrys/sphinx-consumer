cmake_minimum_required(VERSION 3.15)
project(sphinxdoc CXX)

add_library(sphinxdoc src/sphinxdoc.cpp)
target_include_directories(sphinxdoc PUBLIC include)

set_target_properties(sphinxdoc PROPERTIES PUBLIC_HEADER "include/sphinxdoc.h")

add_subdirectory("docs")

install(TARGETS sphinxdoc)
