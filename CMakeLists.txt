# /CMakeLists.txt
#
# Main build file for cmake-include-guard
#
# See /LICENCE.md for Copyright information
project (CMakeForwardArguments)
cmake_minimum_required (VERSION 2.8 FATAL_ERROR)

include ("${CMAKE_CURRENT_LIST_DIR}/conanbuildinfo.cmake")
conan_basic_setup ()

include ("cmake/cmake-module-common/Common" OPTIONAL)

set (_CUR_LIST_DIR "${CMAKE_CURRENT_LIST_DIR}")
set (CMAKE_FILES
     "${_CUR_LIST_DIR}/IncludeGuard.cmake"
     "${_CUR_LIST_DIR}/CMakeLists.txt")
set (MARKDOWN_FILES
     "${CMAKE_CURRENT_LIST_DIR}/LICENSE"
     "${CMAKE_CURRENT_LIST_DIR}/README.md")

if (COMMAND cmake_module_add_common_targets)

    cmake_module_add_common_targets (NAMESPACE cmake
                                     CMAKE_FILES ${CMAKE_FILES}
                                     DOCUMENTATION_FILES ${MARKDOWN_FILES})

endif ()