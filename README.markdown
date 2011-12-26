# django-xversion

## Basic Installation

* Add `xversion.middleware.VersionMiddleware` to your application's
  `MIDDLEWARE_CLASSES` setting.
* Add `GIT_REPOSITORY_DIR` to your application settings with the path to
  project's `.git` directory.

### To add an `X-Version` header to all HTTP responses

Requires `VersionMiddleware` (see above)

* Add `xversion.middleware.XVersionMiddleware` to your application's
  `MIDDLEWARE_CLASSES` setting.

### To add `VERSION` to your default template context

* Add `xversion.context_processors.version` to your `TEMPLATE_CONTEXT_PROCESSORS`
  setting.

## Common Issues

### I keep getting `OSError: [Errno 2] No such file or directory`

You either:

* don't have `git` installed, or
* `git` is not located on your system's `PATH`. By default (via the behavior
of `subprocess.Popen`), the `git` executable will expected to be on your
system's `PATH` environment variable. The location can be changed to the
absolute path of the `git` executable with the `GIT_BINARY_LOCATION` setting.
