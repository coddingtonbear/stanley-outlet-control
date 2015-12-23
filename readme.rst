Stanley AC Outlet Remote Controller
===================================

Use your HackRF for controlling your Stanley remotely-controlled AC outlets.

Requirements
------------

* Gnuradio
* gr-osmocom

Installation
------------

Just install directly from pip::

    pip install stanley-outlet-control


Use
---

::

    stanley-outlet-control [outlet number] [on|off]

Notes
-----

This is currently set up to use a HackRF, but if you have any experience with
Gnuradio, you should be able to easily alter this to be usable via any
SDR transmitter.

* Modulation: On-off-keyed.
* Frequency: 433.839 MHz
* Bit rate: 1872bps
* Control Signals:

  * Outlet #1

    * Off: ``1001101001101001101001101001001101101001001001101001101001001001001001001``
    * On: ``1001101001101001101001101001001101101001001001101001101001001001001101101``

  * Outlet #2

    * Off: ``1001101001101001101001101101101001001001001001101001101001001001001001001``
    * On: ``1001101001101001101001101101101001001001001001101001101001001101101001001``

  * Outlet #3

    * Off: ``1001101001101001101001101001001001001101101001101001101001001001001001001``
    * On: ``1001101001101001101001101001001001001101101001101001101101101001001001001``

