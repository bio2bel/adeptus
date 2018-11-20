Bio2BEL ADEPTUS |build|
=======================
Converts ADEPTUS disease-differential gene expression signatures to BEL.

Big thanks to Daniel Himmelstein for preprocessing this data in his repository at:
https://github.com/dhimmel/adeptus

Installation |pypi_version| |python_versions| |pypi_license|
------------------------------------------------------------
``bio2bel_adeptus`` can be installed easily from
`PyPI <https://pypi.python.org/pypi/bio2bel_adeptus>`_
with the following code in your favorite terminal:

.. code-block:: sh

    $ python3 -m pip install bio2bel_adeptus

or from the latest code on `GitHub <https://github.com/bio2bel/adeptus>`_ with:

.. code-block:: sh

    $ python3 -m pip install git+https://github.com/bio2bel/adeptus.git

Setup
-----
This repository does not currently cache the data, but only wraps conversion to BEL.

Python REPL
~~~~~~~~~~~
.. code-block:: python

    >>> import bio2bel_adeptus
    >>> adeptus_manager = bio2bel_adeptus.Manager()
    >>> graph = adeptus_manager.to_bel()



.. |build| image:: https://travis-ci.com/bio2bel/adeptus.svg?branch=master
    :target: https://travis-ci.com/bio2bel/adeptus
    :alt: Build Status

.. |documentation| image:: http://readthedocs.org/projects/bio2bel-adeptus/badge/?version=latest
    :target: http://bio2bel.readthedocs.io/projects/adeptus/en/latest/?badge=latest
    :alt: Documentation Status

.. |pypi_version| image:: https://img.shields.io/pypi/v/bio2bel_adeptus.svg
    :alt: Current version on PyPI

.. |coverage| image:: https://codecov.io/gh/bio2bel/adeptus/coverage.svg?branch=master
    :target: https://codecov.io/gh/bio2bel/adeptus?branch=master
    :alt: Coverage Status

.. |python_versions| image:: https://img.shields.io/pypi/pyversions/bio2bel_adeptus.svg
    :alt: Stable Supported Python Versions

.. |pypi_license| image:: https://img.shields.io/pypi/l/bio2bel_adeptus.svg
    :alt: MIT License
