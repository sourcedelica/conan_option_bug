project(cob-zmq CXX)
set(CMAKE_CXX_STANDARD 14)

if(EXISTS ${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
	include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
	conan_basic_setup(TARGETS)
endif()


set(SOURCE_FILES
        Zmq.cpp)

add_library(cob-zmq ${SOURCE_FILES})
add_library(Cob::Zmq ALIAS cob-zmq)
