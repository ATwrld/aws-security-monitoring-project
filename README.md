# AWS Security Monitoring Pipeline (SOC | IAM | GRC)

## Overview
Built an event-driven cloud security monitoring system using AWS services to detect and respond to IAM misconfigurations.

## Architecture
Security Hub → EventBridge → Lambda → S3

## Features
- Detects security findings from AWS Security Hub
- Processes events using AWS Lambda
- Stores findings in S3 for auditing and compliance
- Simulates SOC alert pipeline

## Technologies Used
- AWS Lambda
- AWS Security Hub
- Amazon EventBridge
- Amazon S3
- IAM

## Use Case
This project simulates a real-world SOC environment where security findings are automatically processed and logged for compliance and incident response.

## What I Learned
- Event-driven architecture in AWS
- IAM roles and permissions
- Cloud security monitoring
- Automation of security workflows
