"""
    Build script for test.py
    test-builder.py
"""

from os.path import join
from SCons.Script import AlwaysBuild, Builder, Default, DefaultEnvironment

env = DefaultEnvironment()
platform = env.PioPlatform()

VICE_DIR = platform.get_package_dir("tool-vice")

# A full list with the available variables
# http://www.scons.org/doc/production/HTML/scons-user.html#app-variables
env.Replace(
    AR="llvm-ar",
    AS="mos-c64-clang",
    CC="mos-c64-clang",
    CXX="mos-c64-clang++",
    OBJCOPY="llvm-objcopy",
    RANLIB="llvm-ranlib",

    UPLOADER=join(VICE_DIR, "bin", "x64sc"),
    UPLOADCMD="$UPLOADER $SOURCES"
)

env.Append(
    # ARFLAGS=["..."],

    # ASFLAGS=["flag1", "flag2", "flagN"],
    # CCFLAGS=["flag1", "flag2", "flagN"],
    # CXXFLAGS=["flag1", "flag2", "flagN"],
    # LINKFLAGS=["flag1", "flag2", "flagN"],

    # CPPDEFINES=["DEFINE_1", "DEFINE=2", "DEFINE_N"],

    # LIBS=["additional", "libs", "here"],

    BUILDERS=dict(
        ElfToBin=Builder(
            action=" ".join([
                "$OBJCOPY",
                "-O",
                "binary",
                "$SOURCES",
                "$TARGET"]),
            suffix=".bin"
        )
    )
)

# The source code of "platformio-build-tool" is here
# https://github.com/platformio/platformio-core/blob/develop/platformio/builder/tools/platformio.py

#
# Target: Build executable and linkable firmware
#
target_elf = env.BuildProgram()

# #
# # Target: Build the .bin file
# #
# target_bin = env.ElfToBin(join("$BUILD_DIR", "firmware"), target_elf)

#
# Target: Upload firmware
#
upload = env.Alias(["upload"], target_elf, "$UPLOADCMD")
AlwaysBuild(upload)

#
# Target: Define targets
#
Default(target_elf)