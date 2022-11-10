ARG GCC_VERSION
FROM ghcr.io/peterkappelt/arm-gcc-docker:$GCC_VERSION

ARG SDK_FOLDER
RUN test -n "$SDK_FOLDER" || (echo "SDK_FOLDER  not set" && false)

RUN mkdir /sdk
COPY "./$SDK_FOLDER" "/sdk"
COPY ./Makefile.posix /sdk/components/toolchain/gcc/