---
finding_id: F-<%tp.date.now("YYYYMMDD")%>-<%tp.system.prompt("Sequential # (e.g., 001)")%>
severity: <%tp.system.suggester(["Critical", "High", "Medium", "Low", "Informational"], "Select Severity")%>
cvss_score: <%tp.system.prompt("CVSS Score (e.g., 9.8)")%>
cvss_vector: ""
affected_systems: <%tp.system.prompt("Affected Systems/IPs")%>
test_phase: <%tp.system.suggester(["External", "Internal", "WebApp", "Container"], "Select Test Phase")%>
status: Open
date_identified: <%tp.date.now("YYYY-MM-DD")%>
date_validated: 
remediation_priority: <%tp.system.suggester(["Immediate", "High", "Medium", "Low"], "Remediation Priority")%>
tags: [finding, <%tp.date.now("YYYY")%>]
---

# Finding: <%tp.file.title%>

## 🎯 Executive Summary
[One-paragraph description of the finding and its business impact]

---

## 📊 Risk Rating

**CVSS v3.1 Score:** `cvss_score` / 10.0
**CVSS Vector:** 
```
CVSS:3.1/AV:_/AC:_/PR:_/UI:_/S:_/C:_/I:_/A:_
```

**Severity:** `severity`
**Likelihood:** [High/Medium/Low]
**Impact:** [High/Medium/Low]

---

## 🔍 Description

### Technical Details
[Detailed technical description of the vulnerability]

### Attack Scenario
[Describe how an attacker would exploit this]

---

## 🎯 Affected Systems

| System/Component | IP/URL | Affected Version | Notes |
|------------------|--------|------------------|-------|
| <%tp.system.prompt("System Name")%> | | | |

---

## 📸 Evidence

### Screenshot 1: [Description]
![[<%tp.file.folder(true)%>/_Attachments/<%tp.file.title%>_evidence_01.png]]

### Screenshot 2: [Description]
![[<%tp.file.folder(true)%>/_Attachments/<%tp.file.title%>_evidence_02.png]]

### Proof of Concept
```bash
# Commands used to discover/validate
[paste commands here]
```

**Output:**
```text
[paste command output or response]
```

---

## 💥 Impact

### Business Impact
[Describe the business-level impact]
- Data confidentiality compromise
- Service availability disruption
- Compliance violation
- Reputational damage

### Technical Impact
[Describe the technical impact]
- Unauthorized access to systems
- Data exfiltration potential
- Privilege escalation
- Lateral movement

---

## 🛡️ Affected NIST 800-53 Controls

- **AC-3:** Access Enforcement
- **IA-2:** Identification and Authentication
- **SC-7:** Boundary Protection
- **SC-8:** Transmission Confidentiality and Integrity
- **SI-2:** Flaw Remediation
- **SI-10:** Information Input Validation

[Select and describe which controls are impacted]

---

## ✅ Remediation

### Recommended Fix
1. [Step-by-step remediation guidance]
2. 
3. 

### Code Example (If Applicable)
**Vulnerable Code:**
```language
[paste vulnerable code snippet]
```

**Secure Code:**
```language
[paste remediated code example]
```

### Validation Steps
1. [How to verify the fix]
2. 
3. 

---

## 📚 References

### Internal References
- Related Test: [[TPL_External_Pentest#EXP-02]]
- Related Finding: [[Finding_]]

### External References
- [CWE-XXX: Weakness Name](https://cwe.mitre.org/data/definitions/XXX.html)
- [OWASP: Vulnerability Name](https://owasp.org/)
- [CVE-YYYY-XXXXX](https://cve.mitre.org/)
- [Vendor Advisory]()

---

## 📝 Timeline

| Date | Event | Notes |
|------|-------|-------|
| <%tp.date.now("YYYY-MM-DD")%> | Identified | Initial discovery during testing |
|  | Validated | Confirmed exploitability |
|  | Reported | Reported to client |
|  | Remediated | Fix implemented by client |
|  | Verified | Remediation verified |

---

## 🔄 Status Updates

### <%tp.date.now("YYYY-MM-DD")%> - Initial Discovery
[Notes on discovery]

### [Date] - Update
[Status update notes]

---

## 🏷️ Metadata

**Test Phase Reference:** [[TPL_<%tp.system.suggester(["External", "Internal", "WebApp"], "Select Phase")%>_Pentest]]
**Engagement:** [[<%tp.file.folder(true).split('/')[0]%>]]
**Assessor:** Kal
