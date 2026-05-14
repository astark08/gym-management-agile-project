# Maintenance Plan – Gym Management System

## 1. Refactoring Opportunities

### 1.1 Member Management Requirements  
- **Area/Component:** SRS – Member Management section  
- **Current Issue:** Requirements for adding, updating, and viewing members are described in multiple places with overlapping wording, which makes the behavior slightly unclear and repetitive.  
- **Proposed Improvement (Refactoring):** Consolidate all member-related requirements into a single, clearly structured subsection (e.g., “3.1 Member Management”) with distinct bullets for “Add Member”, “Update Member”, and “View Member”.  
- **Why this improves quality:** Reduces ambiguity and duplication, making it easier to maintain and update requirements as the system evolves.

### 1.2 Architecture Diagram – Data Flow Clarity  
- **Area/Component:** Architecture diagram (data flow between UI, logic, and storage)  
- **Current Issue:** The diagram shows the main components but does not clearly distinguish between control flow and data flow, which can make it harder to reason about where validation and security checks should occur.  
- **Proposed Improvement (Refactoring):** Refine the diagram to explicitly label data flows (e.g., “member data”, “payment status”) and trust boundaries, and separate UI, application logic, and storage into clearly defined layers.  
- **Why this improves quality:** Improves understandability, supports better security and reliability reasoning, and makes future design changes less risky.

### 1.3 Test Cases – Coverage and Duplication  
- **Area/Component:** Test cases for member operations  
- **Current Issue:** Existing test ideas focus mainly on “happy path” scenarios (e.g., adding a valid member) and may repeat similar steps without covering edge cases such as invalid input, empty fields, or duplicate members.  
- **Proposed Improvement (Refactoring):** Add negative and boundary test cases (e.g., very long names, invalid membership types, missing required fields) and remove redundant tests that cover the same behavior.  
- **Why this improves quality:** Increases test coverage, reduces redundancy, and makes the test suite more effective at catching defects early.

---

## 2. Technical Debt Analysis

### 2.1 Lack of Authentication and Authorization  
- **Description of the debt:** The system assumes that anyone running it is an authorized staff member; there is no login or role separation.  
- **Why it is a problem:** In a real environment, this would allow any user with access to the machine to view or modify all member data.  
- **Potential impact if not addressed:** Data tampering, privacy issues, and loss of trust in the system’s integrity.  
- **Suggested resolution:** Introduce a simple authentication mechanism (e.g., staff login) and define roles (admin vs regular staff) for sensitive operations.

### 2.2 Plain-Text Data Storage  
- **Description of the debt:** Member information is conceptually stored in plain text or simple structures without encryption or access control.  
- **Why it is a problem:** Sensitive data could be exposed if files are accessed directly or copied.  
- **Potential impact if not addressed:** Data leaks, regulatory issues, and reputational damage.  
- **Suggested resolution:** Plan to migrate to a more secure storage approach (e.g., database with restricted access and optional encryption for sensitive fields).

### 2.3 Minimal Error Handling and Logging  
- **Description of the debt:** Error handling is not fully specified, and there is no clear logging strategy for failures or important events.  
- **Why it is a problem:** Failures may result in crashes or silent errors, and there is no audit trail for investigating issues.  
- **Potential impact if not addressed:** Reduced reliability, difficulty diagnosing problems, and inability to trace changes or suspicious activity.  
- **Suggested resolution:** Define a basic error-handling and logging approach (e.g., log file for key operations and errors, user-friendly error messages).

---

## 3. Versioning Strategy

- **Version format:** `vMAJOR.MINOR.PATCH` (e.g., `v1.0.0`)  

### Major Version Updates  
- Triggered by:  
  - Breaking changes to core functionality  
  - Significant architectural changes (e.g., moving from file-based storage to a database)  
  - Major new features that change how users interact with the system  
- Example: Moving from a simple console-only system to a client–server architecture → `v2.0.0`.

### Minor Version Updates  
- Triggered by:  
  - New features that are backward compatible (e.g., adding a new report or search feature)  
  - Improvements to usability or performance that do not break existing behavior  
- Example: Adding advanced member search or filtering → `v1.1.0`.

### Patch (Small Revisions)  
- Triggered by:  
  - Bug fixes  
  - Small documentation updates  
  - Minor refactoring that does not change behavior  
- Example: Fixing a typo in a menu option or correcting a small logic bug → `v1.0.1`.

**Current version of the project:** `v1.0.0` (initial complete design and documentation).

---

## 4. Dependency and Change Planning

### Current Dependencies and Assumptions  
Even though the project is conceptual, the system implicitly depends on:  
- **User input via console:** Assumes users provide valid, well-formed data.  
- **Local file system or storage:** Assumes the environment can store and retrieve member data.  
- **Execution environment:** Assumes a Python runtime (or similar) is available and stable.  
- **Organizational processes:** Assumes staff follow procedures for using the system correctly.

### Impact of Dependency Changes  
- **Change in input method (e.g., moving from console to web UI):**  
  - The UI layer would need to be redesigned, but core logic could be reused if properly separated.  
- **Change in storage (e.g., moving from files to a database):**  
  - Data access logic would need to be refactored; schema design and migration would be required.  
- **Change in environment (e.g., deployment to cloud or shared server):**  
  - Security, authentication, and access control would become more critical; logging and monitoring would need to be more robust.

### Adaptation Strategy  
- Keep a clear separation between UI, business logic, and data storage in the design so each layer can evolve independently.  
- Document assumptions about dependencies so future changes can be planned rather than discovered accidentally.  
- Plan incremental changes (e.g., first introduce a data access layer, then swap storage implementation).

---

## 5. Evolution Reflection

Since Week 1, the system has evolved from a vague idea of a “gym app” into a more structured and well-documented design with clear requirements, architecture, test strategy, and security considerations. The documentation now includes CI/CD thinking, deployment planning, and threat modeling, which makes the system feel more like a real, maintainable product rather than just a one-off assignment.

If this were a real system, my next priority would be to strengthen the separation of concerns in the design (clear layers for UI, logic, and storage) and to formalize authentication and data protection requirements. This would make it easier to evolve the system into a web or mobile application later without rewriting everything. Ongoing maintenance is critical in software engineering because systems rarely stay static—requirements change, threats evolve, and technical debt accumulates over time. Regularly revisiting design, refactoring, and addressing technical debt ensures that the system remains reliable, secure, and adaptable instead of becoming brittle and expensive to change.
