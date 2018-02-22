#!/usr/bin/env bash
cd test
rm -rf build
mkdir build
cd build
conan install ..