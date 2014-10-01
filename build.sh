#!/bin/bash

TOP_DIR=${PWD}

rm -rf "${TOP_DIR}/RPMS"
rm -rf "%{TOP_DIR}/SRPMS"

mock --buildsrpm \
        --verbose \
        --define "dist .el7" \
        --resultdir="${TOP_DIR}/SRPMS" \
        --spec ${TOP_DIR}/SPECS/*.spec \
        --sources "${TOP_DIR}/SOURCES"

mock --rebuild \
        --verbose \
        --define "dist .el7" \
        --resultdir="${TOP_DIR}/RPMS" \
        ${TOP_DIR}/SRPMS/*.src.rpm

# EOF
