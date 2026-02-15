- how effectively you can collaborate within and across teams

  - We had a situation where a large client like Air Canada was onboarded onto our system and I was responsible for the API side and another team was responsible for the ingestion aspect and consuming our api
  - So I had the responsibility to execute the API side and co-ordinate with the off shore team to move things forward
    - So I organized weekly syncs, created a teams channel for the people that were needed for cross communication and shared documents leading discussion on how the API should be consumed from the event hub
    - Got buy in from the QA tester, Product Owners and more importantly the Business Analyst of what will be updated in the DB
  - Result of this was we were able to onboard 40k members onto our system with 4 month latency between our time of execution
    - and we absolved the manual process reducing manual work of 10k monthly manual setup to 15 mins

- We'll explore your ability to mentor

  - So I am responsible for mentoring groups, engineers on different levels
  - Depends on the engineer - Pair Programming, KT sessions, sharing documents, hand off approach when needed for people to create frameworks to learn themselves
  - Engineer who was an SRE and has not coded in over a decade
  - I was tasked with working with him on delivering a new API service
  - So I setup Pair programming sessions in the beginning then incrementally chunked and provided him work to do himself
  - Result engineer is more confident in terms of developing features - and exploring and implementing his framework of attacking problems

- enhance team culture (Recognition of various engineers throughout the process)

  - Strategically recognize engineers for each big milestone they make within the team - podium

- improve engineering practices (Burpsuite Scans) - proactive approach to problem solving

  - So alot of times we have a production deployment we need to run it past security teams approval
  - I noticed that burpsuite scans were what they were running and the DevOps pipeline could facilitate this feature
  - I co-ordinated with the AppSec team to have it installed on our pipelines
  - with it we have automated Security scans on our system and productionizing conversation and latency from AppSec team has been within a day as opposed to taking a week

- scenarios related to customer focus

  - So we have a feature that is a portal where a user can communicate with us using the portal - one was sending text and the other was sending emails
  - And after my investigation I found that we could implement the backend logic to route the communication without having 2 different interfaces
  - So I had a conversation with UI/UX and the PO to establish if it would be a better experience for the customers and then explained from the technical side that the effort would be minimal
  - With it we developed a centralized view for customers to contact us without jumping around different pages and at the same time reduced implementation work for the engineers delivering the product before the established time

- impact

  - We had all ourr backend engine sparsed out and being SOAP services which were highly underperformant
  - So I worked with a couple of engineers and solution architect to design a solution that would centralize all of our calls through a single system with GraphQL being the aggregation layer
  - Result of this was - we were able to decommission a lot of our legacy services and improve performance for our backend engine across for one of our major service calls by 80% across 100+ different applications serving 90k request per month

- ownership

  - We had a scenario where alot of our business rules configuration was hardcoded and implemented using proprietary software
  - So I had to do data modelling and solution session to drive and own this feature to offload ourselves away from this implementation
  - Result of this I created an inhouse rules configuration engine that eliminated hardcoding and 1 week latency to 15 mins without needed production deployments and saving 400k in licensing fee

- leadership

  - So we have a replatforming initiaitve that has a landing page on it
  - I was responsible for negotiating timelines, establishing requirements with Product owners and UI/UX, designing the technical roadmap and solution design for it - communicate it to my team - implement feature while mentoring the team members throughout the process and get the feature across the finish line
  - we had a better experience for our customers, load time reduced by 80% and the search performance improved by 65-90% for our feature

- learning
  - I like to always chase uncomfort and curious about understanding things that I am not aware of
  - For me when I started I was mostly working frontend but my curiosity got me working full stack REST ful aspect from there I learned GraphQL
  - Later I worked on infrastructure now I want to learn more about ML
- Growth mindset
  - When desigining the backend engine of our business unit - it was a challenging project
  - throughout the process I would see myself going inside rabbit holes and being concerned about every edge case which led to lack of progress and some big features being delayed
  - I understood from that that progress is important, need to reduce the noise not jump into rabbit holes when I see myself - timebox myself
    and see what problem I am trying to solve and not chew over aspects that don't progress the high level solution and have the confidence that you can find a solution for any problem
