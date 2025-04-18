#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================================================
#
# Command definition for initializing a new ContentForge project.
#
# This module defines the `init` command for the ContentForge CLI,
# which is responsible for scaffolding a new ContentForge plugin project in a specified directory.
#
# @filename   init.py
# @path       src\contentforge\cli\commands\init.py
# @project    ContentForge
# @encoding   utf-8
#
# @product    PyCharm
# @author     Content Forge
# @email      mailto:ContentForgeTeam@outlook.com
# @time       2025/04/18 22:15
#
# @version    git
# @record     2025/04/18 22:40 <Content Forge> Create file.
#             2025/04/18 22:40 <Content Forge> Update header comment.
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

import click  # Importing the Click library for creating command line interfaces.


@click.command(name="init", help="Initialize a new ContentForge DCC project.")
@click.option("--name", "-n", default=".", help="Target directory for scaffold")
def init(name):
    """
    Scaffold a new ContentForge plugin project.

    :param name: Target directory where the new project will be created.
    """
    # TODO: Fill in your initialization logic here
    # This is where the logic for creating the project directory and initializing files would go.

    # Output initialization success message
    click.echo(f"Initialized a new ContentForge project at '{name}'")


# =============================================================================================================
# Script Execution
# =============================================================================================================
if __name__ == '__main__':
    # Execute the init command when the script is run directly
    init()
