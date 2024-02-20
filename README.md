# How to run this code: 

## On Mac / Linux: 

In terminal follow these commands: <br> 
`git clone https://github.com/kfwojton/takehome.git`  <br>
`cd takehome` <br>
`virtualenv myenv`<br> 
Note install virtual env here if you don't have it installed https://virtualenv.pypa.io/en/latest/<br>
`source myenv/bin/activate` <br>
`pip install -r requirements.txt`<br> 
copy the contents of example.env file to a new file called .env
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

I propose implementing the app utilizing a PostgreSQL database to meticulously track all user activity, mirroring the functionality demonstrated in our current operational model. Additionally, I would ensure a streamlined user experience by incorporating a sign-in feature accompanied by a checkbox for users to consent to our terms of service.

Within these terms of service, precise language would be outlined, particularly emphasizing the irrevocability of final allocations upon execution. To further enhance transparency and user confidence, prior to any execution, I would initiate an automated email distribution, furnishing investors with a comprehensive breakdown of their investment amounts and corresponding percentages.

Simultaneously, a robust contingency plan would be in place to address any unforeseen issues, including the discovery of critical bugs. This strategic approach enables us to conduct thorough investigations, compile detailed reports, and swiftly implement resolutions. Although adjustments to equity distribution may be impractical once finalized, any accounting discrepancies or genuine oversights would be promptly addressed through collaboration with the fundraising entity.

From an organizational standpoint, meticulous project management practices would underpin this entire process, ensuring efficiency, accountability, and ultimately, the integrity of our operations.

    
1. Establish a dedicated Slack channel named "Bug Reporting" with a designated staff member assigned to it, with rotations on a weekly basis. This ensures we always have a developer available to promptly address any reported issues. As bugs are reported, the assigned staff member would access the database, investigate the transaction in question, provide a resolution, and communicate it within the channel. This responsibility doesn't necessarily fall solely on technical staff; rather, it could involve customer service personnel, ensuring a holistic approach to issue resolution.

2. Implement a monthly team meeting to facilitate open discussions about any encountered issues and brainstorm proactive measures to mitigate them in the future. This collaborative approach fosters a culture of continuous improvement and proactive problem-solving within the team.

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
I would respond with empathy, acknowledging your concern about not receiving the allocations you requested. In such situations of oversubscription, our policy prioritizes allocations based on the total current holdings of the venture. This approach is rooted in our commitment to supporting startups and giving precedence to existing shareholders, who often demonstrate a commitment to the company's growth by reinvesting.

As your investment basis increases, so does your opportunity to participate in future rounds. If you're interested, I'd be more than happy to schedule a call to discuss how this proration approach is implemented in more detail.

Moreover, this policy is designed to incentivize investments in early-stage companies, offering existing shareholders the first right to invest based on their cumulative basis. I'd be delighted to share some promising deals with you where you can potentially secure a higher percentage of basis.

Remember, we're here at AngelList to assist you in finding the most suitable investment opportunities tailored to your preferences and goals. Let's explore how we can optimize your investment portfolio together.




