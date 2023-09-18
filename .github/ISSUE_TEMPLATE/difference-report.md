---
name: Difference report
about: If there is a difference between the sync and async repository
title: "[DIFFERENCE]"
labels: ''
assignees: ''
body:
- type: input
  attributes:
    label: "File name"
    description: "The file name"
    placeholder: "/src/DisOAuth/url.py"
  validations:
    required: true
- type: input
  attributes:
    label: "Async line number"
    description: "The line number where the difference is, in the async repository"
    placeholder: "33, 56, (multiple lines) 72-79"
  validations:
    required: true
- type: input
  attributes:
    label: "Sync line number"
    description: "The line number where the difference is, in the sync repository. Only fill out if the line number is differenct in both repositories"
    placeholder: "36, 59, (multiple lines) 75-82"
- type: markdown
  attributes:
    value: "## Thanks for telling us about the difference! We will look into it!"
    

---

**Async or Sync?**
While there may be issues between the differences of the two repositories, remember that this repository is the async version, and not the [sync repository](https://github.com/Arcader717/DisOAuth2), so there will be `async def` and `await` statements in this repository

**Context**
Try to provide the file and line where the difference is for BOTH repositories

**Reminder**
While it may happen, remember, if the update was made recently on the sync repository, it will be made to the async repository soon after, so wait until the update for the async version to report
