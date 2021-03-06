# Setup file for package quark

from setuptools import setup

setup(name="quark",
      version="0.0.1",
      install_requires=["ws4py==0.3.*"],
      py_modules=['quark_runtime', 'quark_threaded_runtime', 'quark_runtime_logging', 'quark_ws4py_fixup'],
      packages=['quark', 'quark.logging', 'quark.reflect', 'quark.behaviors', 'quark.concurrent', 'quark.test', 'quark.spi', 'quark.spi_api', 'quark.spi_api_tracing', 'quark_md'])
