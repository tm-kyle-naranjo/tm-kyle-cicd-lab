# Contributing to CI/CD Workflow Project

We welcome contributions to our CI/CD Workflow project! This document provides guidelines for contributing to this repository.

## Getting Started

1. Fork the repository on GitHub.
2. Clone your fork locally:
   ```
   git clone https://github.com/your-username/your-repo-name.git
   ```
3. Create a new branch for your feature or bug fix:
   ```
   git checkout -b feature/your-feature-name
   ```

## Making Changes

1. Make your changes in your feature branch.
2. Test your changes thoroughly.
3. Commit your changes:
   ```
   git commit -m "Add a descriptive commit message"
   ```
4. Push to your fork:
   ```
   git push origin feature/your-feature-name
   ```

## Submitting a Pull Request

1. Go to the original repository on GitHub.
2. Click the "New pull request" button.
3. Select your fork and the feature branch you created.
4. Fill in the PR template with all relevant information.
5. Submit the pull request.

## Workflow File Changes

When modifying workflow files:

1. Ensure changes are consistent across `dev-workflow.yml` and `prod-workflow.yml` if applicable.
2. Test changes in `template-workflow.yml` thoroughly.
3. Update documentation in README.md if workflow behavior changes.

## Environment and Secret Management

- Do not commit actual secret values to the repository.
- When adding new variables or secrets, update both `dev` and `prod` environments.
- Document any new environment variables or secrets in the README.md.

## Code Style

- Follow existing code style and formatting in Python scripts.
- Use meaningful variable names and add comments where necessary.

## Reporting Issues

- Use the GitHub issue tracker to report bugs or suggest features.
- Provide as much context as possible, including steps to reproduce for bugs.

## Community and Conduct

- Be respectful and constructive in discussions and code reviews.
