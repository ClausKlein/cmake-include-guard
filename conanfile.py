from conans import ConanFile
from conans.tools import download, unzip
import os

VERSION = "0.0.7"


class CMakeIncludeGuardConan(ConanFile):
    name = "cmake-include-guard"
    version = os.environ.get("CONAN_VERSION_OVERRIDE", VERSION)
    generators = "cmake"
    url = "http://github.com/polysquare/cmake-include-guard"
    licence = "MIT"

    def source(self):
        zip_name = "cmake-include-guard.zip"
        download("https://github.com/polysquare/"
                 "cmake-include-guard/archive/{version}.zip"
                 "".format(version="v" + VERSION),
                 zip_name)
        unzip(zip_name)
        os.unlink(zip_name)

    def package(self):
        self.copy(pattern="*.cmake",
                  dst="cmake/cmake-include-guard",
                  src="cmake-include-guard-" + VERSION,
                  keep_path=True)
