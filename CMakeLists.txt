cmake_minimum_required(VERSION 3.14)

project(bossa CXX)

set(CMAKE_CXX_STANDARD 17)

add_library(bossa
        BOSSA/src/CmdOpts.cpp
        BOSSA/src/Samba.cpp
        BOSSA/src/Flash.cpp
        BOSSA/src/D5xNvmFlash.cpp
        BOSSA/src/D2xNvmFlash.cpp
        BOSSA/src/EfcFlash.cpp
        BOSSA/src/EefcFlash.cpp
        BOSSA/src/Applet.cpp
        BOSSA/src/WordCopyApplet.cpp
        BOSSA/src/WordCopyArm.cpp
        BOSSA/src/Flasher.cpp
        BOSSA/src/Device.cpp
        BOSSA/src/PosixSerialPort.cpp
        BOSSA/src/OSXPortFactory.cpp
        )

target_include_directories(bossa PUBLIC ${CMAKE_CURRENT_LIST_DIR}/BOSSA/src)