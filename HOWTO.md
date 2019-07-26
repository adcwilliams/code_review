# The Code Review Process

The Review is an integral part of ensuring that code that you write is bug free and tested. This GitLab project has demonstrated the mechanics of using GitLab to perform a review, but it doesn't discuss what you, as a reviewer, should be looking for when ask to review a piece of code, nor does it provide guidelines of what you, as a code author, should be doing to make the work of a reviewer easier and not turn it into a burden. This article will concentrate on those topics, how to make a review work from both perspectives.

## What is a Review

Typically, a Git project has an _owner_ and _collaborators_. In the case of large projects there is frequently more than one owner and there may also be other, purely technical, roles intended to manage the codebase. The principal distinction between the owner and collaborators is that only the owner (or delegates) has permission to write to the `master branch`. This ensures that all changes to the master branch have to be written and tested in personal development branches and then merged into the master branch via `merge requests` (GitHub calls them _pull requests_). It's at this point that the review is performed. This ensures that all code in the master branch has been tested and reviewed, and that all development branches created from master should be based on reviewed code.

## The Background to a Review

Large projects typically start of with _style_ and _development_ guides so that a reviewer has a document to review code against. If you're starting a collaborative project it's important to ensure that you have a set of standards to act as benchmarks. This ensures that:

 * Everybody knows what the technical or quality threshold is for acceptable code.
 * The reviewer has a document they can refer to so that they know what to look for.
 * There are no (or at least fewer!) arguments as to what is _right_ and what is _wrong_.

A language like Python has the official `PEP-8` style guide that is typically used as a reference for _correct_ code. Other languages may or may not have official guides, but it's less important which one you choose than the fact that you have one and stick to it.

For individual projects it's still a good idea to pick a style guide or a formal version of the language for reference. Individual projects frequently turn into collaborative projects unexpectedly. At some place in your project, perhaps in a `README.md` file or Wiki, you would have a few lines, something like:

> This project was written in Python 3, following the PEP-8 style guide.

...or...

> This project was written according to the Fortran 2008 standard, using Google Style Guide version 1.0.

Now both the author and reviewers know the template that the code should be reviewed against.

## The Burden on the Author

Reviews typically follow the peer process familiar to researchers in all fields. The assumption is that by taking part in the process of software development you will be called upon to perform reviews, and likewise can expect that people will be willing to review your code. However, if you make your code difficult to review then you may find people reluctant to get involved. On the other hand, if you follow a few basic rules you can make the process easier and encourage more people to volunteer. So what does an author need to do to prepare for a review?

### Prepare the Groundwork

It's always a good idea to start off a new piece of work with an **Issue**. Issues work similarly in both GitLab and GitHub, and allow the author to document what they want to achieve. They help prevent scope creep and provide a reference document for both the author and reviewer. The author can make notes as they go along to remind themselves what they've done, and the reviewer can follow the author's thought processes and decision making. It's generally a good idea to include the potential reviewer(s) in the Issue as early as possible so they can see what is happening. This means that when a review is requested, the work involved shouldn't come as a complete surprise to the reviewer. Remember to test your code and if possible document the tests performed in the Issue. The best way of achieving this is by using automated `unit tests` which run whever a commit is performed. That topic is outside the scope of this document.

### Bite-Sized Chunks

Don't try and dump 1000 lines of code on a reviewer with little or no experience in what you are doing and expect the reviewer to take the time to review it adequately. A good review should take about fifteen minutes or less - any longer than that and it becomes a burden. This requires some thought as to planning sufficiently concise issues. Try and break large tasks into small chunks, and if that's not possible then conduct intermediate reviews as the task progresses. If a large piece of work is unavoidable then try bringing in multiple reviewers or be prepared to reward the reviewer in a suitable manner!

### Documentation

There should be sufficient information for a reviewer to make a judgement. This includes the Issue, describing what is being performed, but also the code should be properly documented. This means using inline comments to describe the purpose of any new variables, and what blocks of code do. Two questions that need to have ready answers are **Why?** and **How?**.

### The Merge Request

The Merge Request is the formal review process. If all has gone well the reviewer should have an Issue describing what the author wishes to be reviewed, a small enough chunk of documented code to understand and absorb, and ideally, tests demonstrating that the code actually does what the author claims. The merge request allows both parties to ask questions make comments, and ideally reach a consensus. In collaborative projects the owner or branch manager will also be involved to rubber stamp the review and occasionally break deadlocks. In smaller projects a third party may become involved to perform a similar role. Once there is agreement, the development branch is merged and the Issue and Merge request closed.

## The Burden on the Reviewer

Typically, the author will have done the above preparation and the reviewer's role is a relatively easy one. Remember, the quality of the code is the author's responsibility and you are doing them a favour by helping to improve that quality. But what should a reviewer look for in order to say that they have performed a thorough review?

### Style

If you have a style or development guide to act as a template, then make sure that the code matches the guide. If it doesn't then point out where it deviates.

### Tests

If the author has provided automated tests then run them and make sure the results are what they should be. This will catch any odd circumstances whereby the author's development environment has been set up in such a way that means code will not build or run on other machines.

### Code

Look through the code a high level and see if it appears to do what the author is suggesting it should do. If the tests work then you can assume that it does, which makes your life easier. Use your knowledge of the programming language in question to suggest any improvements, perhaps to efficiency or readability, or suggest a way in which it could be done better. An inexperienced reviewer may be nervous about being too critical, but it's better to make note of things that _might_ be wrong than to let potentially broken code pass. The author will thank you for picking up mistakes when the alternative is having to retract a publication.

## Summary

 * A code review is not meant to be a burden. Regular reviews can save time, catching bugs and suggesting improvements while development is in progress.
 * A review is made considerably easier if the author provides a set of tests that can be run. These can be sample input datasets with expected output, or automated unit tests that can be run to provide evidence that a function returns a correct result.
 * The correct level of critique comes with practice. _Authors_: Don't get too attached to your code or your favourite way of achieving a result. Don't be afraid to take advice. _Reviewers_: Review the code, not the author. Making a bad mistake does not make them a bad person!
 * Every programmer, no matter how experienced, occasionally makes horrendous, code-breaking mistakes. The point of the review is to catch these mistakes before they become embedded in the master branch and are used in research. Don't be afraid to comment.