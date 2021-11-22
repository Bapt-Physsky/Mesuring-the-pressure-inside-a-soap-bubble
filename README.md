# Mesuring-the-pressure-inside-a-soap-bubble
This is about my experimental project that I did in third year of my Licence de Physique (Physics degree) at Université de Bretagne Occidentale.

Me and my pair, with our referent professor, tried to mesure the pressure inside a soap bubble with a MEMS pressure sensor, but after some experiment, we came back on the indirect method due to the high sensibility of the MEMS sensor and the high nose of the wintery weather.

#################################################

Subject abstract (in french, english translation below) :

Le but de l'expérience est de mesurer la pression dans une bulle de savon en fonction de son rayon. Théoriquement, la différence de pression entre l'intérieur et l'extérieur d'une bulle d'un rayon 10 mm est de seulement 10^-4 atm (10 Pa). C'est la limite de la précision d'un manomètre à l'eau. Par contre, les capteurs basés sur la technologie MEMS (microsystèmes électromécaniques), qui se trouvent par exemple dans les smartphones, peuvent avoir une meilleure sensibilité. Quel est leur principe de fonctionnement ? Est-il possible de l'utiliser pour ce projet ?

The goal of this experiment is to mesure the pressure inside a soap bubble according to its radius. Theorically, the pressure difference between inside and outside a bubble with a radius of 10mm is about 10^-4 atm (10 Pascal). It's the limit of precision for a water pressure gauge. However, MEMS-tech based sensors, who can be found in smartphone, can have a better sensibility. How their work ? Is it possible to use them in this project ?

#################################################

How we worked ?

We started by using a "direct" measuring method, by using a home-made wareglass (-image to include- ; protocol not finished) :

1. We put the MEMS sensor inside the jame jar ;
2. We plunge the mountpiece in the soap solution ;
3. We hit the record button (the camera has to record the bubble in a way that it is possible to measure is diameter later) ;
4. To inflated the bubble, the operator (one of us) injected air in the system with the syringe ;
5. When the bubble is fully inflated, the operator remove the syringe and immediatly, with his finger, clamp the nozzle to prevent air escaping (and thus, the bubble deflecting) ;
6. The operator release a very little bit his finger, deflating the bubble as slow as possible

But, after a few try and run of the previous protocol, we find out that the MEMS sensor is too sensible for this experiment. Because, even inside the closed jar, is was still able to catch the atmospheric variation, who turn out to be a lot in the breton wintery weather (thanks the "giboulées de Mars" - March's sleet). So, my pair buy another MEMS sensor (the same as the one we already use), to counter-act the atmospheric pressure variation.

#################################################

The MEMS sensor we use : Texas Instrument CC2650 SENSORTAG

The pressure sensor use : BMP280

Data acquisition made with phyphox app on Android by Bluetooth

#################################################

The literature on which we relied :

C.V. Boys, "Bulles de savon, quatre conférences sur la capillarité", Paris 1892 ;

F. L. Román, J. Faro and S. Velasco, Am. J. Phys., vol. 69, p.917 (2001) ;

P. Marmottant, S. Hilgenfeldt, Nature, vol. 432, p.153 (2003) ;

T. Lopez-Arias, L.M. Gratton, S. Oss, Eur. J. Phys. vol. 29, p.1235 (2008) ;

B. Néel, E. Villermaux, J. Fluid Mech., vol. 838, p.192 (2018) ;

M. Specht and al., Am. J. Phys., vol. 87, p.1014 (2019)

#################################################

The scheme of the scale measuring method is the "chemix_numbered.png" file, and here is the legend :

1. Soap bubble

2. Bell

3. Syringe

4. Petri dish with water

5. Scale

6. Support

#################################################

The python programme is in french, but, you can ask for a english version !

How it's work ? Well, this python code is for making plot based on the .txt file. The first plot are about the pressure differential evolution during the deflating of the bubble and the second one illustrate the surface tension.

#################################################

Log : (day-month-year)

2-10-2021 : Read me complété ; ajout code python ; ajout schéma expérience ;

3-10-2021 : Read me ajourné ;

4-10-2021 : Correction Read me ;

22-11-2021 : Correction Read me ;


