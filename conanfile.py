from conans import ConanFile, CMake, tools


class BossaConan(ConanFile):
    name = "bossa"
    version = "1.9.2"
    license = "BSD-3"
    url = "https://github.com/torfinnberset/BOSSA"
    description = "BOSSA is a flash programming utility for Atmel's SAM family of flash-based ARM microcontrollers"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        git = tools.Git(folder="BOSSA")
        git.clone("https://github.com/torfinnberset/BOSSA", "conan-pkg")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="BOSSA")
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="BOSSA/src", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
