# AeroGrid

> Wind turbine telemetry analysis that flags turbines needing urgent maintenance.

AeroGrid was completed as part of the **IEUK Bright Network Virtual Internship**. It processes telemetry readings from a fleet of wind turbines, calculates per-turbine averages for temperature and vibration, and flags any turbine whose averages cross a safety threshold.

## Table of Contents

- [Overview](#overview)
- [How It Works](#how-it-works)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [Sample Output](#sample-output)
- [Dataset](#dataset)
- [Documentation](#documentation)
- [Possible Improvements](#possible-improvements)

## Overview

Wind turbines continuously report sensor data. Sustained high temperature or vibration can indicate wear or imminent failure. AeroGrid reads this telemetry, treats an **anomaly** as a deviation from what is normal or safe, and lists the turbines that need urgent maintenance.

## How It Works

`read_telemetry.py` reads `telemetry.csv` using Python's built-in `csv` module, then:

1. Accumulates the temperature and vibration readings for each turbine.
2. Calculates each turbine's **average** temperature and vibration.
3. Flags a turbine if either average exceeds its threshold.
4. Prints the unique list of turbine IDs requiring urgent maintenance.

| Metric | Unit | Flag threshold |
| --- | --- | --- |
| Average temperature | °C | above **85.0** |
| Average vibration | mm/s | above **15.0** |

A turbine that breaches both thresholds is only reported once.

## Repository Structure

```
AeroGrid/
├── README.md
└── AeroGrid-IEUK/
    ├── read_telemetry.py          # Main analysis script
    ├── telemetry.csv              # Input data (5,000 readings)
    ├── telemetry_data.xlsx        # Spreadsheet version of the data
    ├── requirements.txt           # Python dependencies
    ├── Dockerfile                 # Container image definition
    ├── compose.yaml               # Docker Compose configuration
    ├── README.Docker.md           # Docker build/deploy notes
    ├── running_script.txt         # Quick run instructions
    ├── Reflection.jpg             # Internship reflection
    ├── Engineering Report/
    │   └── AeroGrid_Engineering Report.docx
    └── System Architecture/
        ├── AeroGrid_architecture_enchanced.jpg
        ├── AeroGrid_pdf_note_enchanced.pdf
        └── AeroGrid_standard_pdf_enchanced.pdf
```

## Getting Started

### Prerequisites

- **Python 3** (the Dockerfile targets Python 3.14), or
- **Docker Desktop** if you prefer to run it in a container

The script uses only the Python standard library, so no extra packages are needed to run it locally.

### Option 1: Run locally

```bash
git clone https://github.com/rumenvasil3v/AeroGrid.git
cd AeroGrid/AeroGrid-IEUK
python read_telemetry.py
```

### Option 2: Docker Compose

```bash
cd AeroGrid/AeroGrid-IEUK
docker compose up --build
```

### Option 3: Pre-built Docker image

```bash
docker run -d -p 8080:80 rumenvasil3v/flagging-anomalies-turbines
```

Then check the container logs to see the flagged turbines.

## Sample Output

Running the script against the included dataset reports:

```
Average temp for T-04 is 90.58117647058822
Average vibration for T-07 is 20.570216962524658
Turbine ID needed for urgent maintenance: T-04
Turbine ID needed for urgent maintenance: T-07
```

The script also prints every raw CSV row as it reads it, so you will see those lines before the summary.

## Dataset

`telemetry.csv` contains **5,000 readings** from **10 turbines** (`T-01` to `T-10`), recorded roughly once a minute between 15 and 19 April 2026.

| Column | Description |
| --- | --- |
| `timestamp` | Date and time of the reading |
| `turbine_id` | Turbine identifier (e.g. `T-04`) |
| `temperature_c` | Temperature in degrees Celsius |
| `vibration_mm_s` | Vibration in millimetres per second |
| `rpm` | Rotor speed in revolutions per minute |

## Documentation

Supporting project material lives in `AeroGrid-IEUK/`:

- **Engineering Report:** `Engineering Report/AeroGrid_Engineering Report.docx`
- **System Architecture:** diagram and PDF notes in `System Architecture/`
- **Reflection:** `Reflection.jpg`

## Possible Improvements

- Use `pandas` for faster, more concise handling of large CSV files.
- Make thresholds configurable via command-line arguments or a config file.
- Remove the per-row `print` for cleaner output on large datasets.
- Add unit tests for the averaging and flagging logic.
- Flag on rolling or recent averages rather than the whole period, to catch emerging faults sooner.

## Author

**rumenvasil3v** — completed as part of the IEUK Bright Network Virtual Internship.
