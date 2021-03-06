#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Rancher API
# Copyright (c) 2008-2020 Hive Solutions Lda.
#
# This file is part of Hive Rancher API.
#
# Hive Rancher API is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by the Apache
# Foundation, either version 2.0 of the License, or (at your option) any
# later version.
#
# Hive Rancher API is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License for more details.
#
# You should have received a copy of the Apache License along with
# Hive Rancher API. If not, see <http://www.apache.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2020 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

class ProjectAPI(object):
    """
    The project API endpoints used by the Rancher 2.x
    infra-structure.
    """

    def list_projects(self, cluster, *args, **kwargs):
        url = self.base_url + "clusters/%s/projects" % cluster
        contents = self.get(url, **kwargs)
        data = contents["data"]
        return data

    def list_projects_name(self, cluster, name):
        url = self.base_url + "clusters/%s/projects?name=%s" % (cluster, name)
        contents = self.get(url)
        data = contents["data"]
        return data

    def get_project(self, cluster, id):
        url = self.base_url + "clusters/%s/projects/%s" % (cluster, id)
        contents = self.get(url)
        return contents

    def get_project_safe(self, cluster, id):
        contents = self.list_projects_name(cluster, id)
        if contents: return contents[0]
        return self.get_project(cluster, id)
