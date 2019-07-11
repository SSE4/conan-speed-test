from __future__ import print_function
from conans import ConanFile, CMake, tools
from os import path, getcwd, environ, rename


class CppRestSDKConan(ConanFile):
    name = "cpprestsdk"
    version = "2.10.13"
    description = "A project for cloud-based client-server communication in native code using a modern asynchronous " \
                  "C++ API design"
    topics = ("conan", "cpprestsdk", "rest", "client", "http")
    url = "https://github.com/bincrafters/conan-cpprestsdk"
    homepage = "https://github.com/Microsoft/cpprestsdk"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "MIT"
    generators = "cmake"

    settings = "os", "arch", "compiler", "build_type"
    options = {
        "shared": [True, False],
        "exclude_websockets": [True, False],
        "exclude_compression": [True, False],
        "fPIC": [True, False]
    }
    default_options = {
        "shared": False,
        "exclude_websockets": False,
        "fPIC": True,
        "exclude_compression": False
    }

    _source_subfolder = "source_subfolder"
    _build_subfolder = "build_subfolder"

    root = "%s-%s" % (name, version)
    short_paths = True

    def configure(self):
        if self.settings.compiler == 'Visual Studio':
            del self.options.fPIC

    def requirements(self):
        self.requires.add("OpenSSL/1.0.2r@conan/stable")
        if not self.options.exclude_compression:
            self.requires.add("zlib/1.2.11@conan/stable")
        if not self.options.exclude_websockets:
            self.requires.add("websocketpp/0.7.0@bincrafters/stable")
        self.requires.add("boost_random/1.69.0@bincrafters/stable")
        self.requires.add("boost_system/1.69.0@bincrafters/stable")
        self.requires.add("boost_thread/1.69.0@bincrafters/stable")
        self.requires.add("boost_filesystem/1.69.0@bincrafters/stable")
        self.requires.add("boost_chrono/1.69.0@bincrafters/stable")
        self.requires.add("boost_atomic/1.69.0@bincrafters/stable")
        self.requires.add("boost_asio/1.69.0@bincrafters/stable")
        self.requires.add("boost_date_time/1.69.0@bincrafters/stable")
        self.requires.add("boost_regex/1.69.0@bincrafters/stable")
        self.requires.add("cmake_findboost_modular/1.69.0@bincrafters/stable")

    def source(self):
        pass

    def build(self):
        pass

    def package(self):
        pass

    def package_info(self):
        pass
