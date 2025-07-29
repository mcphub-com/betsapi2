markdown
# BetsAPI2 MCP Server

Welcome to the BetsAPI2 MCP (Message Control Protocol) Server! This server is designed to provide comprehensive data and insights related to bet365 events, including scores, stats, and odds. Whether you are looking for in-play or pre-match data, BetsAPI2 has you covered with real-time updates and reliable information to support your betting and sports analysis needs.

## Overview

BetsAPI2 offers a robust platform for accessing a wide range of data related to sports betting. With a focus on bet365 events, users can explore current scores, detailed statistics, and various betting odds. The server supports both in-play and pre-match data, making it a versatile tool for sports enthusiasts and analysts alike.

### Key Features

- **Real-Time In-Play Data**: Access live data on ongoing events, including scores, stats, and market information.
- **Upcoming Events**: Get information on future fixtures and events to plan your betting strategy.
- **Pre-Match Odds**: Retrieve odds for upcoming events to help make informed betting decisions.
- **Event Results**: View results of completed events to analyze performance and outcomes.

## Tool List

BetsAPI2 MCP Server provides several tools to interact with the data:

1. **Bet365 Inplay Filter**: Filter in-play events based on various criteria such as sport ID and league ID.
2. **Bet365 InPlay**: Access detailed in-play data for current events.
3. **Bet365 InPlay Event**: Retrieve comprehensive information on a specific in-play event, including scores, stats, and market details.
4. **Bet365 Upcoming Events**: Get a list of upcoming events and fixtures.
5. **Bet365 PreMatch Odds**: Access pre-match odds for various events.
6. **Bet365 Result**: View results of past events to evaluate outcomes and performance.

## Tool Details

### Bet365 Inplay Filter
- **Purpose**: Filter in-play events by sport and league.
- **Parameters**:
  - `sport_id` (optional): Filter by sport ID. Default: 1.
  - `league_id` (optional): Filter by league ID. Default: 0.
  - `skip_esports` (optional): Option to exclude esports data.

### Bet365 InPlay
- **Purpose**: Retrieve detailed in-play data.
- **Parameters**: None

### Bet365 InPlay Event
- **Purpose**: Access detailed information on in-play events.
- **Parameters**:
  - `FI`: Identifier for the event.
  - `stats` (optional): Include stats in the response.
  - `lineup` (optional): Include lineup information.

### Bet365 Upcoming Events
- **Purpose**: List upcoming events and fixtures.
- **Parameters**:
  - `sport_id`: Filter by sport ID. Default: 0.
  - `league_id` (optional): Filter by league ID. Default: 0.
  - `day` (optional): Specify the day for the events.
  - `page` (optional): Pagination parameter.

### Bet365 PreMatch Odds
- **Purpose**: Access odds for pre-match events.
- **Parameters**:
  - `FI`: Identifier for the event.

### Bet365 Result
- **Purpose**: View results for past events.
- **Parameters**:
  - `event_id`: Identifier for the event.

## Conclusion

BetsAPI2 MCP Server is your go-to source for accessing comprehensive bet365 data. With tools designed for both in-play and pre-match analysis, you can stay informed and make strategic decisions with confidence. Explore the features and leverage the detailed insights provided by BetsAPI2 to enhance your sports betting experience.