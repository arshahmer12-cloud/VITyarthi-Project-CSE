# Electricity Bill Calculator

A program that calculates an electricity bil using a progressive (slab-based) tariff, and estimates monthly consumption from a list ofhousehold appliances.

## Overview

Enter a consumer's details once, then calculate their bill from two meter readings — the
program applies the correct slab-based tariff for their connection type (Domestic or
Commercial), adds electricity duty and surcharge, and can also estimate what a set of
appliances would add to the monthly bill before a single unit is consumed.

## Features

- **Consumer Details** — name, consumer number, and connection type (Domestic / Commercial),
  with re-prompting on invalid input
- **Bill Calculation** — progressive slab-based energy charge + fixed charge + 5% electricity
  duty + 2% surcharge
- **Appliance Consumption Estimator** — estimate monthly units (and by extension, cost) from
  wattage, hours/day, and days/month for one or more appliances
- **Bill Summary** — a clean, formatted summary of the last calculated bill
- Input validation throughout (non-empty fields, non-negative/ordered meter readings,
  positive appliance values with sensible upper bounds)

## Technologies Used

- Python 3.8+ (no third-party packages — standard library only: `input()`/`print()` and
  built-in numeric types)

## Project Structure

electricity-bill-calculator/
├── README.md
├── statement.md
├── bill_calculator.py         # the entire program

## Environment Setup

1. Install Python 3.8 or later if you don't already have it:
   - Windows/Mac: download from [python.org/downloads](https://www.python.org/downloads/)
   - Linux: `sudo apt install python3` (Debian/Ubuntu) or your distro's equivalent
2. Verify the install:

   python3 --version

   (On Windows, this may just be `python --version`.)

No virtual environment or `pip install` is required — the program uses only Python's
standard library.

## Steps to Install & Run

1. Clone the repository:

   git clone.
   cd electricity-bill-calculator

2. Run the program.

   python3 bill_calculator.py

3. Use the on-screen menu (1–5) to enter consumer details, calculate a bill, estimate
   appliance consumption, view the bill summary, or exit.

## Instructions for Testing

This program is tested manually against a set of representative scenarios (no automated
test framework is used). To verify it yourself, run the steps below in order and confirm
the output matches:

| # | Scenario | Steps | Expected Result |

| 1 | Domestic bill, mid-range usage | Option 1 → any name/number → connection `1` (Domestic); Option 2 → previous `100`, current `250` | Units = 150.0; Energy Charge = ₹525.00; Total Bill = ₹661.75 |
| 2 | Commercial bill, top slab | Option 1 → connection `2` (Commercial); Option 2 → previous `0`, current `500` | Units = 500.0; Energy Charge = ₹3,550.00 (verify against the slab table in `design/requirements.md`) |
| 3 | Invalid meter reading | Option 2 → previous `300`, current `250` | Program prints an error and re-prompts instead of accepting the reading |
| 4 | Appliance estimator | Option 3 → `1` appliance → name, `75` watts, `8` hours/day, `30` days | Estimated consumption = 18.00 units/month |
| 5 | Guard before details exist | Restart the program → Option 2 or Option 4 immediately | Program asks you to enter consumer details first, without crashing |
