# SWE1 App – Continuous Integration

[![Build Status](https://app.travis-ci.com/cesarsanchez1/swe1-app.svg?branch=main)](https://app.travis-ci.com/github/cesarsanchez1/swe1-app)
[![Coverage Status](https://img.shields.io/badge/coverage-94%25-brightgreen)](https://coveralls.io/github/cesarsanchez1/swe1-app?branch=main)

This Django application is configured with Continuous Integration using Travis CI.  
Each build automatically runs:
- **Black** (code formatter)
- **Flake8** (linter)
- **Pytest + Coverage**
- **Deployment to AWS Elastic Beanstalk**

The project demonstrates a complete CI/CD pipeline for Django using Travis CI and AWS.
