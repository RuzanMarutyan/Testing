# Test Plan

## Owner: 
Test Manager/Test Lead

## Reviewer: 
QA Team, Project Manager, Delivery Manager, Dev Leads, BA

## Approver: 
Project Manager

---

## 1. Project Overview
List all the statements important for the particular project which may affect the test process both in positive and negative ways. You may refer to this as a reusable reminder which helps to address risks and limitations properly.

**Notes:** You may list the architecture of the product, 3rd-party dependencies, etc.

---

## 2. Test Scope
Clearly define which systems/components/interfaces/test types are in scope of the document. Also, define what’s not included in the scope.

---

## 3. Test Objectives
List all the software features (functionality, performance, GUI…) which need to be tested. Define the target or the goal of the test based on the above features.

---

## 4. Test Strategy
Define the test approach. Please refer to the [Test Strategy Document](https://epam.sharepoint.com/display/GDOKB/Test+Strategy+Document).

**Notes:** This section is optional.

---

## 5. Test Criteria
- **Entry Criteria:** Defines the benchmarks for starting all tests.
- **Suspension Criteria:** Defines the benchmarks for suspending all tests.
- **Exit Criteria:** Defines the benchmarks that signify the successful completion of a test phase or project.

---

## 6. Test Deliverables
Define the artifacts that are created during the testing process, such as requirement traceability matrix, test cases, test scripts, test data, logs, test report, TA framework, etc.

---

## 7. Test Environment
#### Introduction
This section outlines the necessary hardware, software, test data, network configuration, and tools required to create a suitable environment for testing. It ensures that all components are in place to conduct effective and efficient testing.

| **Category** | **Details** | **Examples** |
|--------------|-------------|--------------|
| **Hardware Requirements** | | |
| Device Type | Specify the type of device required for testing. | Server, Client, Mobile |
| Specs | Detail the specifications needed for each device type. | CPU: Intel i7, RAM: 16GB, Storage: 500GB SSD |
| **Software Requirements** | | |
| OS | List the operating systems required for testing. | Windows 10, macOS Catalina, Ubuntu 20.04 |
| Browsers | Specify the browsers and their versions needed. | Chrome 89, Firefox 86, Safari 14 |
| Versions | Mention the specific versions of the software. | |
| Databases | List the databases and their versions required. | MySQL 8.0, PostgreSQL 13 |
| **Test Data** | | |
| Type | Describe the type of test data needed. | User accounts, Mock transactions |
| Format | Specify the format of the test data. | CSV, JSON, XML |
| Creation Method | Detail how the test data will be created. | Manual entry, Scripted generation |
| **Network Configuration** | | |
| Type | Specify the type of network setup required. | LAN, WAN, VPN |
| Bandwidth | Detail the bandwidth requirements. | 100 Mbps, 1 Gbps |
| Protocols | List the network protocols needed. | HTTP, HTTPS, FTP |
| Firewalls | Mention any firewall configurations required. | Open ports 80, 443 |
| **Testing Tools** | | |
| Tool Name | List the tools required for testing. | Selenium, JIRA, Postman |
| Purpose | Describe the purpose of each tool. | Automated testing, Issue tracking, API testing |
| Version | Specify the version of each tool. | Selenium 3.141.59, JIRA 8.13, Postman 8.0 |
| **Environment Types** | | |
| Dev | Development environment for initial testing and debugging. | |
| QA | Quality Assurance environment for thorough testing. | |
| Staging | Pre-production environment for final validation. | |
| Production | Live environment where the application is deployed. | |

This template provides a structured framework to document the test environment requirements, ensuring all necessary components are considered and detailed for successful testing.

---

## 8. Resource Plan
- **Human Resource Plan:** Role and responsibility
- **Hardware Resource Plan**

---

## 9. Schedule
Define test activities mapped on a project schedule with timelines