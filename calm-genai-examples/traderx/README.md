# TraderX Python Implementation

This folder contains the Python implementation for the architecture described in the `2024-12 traderx.json` and associated JSON files.

## Overview

The `traderx` folder provides a Python implementation of the TraderX architecture. The architecture and flows are described in the JSON files located in the `calm/samples/2024-12/traderx` folder. These JSON files define the nodes, relationships, and flows of the TraderX system.

## Contents

- `__init__.py`: Makes the `traderx` folder a Python package.
- `config.py`: Stores configuration settings for the Python implementation, including database connections and other necessary configurations.
- `database.py`: Handles database connections and operations, including functions to connect to the database and perform CRUD operations.
- `models.py`: Defines data models for the architecture, including classes for each node type (e.g., `Account`, `Trade`, `Position`).
- `services.py`: Implements business logic and services, including functions for each flow described in the JSON files (e.g., `add_update_account`, `load_positions`).
- `main.py`: Serves as the entry point for the Python implementation, including a main function to initialize the application and run the necessary services.

## Running the Python Implementation

To run the Python implementation, follow these steps:

1. Ensure you have Python 3.8 or higher installed.
2. Install the required dependencies by running:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure the necessary settings in `config.py`.
4. Run the main script:
   ```bash
   python main.py
   ```

## Architecture and Flows

The architecture and flows of the TraderX system are described in the following JSON files:

- `traderx.json`: Describes the overall architecture of the TraderX system, including nodes and relationships.
- `flows/add-update-account/add-update-account.json`: Describes the flow for adding or updating account information in the database.
- `flows/load-list-of-accounts/load-list-of-accounts.json`: Describes the flow for loading a list of accounts from the database to populate the GUI drop-down for user account selection.
- `flows/load-positions/load-positions.json`: Describes the flow for loading positions for a specific account and subscribing to updates.
- `flows/submit-trade-ticket/submit-trade-ticket.json`: Describes the flow for submitting a trade ticket and validating the trade, account, and publishing a new trade event.
- `flows/trade-processing/trade-processing-new-trade.json`: Describes the process flow for handling new trade events.
- `flows/trade-processing/trade-processing-update-trade.json`: Describes the process flow for handling update trade events.

## CALM Decorators

All the code references CALM via a decorator `CALM<thing>("description")` to provide descriptions and context for each component and function.
