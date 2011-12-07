import os
import subprocess
from copy import copy
from django.conf import settings
from django.core.exceptions import MiddlewareNotUsed


class VersionMiddleware(object):
    def __init__(self):
        """
        Adds VERSION to the application settings with the current version.
        """
        settings.VERSION = self.get_version()
        raise MiddlewareNotUsed

    def get_version(self):
        git_binary = getattr(settings, 'GIT_BINARY_LOCATION', 'git')
        env = copy(os.environ)
        env.update({'GIT_DIR': settings.GIT_REPOSITORY_DIR})
        process = subprocess.Popen('%s rev-parse HEAD' % git_binary, env=env,
            shell=True, stdout=subprocess.PIPE)
        process.wait()
        return process.stdout.read().strip()


class XVersionMiddleware(object):
    def process_response(self, request, response):
        """
        Adds X-Version header to the HTTP response with the current version.
        """
        response['X-Version'] = settings.VERSION
        return response
