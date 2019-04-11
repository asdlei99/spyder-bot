#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2019 Spyder Contributors
#
# Licensed under the terms of the MIT License
# (See LICENSE.txt for details)
# -----------------------------------------------------------------------------
"""Spyder Bot web services."""

# Standard library imports
import os

# Webapp
# ------
# https://devcenter.heroku.com/articles/optimizing-dyno-usage#python
PORT = int(os.environ.get("PORT", 5000))
WEB_CONCURRENCY = int(os.environ.get("WEB_CONCURRENCY", 1))

# Github vars. Environment variables on web service infrastructure
# ----------------------------------------------------------------
GH_TOKEN = os.environ.get('GITHUB_ACCESS_TOKEN')
GH_WEBHOOK_SECRET = os.environ.get('GITHUB_WEBHOOK_SECRET')

# Bot configuration
# -----------------
VALID_OWNERS = ('spyder', 'goanpeca')
GITHUB_BOT = 'spyder-bot'
GITHUB_BOT_NAME = 'Spyder Service Bot'
