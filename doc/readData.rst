Reading Data
************

Format of data
==============

The data ought to be in .csv format. The delimeter should be a comma (,). The fields should be as followed

.. csv-table::
   :header: File type, Dosage data, Concentration Data, Time Data
   :align: center

   csv, Dose/dose/DOSE, Conc/conc/CONC/C_p, Time/time/TIME/T

In order to use the program, it has to be made sure that the data consists of the above written headings.

.. caution::
   The units of the headings must not be included the headings.

Headings
=========

#. :Dose: This is the data of dosage of drug administedted to the patient. Generally for single compartment drugs i.e. giving single dose, this remain constant through out the time of observation.
#. :Concentration: The Concentration of the drug will decrease with time due to clearence from body. If more than one doses are involved, then there will be a spike in concentration after the next doe is administered.
#. :Time: Time generally starts from 1hr after the administretion of dose. It goes on until the last dose has been cleared.

A sample data table is like followed

.. csv-table::
   :header: Dose, Conc, Time

   500, 0.794, 1
   500, 0.500, 3
   500, 0.250, 6
   500, 0.079, 11

.. caution::
   Tables, like the following, holding units of headers cannot be used.

   .. csv-table::
      :header: Dose :math:`(mg)`, Conc :math:`({\\mu}g/mL)`, Time :math:`(hr)`

      500, 0.794, 1
      500, 0.500, 3
      500, 0.250, 6
      500, 0.079, 11

Errors
======