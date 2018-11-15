cmake_minimum_required(VERSION 2.8.3)
project(asr_sick_lms_400)

#use c++ 11
add_definitions(-std=gnu++0x)

find_package(catkin REQUIRED COMPONENTS
  roscpp
)


catkin_package(
  CATKIN_DEPENDS roscpp
  INCLUDE_DIRS include
  LIBRARIES asr_sick_lms_400)

include_directories(include
      ${catkin_INCLUDE_DIRS}
      ${CMAKE_CURRENT_BINARY_DIR}
      )


add_library(asr_sick_lms_400
    src/sick_lms400.cpp
  )

target_link_libraries(asr_sick_lms_400
    ${catkin_LIBRARIES}
    ${ROS_LIBRARIES}
)

add_dependencies(asr_sick_lms_400
	${catkin_EXPORTED_TARGETS}
)

add_executable(sick_lms400
  src/sick_lms400_node.cpp)
target_link_libraries(sick_lms400 asr_sick_lms_400)


install(TARGETS asr_sick_lms_400
  DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION})

install(
    TARGETS
      sick_lms400
    RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})


install(FILES include/${PROJECT_NAME}/sick_lms400.h
   DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION})
