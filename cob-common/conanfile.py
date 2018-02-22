from conans import ConanFile, CMake


class CobConan(ConanFile):
    name = 'cob-common'
    version = '0.1'
    description = 'cob-common'
    exports_sources = '*.cpp', '*.h', 'CMakeLists.txt'
    url = 'https://github.com/sourcedelica/conan_option_bug.git'
    license = 'none'
    settings = 'os', 'compiler', 'build_type', 'arch'
    generators = 'cmake'

    # Options
    options = {'use_caf': [True, False], 'use_zmq': [True, False]}
    default_options = 'use_caf=True', 'use_zmq=False'

    # Optional dependencies
    def requirements(self):
        if self.options.use_caf:
            self.requires('cob-caf/0.1@eric/test')
        if self.options.use_zmq:
            self.requires('cob-zmq/0.1@eric/test')

    def build(self):
        cmake = CMake(self)
        definitions = {}
        if self.options.use_caf:
            definitions['USE_CAF'] = 'ON'
        if self.options.use_zmq:
            definitions['USE_ZMQ'] = 'ON'
        cmake.configure(defs=definitions)
        cmake.build()

    def package(self):
        self.copy('*.h',   dst='include/%s' % self.name, src='.')
        self.copy('*.a',   dst='lib', keep_path=False)
        self.copy('*.lib', dst='lib', keep_path=False)

