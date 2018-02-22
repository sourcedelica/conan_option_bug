project(cob-caf CXX)
set(CMAKE_CXX_STANDARD 14)

if(EXISTS ${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
	include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
	conan_basic_setup(TARGETS)
endif()


set(SOURCE_FILES
		Caf.cpp)

add_library(cob-caf ${SOURCE_FILES})
add_library(Cob::Caf ALIAS cob-caf)
