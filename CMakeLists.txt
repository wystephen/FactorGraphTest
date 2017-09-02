cmake_minimum_required(VERSION 3.8)
project(FactorGraphTest)

set(CMAKE_CXX_STANDARD 11)




set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -o3 -std=c++11  -msse2 -msse3 -msse4 -lopencv_aruco -lpthread -lSophus ")
#set(CUDA_NVCC_FLAGSS ${CUDA_NVCC_FLAGS} --gpu-architecture sm_20)


#find_package(CUDA REQUIRED)
#include(FindCUDA)
find_package(Eigen3 REQUIRED)

#find_package(PythonLibs 3.0 REQUIRED)
find_package(PythonLibs 2.7 REQUIRED)

find_package(Sophus REQUIRED)
if (SOPHUS_FOUND)
    message("Sophus_FOUND")
endif ()


find_package(OpenMP)
find_package(BLAS)
find_package(LAPACK)


LIST(APPEND CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/cmake_modules)
message(${CMAKE_MODULE_PATH})
# G2O
SET(G2O_ROOT /usr/local/include/g2o)
FIND_PACKAGE(G2O)
FIND_PACKAGE(CSparse)

find_package(Pangolin 0.2 QUIET)

## decide if we have pangolin
#if (Pangolin_FOUND)
#    message("--- found PANGOLIN, compiling dso_pangolin library.")
#    include_directories( ${Pangolin_INCLUDE_DIRS} )
#    set(dso_pangolin_SOURCE_FILES
#            ${PROJECT_SOURCE_DIR}/src/IOWrapper/Pangolin/KeyFrameDisplay.cpp
#            ${PROJECT_SOURCE_DIR}/src/IOWrapper/Pangolin/PangolinDSOViewer.cpp)
#    set(HAS_PANGOLIN 1)
#else ()
#    message("--- could not find PANGOLIN, not compiling dso_pangolin library.")
#    message("    this means there will be no 3D display / GUI available for dso_dataset.")
#    set(dso_pangolin_SOURCE_FILES )
#    set(HAS_PANGOLIN 0)
#endif ()

# Find GTSAM components
find_package(GTSAM REQUIRED) # Uses installed package
include_directories(${GTSAM_INCLUDE_DIR})
set(GTSAM_LIBRARIES gtsam)   # TODO: automatic search libs

find_package(GTSAMCMakeTools)
include(GtsamMakeConfigFile)
include(GtsamBuildTypes)
include(GtsamTesting)

if (OPENMP_FOUND)
    message("OPENMP FOUND")
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${OpenMP_C_FLAGS}")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${OpenMP_CXX_FLAGS}")
    set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} ${OpenMP_EXE_LINKER_FLAGS}")
endif ()

SET(G2O_ROOT /usr/local/include/g2o)
FIND_PACKAGE(G2O)
FIND_PACKAGE(CSparse)

include_directories(
        ./include
        ${EIGEN3_INCLUDE_DIR}
        /usr/local/cuda/include
        /home/steve/Cpp_Extent/Cpp_Extent
        ${PYTHON_INDCLUDE_PATH}
        /usr/include
        /usr/local/include
        ${Sophus_INCLUDE_DIRS}
        ${BLAS_INCLUDE_DIRS}
        /usr/local/include
        ${CSPARSE_INCLUDE_DIR}
        ${G2O_INCLUDE_DIR}
        ${Pangolin_INCLUDE_DIRS}
        ${GTSAM_INCLUDE_DIR}
)



link_directories(
        /usr/local/lib/
        /usr/lib/
        /usr/lib/x86_64-linux-gnu/
        ${BLAS_LIBRARIES}
        ${LAPACK_LIBRARIES}
        #        ./include
)


SET(G2O_LIBS g2o_cli g2o_ext_freeglut_minimal g2o_simulator
        g2o_solver_slam2d_linear g2o_types_icp g2o_types_slam2d
        g2o_core g2o_interface g2o_solver_csparse g2o_solver_structure_only
        g2o_types_sba g2o_types_slam3d g2o_csparse_extension g2o_opengl_helper
        g2o_solver_dense g2o_stuff g2o_types_sclam2d g2o_parser g2o_solver_pcg
        g2o_types_data g2o_types_sim3 cxsparse
        g2o_types_slam3d_addons)

set(Sophus_LIBRARIES libSophus.so)







########################################

#find_package(Boost REQUIRED)
#find_package(GTSAM REQUIRED)

#include_directories(
#        ${Boost_INCLUDE_DIR}
#        ${GTSAM_INCLUDE_DIR}
#
#)

add_executable(ImuFactTest src/ImuFactorsExample.cpp)
target_link_libraries(ImuFactTest
        -ltbb ${GTSAM_LIBRARIES} ${Boost_LIBRARIES})