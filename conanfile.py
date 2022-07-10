from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMakeDeps, CMake, cmake_layout
from conans.model import Generator
import json
import pkg_resources
import pathlib


class SphinxDocsConan(ConanFile):
    name = "sphinxdoc"
    version = "0.1.0"

    # Optional metadata
    license = "MIT"
    author = "Samuel Dowling <samuel.dowling@protonmail.com>"
    url = "https://github.com/samuel-emrys/sphinx-consumer.git"
    description = "This is a C++ package that uses sphinx to build its documentation"
    topics = ("<Put some tag here>", "<here>", "<and here>")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*", "include/*", "requirements.txt"
    python_requires = "pyvenv/0.1.0"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def requirements(self):
        self.requires("python-virtualenv/system")

        # self.options["python-virtualenv"].requirements = json.dumps([
        #     "sphinx==5.0.1",
        #     "sphinx-book-theme==0.3.2",
        # ])
        with pathlib.Path("requirements.txt").open() as requirements_txt:
            self.options["python-virtualenv"].requirements = json.dumps([
                str(requirement) for requirement in pkg_resources.parse_requirements(requirements_txt)
            ])


    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

        dp = CMakeDeps(self)
        dp.generate()

        py = self.python_requires["pyvenv"].module.CMakePythonDeps(self)
        py.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["sphinxdoc"]
