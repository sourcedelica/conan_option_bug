# conan_option_bug

To reproduce:

1. `./create.sh` to create packages in local cache
2. `./install.sh` to run `conan install` for a test consumer

When installing you will get the error:

```
ERROR: cob-common/0.1@eric/test: Incompatible requirements obtained in different evaluations of 'requirements'
    Previous requirements: [cob-caf/0.1@eric/test, cob-zmq/0.1@eric/test]
    New requirements: [cob-caf/0.1@eric/test]
```

Description of the problem

`cob-common` has two options: `use_caf` (default=`True`) and `use_zmq`
(default=`False`).

`cob-client` requires `cob-common`.

`cob-service` requires `cob-common` with `use_zmq=True`.

The `test` consumer requires `cob-common`, `cob-client` and
`cob-service`. In its `conanfile.txt` it sets `cob-common:use_zmq=False`.

There is an error on installation because there is a conflict between
`cob-client` (`cob-common:use_zmq=False`) and `cob-service`
(`cob-common:use_zmq=True`). However, `conanfile.txt` should be resolving
the conflict by forcing `cob-common:use_zmq=False`. So there should be
no error. You should also be able to override the conflict by passing
`cob-common:use_zmq=False` on the command line.

The bug appears to be that the option from `conanfile.txt` is not being
used. You can see this happening by doing the following:

1. Edit `cob-common/conanfile.py`
2. Comment out the `requirements()` method.
3. `conan create . eric/test`
4. `conan create . eric/test -o cob-common:use_zmq=True`
5. `cd ../test/build`
6. `conan install ..`

You will get an error like:

```
cob-common/0.1@eric/test: WARN: Can't find a 'cob-common/0.1@eric/test' package for the specified options and settings:
- Settings: arch=x86_64, build_type=Debug, compiler=gcc, compiler.libcxx=libstdc++, compiler.version=6.2, os=Windows
- Options: use_caf=True, use_zmq=True
```

As you can see, it is not using the `cob-common:use_zmq=False` option
from `conanfile.txt`.