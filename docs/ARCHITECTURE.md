\# BI Navigator - Architecture Document



Version: 1.0

Status: Frozen

Last Updated: June 30, 2026



\---



\# Project Vision



BI Navigator is an Agentic AI-powered Business Intelligence Assistant that enables business users to ask natural language questions and receive SQL-generated insights, visualizations, and business recommendations without writing SQL.



Example:



User:

"Show me the Top 10 products by revenue last quarter."



BI Navigator will:



1\. Understand the user's intent.

2\. Discover the required database schema.

3\. Generate SQL.

4\. Validate SQL.

5\. Execute the query.

6\. Generate business insights.

7\. Recommend visualizations.



\---



\# High-Level Architecture



&#x20;                   User

&#x20;                     │

&#x20;                     ▼

&#x20;              Streamlit UI

&#x20;                     │

&#x20;                     ▼

&#x20;             BI Navigator

&#x20;         (Application Layer)

&#x20;                     │

&#x20;     ┌───────────────┼────────────────┐

&#x20;     ▼               ▼                ▼

&#x20;Intent Agent   Schema Agent    SQL Generator

&#x20;                     │

&#x20;                     ▼

&#x20;             SQL Validator

&#x20;                     │

&#x20;                     ▼

&#x20;             Execution Agent

&#x20;                     │

&#x20;                     ▼

&#x20;              SQLite Database

&#x20;                     │

&#x20;                     ▼

&#x20;                Query Results

&#x20;                     │

&#x20;         ┌───────────┴───────────┐

&#x20;         ▼                       ▼

&#x20;  Insight Agent         Visualization Agent

&#x20;         │                       │

&#x20;         └───────────┬───────────┘

&#x20;                     ▼

&#x20;                 Streamlit UI

&#x20;                     │

&#x20;                     ▼

&#x20;                    User



\---



\# Component Responsibilities



\## Streamlit UI



Responsibilities



\- Accept natural language questions

\- Display generated SQL

\- Display query results

\- Display charts

\- Display AI-generated insights



Does NOT



\- Generate SQL

\- Execute SQL

\- Perform AI reasoning



\---



\## Intent Agent



Purpose



Understand the user's business question.



Input



Show top 10 products by revenue last quarter.



Output



{

&#x20;   "intent": "sales\_analysis",

&#x20;   "metric": "revenue",

&#x20;   "dimension": "product",

&#x20;   "time\_period": "last\_quarter",

&#x20;   "limit": 10

}



\---



\## Schema Agent



Purpose



Identify



\- Tables

\- Columns

\- Relationships

\- Primary Keys

\- Foreign Keys



Required to answer the user's question.



\---



\## SQL Generator Agent



Purpose



Convert structured intent into valid SQLite SQL.



Input



Intent + Database Schema



Output



SELECT ...



\---



\## SQL Validator Agent



Purpose



Validate generated SQL before execution.



Checks



\- SQL syntax

\- Unsupported statements

\- Dangerous statements

\- Hallucinated tables

\- Hallucinated columns



Only validated SQL proceeds to execution.



\---



\## Execution Agent



Purpose



Execute validated SQL against SQLite.



Output



Pandas DataFrame



\---



\## Insight Agent



Purpose



Generate business insights from query results.



Example



Revenue increased 18% compared to the previous quarter.



\---



\## Visualization Agent



Purpose



Recommend and generate appropriate charts.



Possible charts



\- Bar Chart

\- Line Chart

\- Pie Chart

\- Scatter Plot

\- Area Chart



\---



\# Gemini Responsibilities



Gemini is NOT the application.



Gemini is the reasoning engine used by multiple agents.



Agents using Gemini



\- Intent Agent

\- Schema Agent

\- SQL Generator

\- Insight Agent



\---



\# Folder Structure



BI-Navigator/



app/



agents/



services/



database/



prompts/



docs/



tests/



assets/



utils/



README.md



TEAM\_LOG.md



requirements.txt



\---



\# Technology Stack



Frontend



\- Streamlit



LLM



\- Google Gemini



Programming Language



\- Python



Database



\- SQLite



Data Processing



\- Pandas



Visualization



\- Plotly



Configuration



\- python-dotenv



\---



\# Security Design



API Key



Stored inside



.env



Never committed to Git.



SQL Validation



Every generated SQL statement is validated before execution.



Future Enhancement



Only read-only SQL statements will be allowed.



\---



\# Design Principles



1\. Single Responsibility Principle



Every module performs one responsibility.



2\. Separation of Concerns



UI



↓



Application



↓



Agents



↓



Services



↓



Database



3\. Reusability



Gemini communication is centralized inside



services/gemini\_service.py



4\. Modularity



Each AI Agent is independently testable.



\---



\# End-to-End Workflow



User



↓



Streamlit UI



↓



Intent Agent



↓



Schema Agent



↓



SQL Generator



↓



SQL Validator



↓



Execution Agent



↓



SQLite



↓



Insight Agent



↓



Visualization Agent



↓



Streamlit UI



↓



User



\---



\# Sprint Mapping



Sprint 1



Project Foundation



Completed



Sprint 2



Gemini Integration



Completed



Sprint 3



Intent Agent



Upcoming



Sprint 4



Schema Agent



Sprint 5



SQL Generator



Sprint 6



SQL Validator



Sprint 7



Execution Agent



Sprint 8



Insights + Visualization



Sprint 9



Deployment + Demo



\---



Architecture Status



Frozen



Version



1.0



Last Reviewed



June 30, 2026

