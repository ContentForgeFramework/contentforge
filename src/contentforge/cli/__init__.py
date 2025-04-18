#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================================================
#
# Initialization module for the ContentForge command line interface.
#
# This module initializes the ContentForge CLI by importing necessary components,
# registering subcommands, and allowing the CLI to be executed as a standalone script.
#
# @filename   __init__.py
# @path       src\contentforge\cli\__init__.py
# @project    ContentForge
# @encoding   utf-8
#
# @product    PyCharm
# @author     Content Forge
# @email      mailto:ContentForgeTeam@outlook.com
# @time       2025/04/18 22:19
#
# @version    git
# @record     2025/04/18 22:31 <Content Forge> Create file.
#             2025/04/18 22:31 <Content Forge> Update header comment.
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
#             For permissions, please contact EMAIL.
# =============================================================================================================
from __future__ import print_function, unicode_literals

# =============================================================================================================
# Standard Python Imports
# =============================================================================================================
import os  # noqa: F401 - Operating system interfaces (imported but not used here)
import sys  # noqa: F401 - System-specific parameters and functions (imported but not used here)

# Importing the already re-exported click.Command instances from the commands package
from .commands import init, make

# Relative import of the main CLI group
from .main import main


# Registering subcommands to the main CLI group
main.add_command(init)  # Adds the init command to the CLI
main.add_command(make)  # Adds the make command to the CLI

# =============================================================================================================
# Script Execution
# =============================================================================================================
# This block enables the CLI to be run as a standalone script.
if __name__ == '__main__':
    # Invoke the main CLI group to process commands when this script is executed directly.
    main()
