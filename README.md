# code_review
Code review walkthrough for the UKRSE conference 2019

## Purpose

This repository is intended to show a snapshot of the development process at
the point of a _pull request_, when the code undergoes a review to determine
its suitability to be merged into the master branch.

## GitHub Concepts

 * `Issue`: An _Issue_ describes a slice of work to be performed, along with a narrative and discussion of the progress of the issue. An issue should typically contain explanations of:
   * _What_ is to be done
   * _Why_ is it being done
   * _How_ is it being done
 * `Pull Request`: A _Pull request_ (sometimes known as a _merge request_) is a request by a developer to merge code in development branch, and described by an Issue, into the master branch. This request may be considered against the stated intentions of the Issue and permission may be subject to review, potentially against multiple requirements. Typically these can be:
   * _Code Review_: Is the good of acceptable quality? Does it meet the requirements of an agreed style guide? Could it be obviously improved?
   * _Requirements_: Does it do what the Issue requires it to do? Is there scope creep or missing functionality?
   * _Testing_: Do all tests pass? Is the coverage of the tests sufficient to rule out bugs in the submitted code?

## Contents

| File                  | Description |
| --------------------- | ----------- |
| `README.md`           | This file |
| `LICENSE`             | The license under which this work is made available |
| `HOWTO.md`            | Introduction to the respective responsibilities of the code developer and reviewer |
| `CONTRIBUTING`        | Contribution guide |
| `src`                 | Source code and associated test directory |
| `azure-pipelines.yml` | Automated testing configuration file | 
