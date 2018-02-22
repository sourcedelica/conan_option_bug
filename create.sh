#!/usr/bin/env bash
(cd cob-caf && conan create . eric/test)
(cd cob-zmq && conan create . eric/test)
(cd cob-common && conan create . eric/test)
(cd cob-common && conan create . eric/test -o cob-common:use_zmq=True)
(cd cob-client && conan create . eric/test)
(cd cob-service && conan create . eric/test)