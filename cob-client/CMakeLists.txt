project(cob-client CXX)
set(CMAKE_CXX_STANDARD 14)

if(EXISTS ${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
	include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
	conan_basic_setup(TARGETS)
endif()


set(SOURCE_FILES
		Client.cpp)

add_library(cob-client ${SOURCE_FILES})
add_library(Cob::client ALIAS cob-client)

target_link_libraries(cob-client PUBLIC
		CONAN_PKG::cob-common)

if (USE_ZMQ_TRANSPORT)
	message(STATUS "cob-client: USE_ZMQ_TRANSPORT")
	target_compile_definitions(cob-client PUBLIC USE_ZMQ_TRANSPORT USE_ZMQ USE_PROTO)
else()
	message(STATUS "cob-client: USE_ZMQ_TRANSPORT not defined")
	target_compile_definitions(cob-client PUBLIC USE_CAF)
endif()