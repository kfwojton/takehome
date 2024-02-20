# How to run this code: 

## On Mac / Linux: 

In terminal follow these commands: <br> 
`git clone https://github.com/kfwojton/takehome.git`  <br>
`cd takehome` <br>
`virtualenv myenv`<br> 
Note install virtual env here if you don't have it installed https://virtualenv.pypa.io/en/latest/<br>
`source myenv/bin/activate` <br>
`pip install -r requirements.txt`<br> 
copy the contents of example.env file to a new file called .env <br> 
`python manage.py runserver` <br>

Navigate to localhost:8000 on your browser. 

## On Windows: 

Download visual studio code, and add the git bash scripting language https://code.visualstudio.com/docs/sourcecontrol/intro-to-git, then follow the above steps. 


# Interview Questions 

## Discovering a Bug 

Prompt
~~~~~~

Suppose we discover a bug with our algorithm and investors for two deals had incorrect
allocations. This means that some of the investors ended up investing more than they were allowed to
while others invested less than they were allowed to. One of deals happened two years ago and the
other one happened two weeks ago. Please describe, in detail, how would you go about correcting this
issue and how would you communicate this to the affected customers.

Response
~~~~~~~~


I would run this app using a postgres database and record all of the activity, as per implemented with this working example. I would also make sure to have users log in with a sign in with a check box saying they agree to the terms of service. In this terms of service, there should be specific terms around; "the final allocations when executed are final". Also prior to execution, I would send everyone an email with a confirmation of the amounts they are investing and % of such. At the same time there should be a serious bug; This way we can see exactly what happened and recall back with an investigation and a report, and a resolution. Given that equity is already distributed, it would likely not be an option to change the holdings of the company. But should there have been an accounting error, or reasonable mistake, I would work with the company who raised the money, raise this to their attention. From an organizational perspective, I would put this process/project management:

    1. Open a slack channel called Bug Reporting, that has a staff assigned to it; which rotates weekly. This way we can have a dev on call to address any issues. As issues come in; staff can report the bug, and the staff would just go into the database, look up the transaction, check to see if it was an issue, provide a resolution and post that on the channel. Then that person would be responsible for the resolution. This doesn't have to be a tech staff; more a customer service staff.
    2. I would also have a monthly meeting with the team to discuss any issues that came up, and how we can prevent them in the future.

# Squeezed Down 
Prompt
~~~~~~

An angry investor sent us a note about how they keep getting squeezed down to $25K per deal even
though their requested amount is $100K. Underneath the hood, this was because there's limited
allocation (low supply) and a high volume of investors looking to invest (high demand). How should
we communicate this to an investor in a way that minimizes the damage to our relationship with
the investor?

In addition, can you think of a better way we could change the proration basis logic so that
this could potentially happen less often?

Response
~~~~~~~~

I would respond with a message; I'm sorry to hear that you are not receiving the allocations
you have requested. When oversubscribed, we have a policy of allocating shares based on total 
current holdings of the venture. This is largely based on a preference for startups who typically
prefer to follow on investors, and to give first rights to current shareholders. As your basis increases
so does your opportunity to invest in the future. I would be happy to jump on a call should you have 
an interest to discuss how this pro-ration approach is utilized. Furthermore, this policy 
incentivizes investors to invest in low capitalized companies, giving them first right to
invest based on their total basis. I would be happy to share some deals with you where you
can get a high % of basis. As always; I we at AngelList are happy to help you find the right deal for you.

With this response I am pacifying their concerns, and also providing them with a solution and pushing them 
to an action that allows for more deal flow. 

