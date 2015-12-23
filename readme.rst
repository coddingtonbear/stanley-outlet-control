Stanley AC Outlet Remote Controller
===================================

Use your HackRF for controlling your Stanley remotely-controlled AC outlets.

Requirements
------------

* Gnuradio
* gr-osmocom

Notes
-----

* Modulation: On-off-keyed.
* Frequency: 433.839 MHz
* Control Signals:

  * Outlet #1

    * Off: ``1001101001101001101001101001001101101001001001101001101001001001001001001``
    * On: ``1001101001101001101001101001001101101001001001101001101001001001001101101``

  * Outlet #2

    * Off: ``1001101001101001101001101101101001001001001001101001101001001101101001001`` (Unverified)
    * On: ``1001101001101001101001101101101001001001001001101001101001001101101001001`` (Unverified)

  * Outlet #3

    * Off: ``1001101001101001101001101001001001001101101001101001101001001001001001001``
    * On: ``1001101001101001101001101001001001001101101001101001101101101001001001001``
