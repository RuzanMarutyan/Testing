# Test Plan

## Owner: 
Test Manager/Test Lead

## Reviewer: 
QA Team, Project Manager, Delivery Manager, Dev Leads, BA

## Approver: 
Project Manager

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Test Scope](#test-scope)
3. [Test Objectives](#test-objectives)
4. [Test Strategy](#test-strategy)
5. [Test Criteria](#test-criteria)
6. [Test Deliverables](#test-deliverables)
7. [Test Environment](#test-environment)
8. [Resource Plan](#resource-plan)
9. [Schedule](#schedule)
10. [Communication](#communication)
11. [Risks Management](#risks-management)
12. [Approvals](#approvals)

---

## 1. Project Overview
List all the statements important for the particular project which may affect the test process both in positive and negative ways. You may refer to this as a reusable reminder which helps to address risks and limitations properly.

**Notes:** You may list the architecture of the product, 3rd-party dependencies, etc.

## 2. Test Scope
Clearly define which systems/components/interfaces/test types are in scope of the document. Also, define what’s not included in the scope.

## 3. Test Objectives
List all the software features (functionality, performance, GUI…) which may need to be tested. Define the target or the goal of the test based on the above features.

## 4. Test Strategy
Define the test approach. Please refer to the [Test Strategy Document](https://epam.sharepoint.com/:w:/r/sites/policy/_layouts/15/Doc.aspx?sourcedoc=%7BF1B252D8-0840-40B8-BA18-008217B1EA4E%7D&file=PID_TestPlan.dotx&action=default&mobileredirect=true).

**Optional**

## 5. Test Criteria
- **Entry Criteria:** Defines the benchmarks for starting all tests.
- **Suspension Criteria:** Defines the benchmarks for suspending all tests.
- **Exit Criteria:** Defines the benchmarks that signify the successful completion of a test phase or project.

## 6. Test Deliverables
Define the artifacts that are created during the testing process, such as requirement traceability matrix, test cases, test scripts, test data, logs, test report, TA framework, etc.

- Test Plan Document
- Test Cases and Test Scripts
- Test Execution Reports
- Defect Reports
- Test Metrics
- Test Closure Report

## 7. Test Environment

#### Introduction
This section outlines the necessary components and configurations required to create a suitable environment for testing. It includes hardware and software requirements, test data, network configurations, testing tools, and different environment types. This template ensures that all aspects of the test environment are documented and can be easily adapted for various projects.

#### Hardware Requirements

| Device Type | Specifications (CPU, RAM, Storage) | Examples |
|-------------|------------------------------------|----------|
| Server      | CPU: Intel Xeon, RAM: 32GB, Storage: 1TB SSD | Web server, Database server |
| Client      | CPU: Intel i5, RAM: 8GB, Storage: 256GB SSD | Desktop, Laptop |
| Mobile      | CPU: Octa-core, RAM: 4GB, Storage: 64GB | Android, iOS devices |

#### Software Requirements

| Software Type | OS/Browser/Database | Version | Examples |
|---------------|---------------------|---------|----------|
| Operating System | Windows, Linux, macOS | Windows 10, Ubuntu 20.04, macOS Big Sur | Windows 10, Ubuntu 20.04 |
| Browser | Chrome, Firefox, Safari | Chrome 91, Firefox 89, Safari 14 | Chrome 91, Firefox 89 |
| Database | MySQL, PostgreSQL, MongoDB | MySQL 8.0, PostgreSQL 13, MongoDB 4.4 | MySQL 8.0, PostgreSQL 13 |

#### Test Data

| Data Type | Format | Creation Method | Examples |
|-----------|--------|-----------------|----------|
| User Accounts | JSON, CSV | Manually created, Scripted | Test users with different roles |
| Mock Transactions | JSON, XML | Generated via scripts | Sample financial transactions |
| Product Listings | CSV, Excel | Imported from existing data | Sample product catalog |

#### Network Configuration

| Network Type | Bandwidth | Protocols | Firewalls | Examples |
|--------------|-----------|-----------|-----------|----------|
| VPN          | 100 Mbps  | TCP/IP, HTTP/HTTPS | Configured for testing | Secure VPN connection |
| Local Network| 1 Gbps    | TCP/IP, HTTP/HTTPS | Standard firewall settings | Office network setup |
| Cloud Network| Variable  | TCP/IP, HTTP/HTTPS | Cloud-based firewall | AWS, Azure configurations |

#### Testing Tools

| Tool Name | Purpose | Version | Examples |
|-----------|---------|---------|----------|
| Selenium  | Automated testing | 3.141.59 | Browser automation |
| JIRA      | Issue tracking | 8.13.0 | Bug tracking and project management |
| Postman   | API testing | 8.0.7 | API development and testing |

#### Environment Types

| Environment Type | Description |
|------------------|-------------|
| Development (Dev) | Used for initial development and unit testing. |
| Quality Assurance (QA) | Used for functional, integration, and system testing. |
| Staging | Pre-production environment for final testing before release. |
| Production | Live environment where the application is available to end-users. |

## 8. Resource Plan
- **Human Resource Plan:** Role and responsibility
- **Hardware Resource Plan**

## 9. Schedule
Define test activities mapped on a project schedule with timelines and deadlines. Any specific dates should be put here if they exist.

| Activity | Start Date | End Date |
|----------|------------|----------|
| Test Plan Preparation | Jan 10, 2025 | Jan 15, 2025 |
| Test Case Development | Jan 16, 2025 | Jan 20, 2025 |
| Test Environment Setup | Jan 18, 2025 | Jan 19, 2025 |
| Test Execution | Jan 21, 2025 | Feb 05, 2025 |
| Defect Retesting & Closure | Feb 06, 2025 | Feb 10, 2025 |
| Test Closure Report | Feb 11, 2025 | Feb 12, 2025 |

## 10. Communication
Define stakeholders; communication plan, escalation plan.

## 11. Risks Management

#### 1. Purpose of Risk Management
Risk management in software testing is crucial for identifying potential issues that could impact the quality, timeline, and success of the testing process. Effective risk management helps in proactively addressing these issues, ensuring that the testing process is robust and reliable, and that the final product meets the required standards and expectations.

#### 2. Risk Identification
The first step in risk management is to identify and categorize potential risks. Use the following template to document identified risks:

| Risk ID | Description of Risk | Potential Impact | Likelihood | Category of Risk |
|---------|---------------------|------------------|------------|------------------|
| R1      | Delayed environment setup | High | High | Technical |
| R2      | Unavailability of key resources | Medium | Medium | Resource |
| R3      | Change in requirements during testing | High | High | Schedule |

**Descriptions:**
- **Risk ID:** A unique identifier for the risk.
- **Description of Risk:** A brief description of the risk.
- **Potential Impact:** The potential consequences if the risk materializes.
- **Likelihood:** The probability of the risk occurring (e.g., low, medium, high).
- **Category of Risk:** The type of risk (e.g., technical, schedule, resource).

#### 3. Risk Assessment
Once risks are identified, they need to be assessed based on their impact and likelihood. This assessment helps in determining the severity of each risk and prioritizing them accordingly.

**Risk Assessment Process:**
1. **Evaluate Impact:** Determine the potential consequences of the risk on the project.
2. **Evaluate Likelihood:** Assess the probability of the risk occurring.
3. **Determine Severity:** Combine the impact and likelihood to assess the overall severity of the risk.
4. **Prioritize Risks:** Rank the risks based on their severity to focus on the most critical ones first.

#### 4. Risk Mitigation Strategies
For each identified risk, outline a mitigation plan using the following template:

| Risk ID | Mitigation Strategy | Responsible Party | Timeline for Mitigation | Contingency Plan |
|---------|---------------------|-------------------|-------------------------|------------------|
| R1      | Pre-configure environments before testing | DevOps Team | Before Jan 18, 2025 | Use backup environments |
| R2      | Allocate backup team members | Project Manager | Ongoing | Hire temporary resources |
| R3      | Use Agile methodology for quick updates | QA Lead | Ongoing | Prioritize critical changes |

#### 5. Risk Monitoring and Review
Risks need to be continuously monitored throughout the testing process. Regular reviews of the risk register should be conducted to ensure that new risks are identified and existing risks are managed effectively.

**Monitoring and Review Process:**
1. **Regular Updates:** Update the risk register with any new risks or changes to existing risks.
2. **Review Meetings:** Conduct regular meetings to review the status of identified risks and the effectiveness of mitigation strategies.
3. **Adjust Plans:** Adjust mitigation strategies and contingency plans as necessary based on the review outcomes.

#### 6. Reporting
Risk status and updates should be reported as part of the testing effort to keep all stakeholders informed. This can be done through regular status reports, meetings, and documentation updates.

**Reporting Guidelines:**
1. **Status Reports:** Include a section on risk management in regular status reports, highlighting key risks, mitigation actions, and any changes.
2. **Stakeholder Communication:** Ensure that all relevant stakeholders are informed about the risk status and any significant changes.
3. **Documentation:** Maintain up-to-date documentation of the risk register and mitigation plans.

## 12. Approvals
List the persons who will be responsible for reviewing and approving the test plan, including their names, roles, and contact information.

| Name | Role | Signature | Date |
|------|------|-----------|------|
| Project Manager | Approver | | Jan 15, 2025 |
| QA Lead | Reviewer | | Jan 15, 2025 |