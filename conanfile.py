from conans import ConanFile, CMake, tools


class BossaConan(ConanFile):
    name = "bossa"
    version = "1.9.1+bloom1"
    license = "BSD-3"
    url = "https://github.com/torfinnberset/BOSSA"
    description = "BOSSA is a flash programming utility for Atmel's SAM family of flash-based ARM microcontrollers"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    exports_sources = ["src/*", "CMakeLists.txt"]

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="src", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
