from conans import ConanFile, CMake


class CobConan(ConanFile):
    name = 'cob-service'
    version = '0.1'
    description = 'cob-service'
    exports_sources = '*.cpp', '*.h', 'CMakeLists.txt'
    url = 'https://github.com/sourcedelica/conan_option_bug.git'
    license = 'none'
    settings = 'os', 'compiler', 'build_type', 'arch'
    generators = 'cmake'

    # Dependencies
    requires = (
        'cob-common/0.1@eric/test'
    )

    # Options
    def configure(self):
        self.options['cob-common'].use_caf = True
        self.options['cob-common'].use_zmq = True

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy('*.h',   dst='include/%s' % self.name, src='.')
        self.copy('*.a',   dst='lib', keep_path=False)
        self.copy('*.lib', dst='lib', keep_path=False)

