# test_correlation.py

import correlation_engine as ce

ce.file_events = 30
ce.powershell_detected = True
ce.registry_changes = 1

ce.evaluate_threat()