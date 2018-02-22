from conans import ConanFile, CMake


class CobConan(ConanFile):
    name = 'cob-client'
    version = '0.1'
    description = 'cob-client'
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
    options = {'use_zmq_transport': [True, False]}
    default_options = 'use_zmq_transport=False'

    def configure(self):
        self.options['cob-common'].use_caf = not self.options.use_zmq_transport
        self.options['cob-common'].use_zmq = self.options.use_zmq_transport

    def build(self):
        cmake = CMake(self)
        definitions = {}
        if self.options.use_zmq_transport:
            definitions['USE_ZMQ_TRANSPORT'] = 'ON'
        cmake.configure(defs=definitions)
        cmake.build()

    def package(self):
        self.copy('*.h',   dst='include/%s' % self.name, src='.')
        self.copy('*.a',   dst='lib', keep_path=False)
        self.copy('*.lib', dst='lib', keep_path=False)

