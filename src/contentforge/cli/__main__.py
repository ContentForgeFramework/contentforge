#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================================================
#
# Entry point for the ContentForge command line interface.
#
# This script serves as the main entry point for executing the ContentForge CLI,
# which provides various functionalities for content generation and manipulation.
#
# @filename   __main__.py
# @path       src\contentforge\cli\__main__.py
# @project    ContentForge
# @encoding   utf-8
#
# @product    PyCharm
# @author     Content Forge
# @email      mailto:ContentForgeTeam@outlook.com
# @time       2025/04/18 22:06
#
# @version    git
# @record     2025/04/18 22:12 <Content Forge> Create file.
#             2025/04/18 22:12 <Content Forge> Update header comment.
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
import os  # noqa: F401
import sys  # noqa: F401

from . import main  # Importing the main module that contains the core functionality of the CLI.


# =============================================================================================================
# Script Execution
# =============================================================================================================
if __name__ == '__main__':
    # Execute the main function from the main module when this script is run directly.
    main()
