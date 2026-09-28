#!/usr/bin/env python3
import sys
import json
import requests

# Read the specific single alert file path sent dynamically by Wazuh
if len(sys.argv) < 2:
    sys.exit(1)

alert_file_path = sys.argv[1]

with open(alert_file_path, 'r') as alert_file:
    alert_json = json.loads(alert_file.read())

# Extract alert metadata
alert_level = alert_json['rule']['level']
alert_description = alert_json['rule']['description']
agent_name = alert_json['agent']['name']
rule_id = alert_json['rule']['id']

# Send alert if Severity Level is 3 or higher
if alert_level >= 3:
    message = f"🚨 *SOC ALERT DETECTED* 🚨\n\n" \
              f"🖥️ *Agent Name:* {agent_name}\n" \
              f"🆔 *Rule ID:* {rule_id}\n" \
              f"📊 *Severity Level:* {alert_level}\n" \
              f"📝 *Description:* {alert_description}\n\n" \
              f"⚠️ *Action Required: Check Wazuh Dashboard!*"
              
    url = "https://telegram.org"
    payload = {"chat_id": YOUR_CHAT_ID, "text": message, "parse_mode": "Markdown"}
    
    try:
        requests.post(url, json=payload, timeout=10)
    except Exception as e:
        pass
