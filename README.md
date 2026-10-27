# Home SOC Lab

## Overview
A hands-on cybersecurity portfolio project focused on security monitoring,
authentication log analysis, basic detection engineering, and investigation
documentation using a local Kali Linux environment.

## Project Goals
- Analyse authentication events from sample logs.
- Detect repeated failed logins using a configurable threshold.
- Record investigation findings and test results.
- Build a foundation for future SIEM monitoring with Wazuh.

## Current Lab Components
- Kali Linux running in VirtualBox.
- Docker installed and verified with the hello-world container.
- Initial local network scan and network baseline evidence.
- Python authentication log analysis script.
- Fictional authentication log samples.
- Incident investigation report.
- Automated Python unit tests.

## Detection Logic
The current Python script counts failed authentication events by source IP.
It triggers an alert when an IP has three or more failed logins in the
input log.

The threshold is a lab setting for demonstration, not a universal
security standard.

## Run the Detection Script

From the project directory:

    python3 detection-rules/analyze_auth_logs.py

To analyse the lower-volume sample:

    python3 detection-rules/analyze_auth_logs.py evidence/sample-logs/sample-auth-low-volume.log

## Run Automated Tests

    python3 -m unittest discover -s tests -v

The current test suite contains three tests covering alert triggering,
non-triggering at a lower event count, and successful-login counting.
All three passed in the recorded run.

## Evidence and Documentation
- `evidence/`: baseline records and sample authentication logs.
- `detection-rules/`: Python detection script.
- `investigations/`: analysis outputs and automated test results.
- `incident-reports/`: investigation report.
- `tests/`: automated unit tests.
- `documentation/`: lab environment and Wazuh requirements assessment.

## Limitations
The authentication events are fictional training data. The current script
is a basic demonstration, not a production-grade detection engine.
It does not establish that an actual compromise occurred.

## Planned Work
- Improve detection logic and validation.
- Add a suitable SIEM deployment, with Wazuh still under evaluation
  because of the laptop's memory constraints.
- Add further monitoring and investigation exercises.
- Document architecture, setup, and evidence as the project grows.

## Safety
Only use authorised systems and data. Do not test against university or
other third-party systems without explicit permission.
