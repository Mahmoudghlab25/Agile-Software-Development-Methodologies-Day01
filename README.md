# Agile-Software-Development-Methodologies-Day01

This repository demonstrates Agile engineering practices using:

- Clean Code principles
- Test Driven Development (TDD) techniques

## Used Stack and Programming Languages

### Programming Language

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

### Testing Stack

![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)

### CI Tools Covered in This Project

![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white)
![AWS CodePipeline](https://img.shields.io/badge/AWS_CodePipeline-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)

## Clean Code Principles

This project applies practical clean code ideas:

- Meaningful naming: function and test names should explain intent.
- Small focused functions: each function should do one thing well.
- Readability first: straightforward control flow and simple logic.
- Defensive behavior: invalid input should be handled safely.
- Testability: behavior should be easy to verify with unit tests.

## Test Driven Development Techniques

The repository follows a basic TDD workflow:

1. Write a failing test for the required behavior.
2. Implement the smallest change needed to pass the test.
3. Refactor code while keeping tests green.
4. Repeat for new scenarios and edge cases.

Current tests cover:

- Standard addition
- Addition with spaces
- Negative numbers
- Invalid input fallback behavior

Run tests locally with:

```bash
pytest -q
```

## Task 1

### Objective

Create a function that takes a string parameter representing an addition operation and returns the sum of integers in that string.

### Implemented Function

- File: task1.py
- Function: get_sum_from_string(operation_str)

### Expected Behavior

- Input format: two integers separated by exactly one + operator.
- Whitespace around numbers is allowed.
- Negative numbers are allowed.
- On invalid input, the function returns 0.

### Examples

- "10+20" -> 30
- " 5 + 5 " -> 10
- "10 + -5" -> 5
- "invalid" -> 0

### Quality Notes

- Function includes basic exception handling for malformed input.
- Unit tests in test_task1.py validate normal and edge cases.
---
## Task 2: Benchmark for CI Applications

### Scope

Compare three CI tools for business usage:

- Jenkins
- AWS CodePipeline
- GitHub Actions

Evaluation focus:

- When to use each tool (business context)
- Pricing model
- Deployment settings and operational setup

### 1) Jenkins

When to use:

- Teams requiring maximum customization and plugin flexibility.
- Organizations with self-hosted infrastructure and strong DevOps support.
- Complex legacy or hybrid environments not tied to one cloud provider.

Pricing:

- Jenkins software is free and open source.
- Costs come from infrastructure, storage, maintenance, upgrades, and admin effort.
- Total cost can grow with scale due to operational overhead.

Deployment settings:

- Commonly self-hosted on VM, Kubernetes, or bare metal.
- Requires configuring agents/executors, credentials, plugins, and backup strategy.
- Security hardening and plugin lifecycle management are critical.

### 2) AWS CodePipeline

When to use:

- Teams already invested in AWS services (CodeBuild, CodeDeploy, ECS, Lambda).
- Businesses that want managed pipelines with lower infrastructure management.
- Enterprises needing strong IAM-based access control and AWS-native governance.

Pricing:

- Pay per active pipeline/month (AWS region dependent).
- Additional costs for integrated services (for example CodeBuild minutes, artifact storage, deployment targets).
- Can be cost-efficient in AWS-centric workloads.

Deployment settings:

- Define stages (source, build, test, deploy) in AWS Console, CloudFormation, or CDK.
- Integrates with GitHub/CodeCommit as source providers.
- Uses IAM roles/policies and supports cross-account deployment patterns.

### 3) GitHub Actions

When to use:

- Teams hosting code on GitHub and seeking fast CI/CD onboarding.
- Projects that benefit from marketplace actions and pull request automation.
- Startups and product teams prioritizing speed and developer experience.

Pricing:

- Free tier available (limits vary by plan and runner type).
- Paid by usage (minutes, storage) beyond included quotas.
- Self-hosted runners can reduce hosted-runner usage costs in some cases.

Deployment settings:

- Pipelines defined as YAML workflows under .github/workflows.
- Triggered by events (push, pull_request, release, schedule, manual dispatch).
- Supports hosted and self-hosted runners, environments, and approval gates.

### Benchmark Summary

| Tool | Strength | Main Trade-off | Best Fit |
|---|---|---|---|
| Jenkins | Maximum flexibility and plugin ecosystem | Higher operations and maintenance effort | Large/custom enterprise CI setups |
| AWS CodePipeline | Deep AWS integration and managed service model | Cloud lock-in to AWS patterns | AWS-first organizations |
| GitHub Actions | Fast setup and strong GitHub-native workflow | Cost growth with heavy runner usage | GitHub-centric teams and fast-moving products |

### Business Recommendation Guide

- Choose Jenkins when deep customization and self-host control are mandatory.
- Choose AWS CodePipeline when your architecture is primarily on AWS.
- Choose GitHub Actions when code collaboration and CI/CD are centered on GitHub.
---
| Author |
|---|
| Mahmoud Ali |
With My Regards 😊