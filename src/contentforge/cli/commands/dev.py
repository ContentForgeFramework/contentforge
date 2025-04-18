#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================================================
#
# Development command for ContentForge CLI.
#
# This script provides a command-line interface command to run the
# ContentForge in development mode, allowing developers to test and
# debug their applications.
#
# @filename   dev.py
# @path       src\contentforge\cli\commands\dev.py
# @project    ContentForge
# @encoding   utf-8
#
# @product    PyCharm
# @author     Content Forge
# @email      mailto:ContentForgeTeam@outlook.com
# @time       2025/04/18 22:51
#
# @version    git
# @record     2025/04/18 23:01 <Content Forge> Create file.
#             2025/04/18 23:01 <Content Forge> Update header comment.
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
import os  # noqa: F401 - Standard library for operating system interfaces
import sys  # noqa: F401 - Standard library for system-specific parameters and functions

import click  # Click is a package for creating command-line interfaces


@click.command(name="dev", help="Run the development mode.")
def dev():
    """
    Run the development mode command.

    This command outputs a message indicating that the development mode
    is currently running. It can be extended to include additional
    functionality for development tasks.
    """
    # Output message to indicate that the development mode is active
    click.echo("Start running development mode...")


# =============================================================================================================
# Script Execution
# =============================================================================================================
if __name__ == '__main__':
    # Execute the development command when this script is run directly
    dev()
