# The .openshift Directory

The .openshift directory is a hidden directory where a user can create action hooks, set markers, and create cron jobs.

Action hooks are scripts that are executed directly so can be written in Python, PHP, Ruby, shell, etc. OpenShift Origin supports the following action hooks:

## Table 1. Action Hooks

* pre_build: Executed on your CI system if available. Otherwise, executed before the build step
* build: Executed on your CI system if available. Otherwise, executed before the deploy step
* prepare: Executed just prior to a deployment ID being calculated and before the deployment is ready to use
* deploy: Executed after dependencies are resolved but before application has started
* post_deploy: Executed after application has been deployed and started

Note: On Windows, the execute permissions of an action hook files will be lost during the git push. To fix this problem, you can run this command:

``# git update-index --chmod=+x .openshift/action_hooks/*``
``# git push``

OpenShift Origin also supports the ability for a user to schedule jobs to be ran based upon the familiar cron functionality of linux. Any scripts or jobs added to the minutely, hourly, daily, weekly or monthly directories will be ran on a scheduled basis (frequency is as indicated by the name of the directory) using run-parts. OpenShift supports the following schedule for cron jobs:

* daily
* hourly
* minutely
* monthly
* weekly

The markers directory will allow the user to specify settings such as enabling hot deployments or which version of Java to use.
