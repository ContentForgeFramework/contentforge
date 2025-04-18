#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================================================
#
# Main module for the ContentForge command line interface.
#
# This module defines the entry point for the ContentForge CLI,
# including command groups and subcommands that facilitate content generation and management.
#
# @filename   main.py
# @path       src\contentforge\cli\main.py
# @project    ContentForge
# @encoding   utf-8
#
# @product    PyCharm
# @author     Content Forge
# @email      mailto:ContentForgeTeam@outlook.com
# @time       2025/04/18 22:13
#
# @version    git
# @record     2025/04/18 22:26 <Content Forge> Create file.
#             2025/04/18 22:26 <Content Forge> Update header comment.
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
import os  # noqa: F401
import sys  # noqa: F401

import click  # Importing the Click library for creating command line interfaces.


@click.group()
def main():
    """
    ContentForge Artisan CLI entry point.

    This command group serves as a container for all subcommands of the ContentForge CLI.
    It does not execute any business logic on its own.
    """
    # This is only for grouping, no business logic is executed here
    pass


# =============================================================================================================
# Script Execution
# =============================================================================================================
if __name__ == '__main__':
    # Execute the main command group when the script is run directly
    main()
