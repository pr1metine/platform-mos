import os
import sys
from warnings import warn
from platformio.public import PlatformBase

IS_WINDOWS = sys.platform.startswith("win")
IS_LINUX = sys.platform.startswith("linux")
IS_MAC = sys.platform.startswith("darwin")

class MOSPlatform(PlatformBase):
    def get_boards(self, id_=None):
        result = super().get_boards(id_)
        return result

    def configure_default_packages(self, variables, targets):
        # until toolchain is not yet approved in PIO registry: redirect packages at will here
        # (temporary)
        if IS_LINUX:
            self.packages["toolchain-llvm-mos"]["version"] = "https://github.com/pr1metine/pio-toolchain-llvm-mos-linux.git"
            self.packages["tool-vice"]["optional"] = True
            warn("VICE will not be installed. Please install this with your favorite package manager: https://www.addictivetips.com/ubuntu-linux-tips/play-commodore-64-games-on-linux/")
        elif IS_MAC:
            self.packages["toolchain-llvm-mos"]["version"] = "https://github.com/pr1metine/pio-toolchain-llvm-mos-macos.git"
            self.packages["tool-vice"]["version"] = "https://github.com/pr1metine/pio-tool-vice-macos.git"
        return super().configure_default_packages(variables, targets)

    def configure_debug_session(self, debug_config):
        super().configure_debug_session(debug_config)