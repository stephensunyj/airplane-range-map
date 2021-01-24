## Hack@Brown 2021 Project
## [Plane Range App](http://jneronha.pythonanywhere.com/rangeapp)

#### Created by Jay-Young Cho, Joshua Neronha, and Stephen Sun
##### Brown University School of Engineering
###### January 23-24, 2021

This web application is built on Python and its libraries and published using Django on PythonAnywhere as a hosting service at (jneronha.pythonanywhere.com/rangeapp) and (planerange.me).

* plane_range.py: the key Python script which contains a number of plotting frameworks and functions in addition to data cleaning and organization. This code powers the app and its functions can be used in a standalone fashion to generate the plots on the website.
* index.html: this is the HTML script powering the Django website
* views.py: this script controls the Django script and connects index.html to plane_range.py
* manage.py / settings.py / urls.py: vital but uninteresting script forming the Django backend


#### References and Source Material:
1. Airport codes and lat/long data were sourced from [J. Patokal's OpenFlights project](https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat)
2. Aircraft capacity/range information came from [DVB Bank SE's "Overview of Commercial Aircraft](https://www.dvbbank.com/~/media/Files/D/dvbbank-corp/aviation/dvb-overview-of-commercial-aircraft-2018-2019.pdf)
3. urschrei's [Circles package](https://github.com/urschrei/Circles) was instrumental for plotting true geodesic circles


