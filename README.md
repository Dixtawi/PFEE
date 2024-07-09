# PFEE : CV Relevance Prediction


## Introduction
In the current recruitment context, companies receive a large number of applications for each job opening. Manually evaluating these resumes is a time-consuming task and prone to biases. Predicting the relevance of resumes to job postings using machine learning can greatly improve the efficiency and fairness of the recruitment process.

However, the use of sensitive personal data in machine learning models raises concerns regarding data privacy and security. This is where our project comes in. We have explored advanced techniques such as Privacy-Preserving Machine Learning (PPML) and Fully Homomorphic Encryption (FHE) to develop a model capable of predicting the relevance of resumes while ensuring the confidentiality of candidate data.

## About This Project
### Project Overview
As part of our engineering school curriculum, we undertook a capstone project (PFEE - Projet de Fin d'Études Encadré) in collaboration with Zama, a pioneering company in the field of homomorphic encryption. Our primary objective was to delve into the functionalities of Privacy-Preserving Machine Learning (PPML), Fully Homomorphic Encryption (FHE), and Concrete ML.

### Project Goals
In this project, our team focused on leveraging these advanced encryption techniques to develop a model that predicts the relevance of a CV (Curriculum Vitae) to a job offer. The goal was to ensure that the predictions are made securely without compromising the privacy of the data involved.

### Key Technologies
- **PPML (Privacy-Preserving Machine Learning)**: Techniques that allow machine learning models to be trained and used without exposing sensitive data.
- **FHE (Fully Homomorphic Encryption)**: A form of encryption that enables computations on encrypted data without needing to decrypt it first.
- **Concrete ML**: An open-source library developed by Zama, which integrates FHE with machine learning to provide privacy-preserving predictions.

### Project Contributions
1. **Understanding and Implementing PPML and FHE**: We conducted an in-depth study of PPML and FHE principles and their implementation.
2. **Model Development**: Created a machine learning model using Concrete ML to assess CVs' relevance to job offers.
3. **Data Privacy**: Ensured that all data used in the predictions remained encrypted, thereby maintaining user confidentiality and data integrity.

## Continuous Integration

This project uses GitHub Actions for continuous integration.

### Configuration

The CI workflow is defined in `.github/workflows/ci.yml`.

### Validating Commit Messages

Commit messages should follow this format:
- `feat: Feature description`
- `fix: Description of the fix`
- `docs: Description of documentation`
- `style: Description of style changes`
- `refactor: Description of refactoring`
- `test: Description of tests`
- `chore: Description of maintenance tasks`

A commit message validation hook is included and will be executed during the CI process.

### Installation of Dependencies

```sh
cd script/
make all
```
