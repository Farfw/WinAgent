# LISA Windows agent

## Description
                                                                                                            
## Installation

## Structure

    WinAgent/
        ├── actions/        # Logic of actions: launching applications, browser, terminals, etc.
        ├── agent.py        # Main executable agent: loop, scheduler, server integration
        ├── agent.spec      # PyInstaller build configuration for creating .exe
        ├── agent_OLD.py    # The agent's old backup, can be deleted or archived
        ├── build/          # PyInstaller build directory (auto-generated)
        ├── client/         # Working with the LISA server: API requests (config, status, logs)
        ├── config/         # Local YAML configs: settings.yaml, paths.yaml, etc.
        ├── dist/           # Final exe (PyInstaller puts it here) ├── logs/ # Agent logs (agent.log)
        ├── planner/        # Scheduler (if there is an extension of the script logic)
        ├── roles/          # YAML templates for offline behavior (if the server is not used)
        ├── run-lisa.ps1    # PowerShell script for launching or testing the agent manually
        ├── utils/          # Logger and auxiliary utilities: singleton lock and setup_logger
        ├── .venv/          # Python virtual environment
        ├── .git/, .idea/   # Git and IDE configs (PyCharm)

## How to use 
