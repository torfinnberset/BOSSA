cmake_minimum_required(VERSION 3.15)

project(bossa CXX)

set(CMAKE_CXX_STANDARD 17)

add_library(bossa
        src/CmdOpts.cpp
        src/Samba.cpp
        src/Flash.cpp
        src/D5xNvmFlash.cpp
        src/D2xNvmFlash.cpp
        src/EfcFlash.cpp
        src/EefcFlash.cpp
        src/Applet.cpp
        src/WordCopyApplet.cpp
        src/WordCopyArm.cpp
        src/Flasher.cpp
        src/Device.cpp
        src/PosixSerialPort.cpp
        src/OSXPortFactory.cpp
        )

target_include_directories(bossa PUBLIC ${CMAKE_CURRENT_LIST_DIR}/BOSSA/src)