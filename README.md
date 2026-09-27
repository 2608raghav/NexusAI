Built a distributed multi-agent AI platform implementing A2A-style orchestration and MCP-based tool integration. Developed specialized AI agents for financial analysis, news aggregation, report generation, and email automation using FastAPI, HTTPX, Docker, PostgreSQL, and Gemini.


NexusAI — Multi-Agent Intelligence Platform
Tagline

An enterprise-grade multi-agent AI platform that orchestrates specialized AI agents using A2A communication and MCP for standardized tool integration.



                                User
                                  │
                                  ▼
                      ┌──────────────────────┐
                      │  API Gateway         │
                      └──────────┬───────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │  Orchestrator Agent     │
                    └──────────┬──────────────┘
                               │
         ┌────────────┬─────────┼───────────┬────────────┐
         ▼            ▼         ▼           ▼            ▼
   News Agent   Finance Agent Weather Agent PDF Agent Email Agent
         │            │         │           │            │
         └────────────┴─────────┴───────────┴────────────┘
                               │
                               ▼
                    ┌─────────────────────────┐
                    │      MCP Server         │
                    └──────────┬──────────────┘
                               │
        ┌──────────┬───────────┬────────────┬────────────┐
        ▼          ▼           ▼            ▼
   Search API  Weather API  Calculator  File System




🌍 Real-World Scenario

Imagine your manager says:

"Analyze Microsoft's stock, summarize today's news, generate a PDF report, and email it to me."

You won't write one giant function.

Instead:

User Request
      │
      ▼
Orchestrator Agent
      │
      ├────────► Finance Agent
      │             │
      │             ▼
      │      Alpha Vantage API
      │
      ├────────► News Agent
      │             │
      │             ▼
      │         NewsAPI
      │
      ├────────► Report Agent
      │             │
      │             ▼
      │       Generate PDF
      │
      └────────► Email Agent
                    │
                    ▼
               Gmail API



# NexusAI

## Multi-Agent Intelligence Platform

NexusAI is an enterprise-grade Agentic AI platform that orchestrates specialized AI agents using Agent-to-Agent (A2A) communication and Model Context Protocol (MCP).

### Features

- Multi-Agent Architecture
- MCP Tool Integration
- A2A Communication
- FastAPI
- Async Python
- Docker
- Gemini Integration
- PostgreSQL
- Redis

Project is under active development.


### Commands for running the agents
 - python -m uvicorn apps.AGENT_NAME.app:app --reload --port PORT_NUMBER
 - eg: python -m uvicorn apps.weather_agent.app:app --reload --port 8002
 - eg: python -m uvicorn apps.orchestrator_agent.app:app --reload --port 8000
 - eg: python -m uvicorn apps.news_agent.app:app --reload --port 8001
### To see the output 
 - http://127.0.0.1:PORT_NUMBER/docs
 - http://127.0.0.1:8000/docs