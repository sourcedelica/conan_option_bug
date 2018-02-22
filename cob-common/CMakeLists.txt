project(cob-common CXX)
set(CMAKE_CXX_STANDARD 14)

if(EXISTS ${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
	include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
	conan_basic_setup(TARGETS)
endif()


set(SOURCE_FILES
		Common.cpp)

add_library(cob-common ${SOURCE_FILES})
add_library(Cob::Common ALIAS cob-common)

if (USE_CAF)
	message(STATUS "cob-common: USE_CAF")
	target_link_libraries(cob-common PUBLIC
			CONAN_PKG::cob-caf)
	target_compile_definitions(cob-common PUBLIC
			USE_CAF)
endif()

if (USE_ZMQ)
	message(STATUS "cob-common: USE_ZMQ")
	target_link_libraries(cob-common PUBLIC
			CONAN_PKG::cob-zmq)
	target_compile_definitions(cob-common PUBLIC
			USE_ZMQ)
endif()
