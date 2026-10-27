# Incident Report INC-001: Repeated Authentication Failures

## 1. Case Information
- Case ID: INC-001
- Project: Home SOC Lab
- Date: 16 October 2026
- Analyst: Jackie Maina
- Environment: Local simulated lab
- Status: Initial investigation documented
- Severity: Low - simulated exercise; compromise not confirmed

## 2. Summary
A Python detection script identified four failed authentication
events associated with the same source IP address in a sample log.

The configured detection threshold was three failed logins per IP.
The observed count exceeded this threshold and generated an alert.

## 3. Evidence
- Log file: evidence/sample-logs/sample-auth.log
- Detection script: detection-rules/analyze_auth_logs.py
- Analysis output: investigations/auth-log-analysis.txt
- Source IP in failed events: 192.0.2.45
- Failed authentication events: 4
- Successful authentication events in the sample: 1
- Successful event source IP: 192.0.2.20

All addresses and events in this exercise are fictional training data.

## 4. Timeline
- 09:10:01 - Failed login for invalid user admin.
- 09:10:08 - Failed login for invalid user admin.
- 09:10:15 - Failed login for invalid user test.
- 09:12:30 - Successful login for analyst from a different example IP.
- 09:14:11 - Failed login for root.

## 5. Analysis
Four failed authentication events came from the same example source IP.
This pattern triggered the configured threshold-based detection rule.

The sample also contains one successful login from a different IP.
The available evidence does not link that successful login to the
failed attempts.

## 6. Findings and Limitations
- Repeated authentication failures were detected.
- The detection script behaved as configured.
- The events are simulated and do not establish a real security incident.
- No evidence confirms account compromise.
- The sample alone cannot establish the intent of the login attempts.

## 7. Recommended Investigation Steps
1. In a real authorized environment, review authentication logs around
   the alert time.
2. Check whether the same account or source appears in other events.
3. Verify whether any successful login followed the failed attempts.
4. Validate the activity with the relevant system owner.
5. Escalate according to the organization's incident response procedure
   if corroborating evidence indicates suspicious activity.

## 8. Conclusion
The lab successfully demonstrated log parsing, threshold-based detection,
alert generation, and evidence documentation.

This case remains a simulated training exercise. No real system was
investigated or remediated.
