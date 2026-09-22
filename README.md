# Lean Manufacturing Calculator 📊

A simple Python tool for analyzing manufacturing and business processes using Lean principles.

## About the Project

Lean Manufacturing calculations are often performed manually or in spreadsheets.

This project provides a simple tool that automatically calculates important Lean process metrics and identifies potential bottlenecks.

## Features

The calculator can calculate:

- Takt Time
- Total Process Time
- Total Waiting Time
- Lead Time
- Process Cycle Efficiency (PCE)
- Process Bottleneck

## How It Works

The user enters:

1. Available production time
2. Customer demand
3. Number of process steps
4. Process time for each step
5. Waiting time for each step

The system then automatically analyzes the process.

## Example

Available Time: 480 minutes

Customer Demand: 120 units

Takt Time:

480 / 120 = 4 minutes per unit

If one process step takes 6 minutes, the system identifies this step as a potential bottleneck because its processing time exceeds the required Takt Time.

## Technologies

- Python
- Lean Manufacturing
- Business Process Analysis

## Future Improvements

Future versions could include:

- Quality Rate
- Rolled Throughput Yield (RTY)
- Value Stream Mapping
- Waste identification
- AI-generated process improvement recommendations
- Web interface

## Author

Nuraily
