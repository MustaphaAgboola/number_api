# Number Properties API

## Overview
A Flask-based API that provides detailed mathematical properties and insights for a given number.

## Features
- Classify number properties
- Identify prime, perfect, and Armstrong numbers
- Generate fun mathematical facts
- Robust error handling

## Endpoints

### 1. URL Parameter Endpoint
**Path:** `/number/<number>`
**Method:** GET
**Example:** `http://your-domain/number/371`

### 2. Query Parameter Endpoint
**Path:** `/api/classify-number`
**Method:** GET
**Query Parameter:** `number`
**Example:** `http://your-domain/api/classify-number?number=371`

## Response Structure

### Success Response
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["odd", "armstrong"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number..."
}
```

### Error Response
```json
{
    "number": "alphabet",
    "error": true,
    "message": "Please provide a valid number"
}
```

## Supported Number Properties
- Even/Odd
- Prime
- Perfect
- Armstrong

## Installation

### Prerequisites
- Python 3.8+
- Flask
- Requests library

### Steps
1. Clone repository
2. Create virtual environment
3. Install dependencies
4. Run application

## Deployment
- Supports AWS EC2 deployment
- Systemd service configuration included
- Runs on port 5000

## Error Handling
- Handles non-numeric inputs
- Validates positive numbers
- Provides descriptive error messages


