project(cob-service CXX)
set(CMAKE_CXX_STANDARD 14)

if(EXISTS ${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
	include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
	conan_basic_setup(TARGETS)
endif()


set(SOURCE_FILES
		Service.cpp)

add_library(cob-service ${SOURCE_FILES})
add_library(Cob::Service ALIAS cob-service)

target_link_libraries(cob-service PUBLIC
		CONAN_PKG::cob-common)

target_compile_definitions(cob-service PUBLIC USE_CAF USE_ZMQ)