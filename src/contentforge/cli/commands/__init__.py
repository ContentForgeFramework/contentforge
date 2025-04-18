#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================================================
#
# Short description for file: Command module initialization for the ContentForge CLI.
#
# Long description for file: This module initializes the command sub-package for the ContentForge CLI by
# importing the available command functions and defining the public API for the commands.
#
# @filename   __init__.py
# @path       src\contentforge\cli\commands\__init__.py
# @project    ContentForge
# @encoding   utf-8
#
# @product    PyCharm
# @author     Content Forge
# @email      mailto:ContentForgeTeam@outlook.com
# @time       2025/04/18 22:33
#
# @version    git
# @record     2025/04/18 22:34 <Content Forge> Create file.
#             2025/04/18 22:34 <Content Forge> Update header comment.
#             CURRENT_USER_NAME description
#
# @license    https://www.apache.org/licenses/LICENSE-2.0 Apache-2.0 License
#
# @copyright  Copyright (c) 2025. All rights reserved.
#
#             This software, including its code, documentation, and related materials,
#             is protected by copyright law and international treaties.
#             Unauthorized use, reproduction, or distribution of any part of this software is prohibited.
#
#             ContentForge is a trademark of ContentForge.org.
#             All other trademarks and registered trademarks are the property of their respective owners.
#
#             For permissions, please contact mailto:ContentForgeTeam@outlook.com.
# =============================================================================================================
from __future__ import print_function, unicode_literals

# =============================================================================================================
# Standard Python Imports
# =============================================================================================================
import os  # noqa: F401 - Operating system interfaces (imported but not used here)
import sys  # noqa: F401 - System-specific parameters and functions (imported but not used here)

from .build import build as build  # Importing the build command
from .dev import dev as dev  # Importing the dev command
from .docs import docs as docs  # Importing the docs command

# Importing command functions from the submodules
from .init import init as init  # Importing the init command
from .make import make as make  # Importing the make command
from .test import test as test  # Importing the test command


# Defining the public API for this module
__all__ = ["init", "make", "build", "dev", "test", "docs"]

# =============================================================================================================
# Script Execution
# =============================================================================================================
if __name__ == '__main__':
    # This block allows the module to be executed as a standalone script,
    # although currently there is no executable functionality defined.
    pass
