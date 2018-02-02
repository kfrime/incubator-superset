#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from superset import app
# cmd: superset runserver -d -p 8085
app.run(debug=True, host='0.0.0.0', port=8088)
