# Problem Statement

Manually calculating an electricity bill is error-prone: tariffs are not flat — they rise in
slabs as consumption increases, and separate duty and surcharge percentages are added on top.
Consumers also have no easy way to estimate how much a new appliance will add to their monthly
bill before they buy it. This project automates both problems in a single, self-contained
command-line tool.

 Scope.

 menu-driven **Electricity Bill Calculator** that:

- Records a consumer's name, consumer number, and connection type (Domestic / Commercial)
- Calculates a bill from two meter readings using a progressive (slab-based) tariff, plus a
  fixed charge, a 5% electricity duty, and a 2% surcharge
- Estimates monthly units and cost for one or more household appliances from their wattage,
  daily usage hours, and days of use per month
- Displays a formatted bill summary on demand

**Out of scope:** persistent storage between program runs, multiple consumers in a single
session, real-time tariff updates from a utility provider, and a graphical interface.

 Target Users

- Domestic and small-commercial electricity consumers who want to verify their bill by hand
- Students learning how progressive/slab-based billing systems work
- Anyone estimating the running cost of a specific appliance before buying it

 High-Level Features

- Consumer detail intake with re-prompting on invalid connection-type input
- Slab-based energy charge calculation (rates differ for Domestic vs. Commercial), with
  electricity duty and surcharge added on top of the energy charge
- Input validation throughout: non-empty consumer number, non-negative meter readings,
  current reading not less than previous, positive appliance wattage/hours/days, hours capped
  at 24/day and days capped at 31/month
- Appliance-based consumption estimator supporting multiple appliances in one run
- On-demand, formatted bill summary
