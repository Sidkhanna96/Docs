# Technical Deep Dive

- GBCore-2 & Landing Page

GBCore-2:

- STAR
  - Cross Functional Teams
    - SA, MMB, MP, Internal Tooling
    - Managing Priorities and Communicating to Product owners - priority features
  - Technical Tradeoffs
    - (GraphQL vs REST API, Redis vs Non Redis, NoSQL vs SQL) -> Outcome
- Successes
  - Business (Business Impact) vs Personal Growth (Technical vs Mindset/Methodology)
- Challenges
  - Lessons Learned
  - Technical vs Non Technical

GB-Core-2:

STAR:

- Situation:
  - Within my Business Unit - There were alot of sparsed out SOAP APIs that each application called in its own way - no one source of truth
  - there was a GraphQL service which was extremely vertical - leading to extremely low performance and difficult maintainability
- Task:
  - I was tasked with Designing System Architecture and Implement with 2 Engineers and proposing solutions to Solution Architects
- Action:
  - So I did a High Level Design of the architecture and then we had few meeting to discuss trade offs, dependencies and maintainability
    - I proposed GraphQL as an aggregation layer - with various different SOAP services and REST APIs Called
  - We went with GraphQL with federated architecture using subgraphs - Desigining re-implementation of various features.
  - Reasoning Since we want to move away from the SOAP services - as they're difficult to add business logic to, slow in performance and cost alot in terms of licensing since run on on-prem IBM servers - costing alot in licensing
    - Trade offs my solution incremental but it doesn't pivot the company to move off of these legacy services.
      ---- Need more information here
- Result:
  - We had massive improvement for alot of service calls - our main call improved from 1.8 seconds to 0.25 - 0.5 ms
    - It quickly made alot of various different applications - highly responsive, maintainable and available - as it would autoscale based on requirements
    - Saved money in terms of IBM on prem licensing costs and moved to our AKS architecture.
  - Alot of new implementations we wanted to do were able to be easily implemented in new services - GraphQL is also a language people want to learn so engineers were excited to contribute to it
  - We decommed alot of applications from calling the SOAP services
  - It centralized a service where alot of different applications would just be calling it

Growth:

- Technical:

  - Personally understood GraphQL,
  - Architectures Designs and decisions - BFF vs Federated Architecture - where the business logic should live
  - performance improvements
    - Data Loader Pattern
    - Parallelizing Calls
    - Caching Strategy
    - Pagination
  - when to use SQL vs NoSQL
    - Alot of our data was relational
    - NoSQL for unstructured data
  - How I can propose my solution
  - Parallelizing calls

- Non-Technical:

  - No Perfect solutioning, think about edge cases especially the main ones - but it is also important to deliver a product and get work done at a certain level.
  - There is always a way you can solve for post deployment issues - some might be involved some might not be.
  - Break problem down into smaller components especially if its large
  - TimeBox myself
  - understand the problem

- Technical:

  - Do the smallest possible janky POC to understand the crux of the problem to solve
  - Read Documentation / Watch quick videos but found for me kinestics approach to be the best way or pairing with someone to see how they look at the problem

- Lessons Learned:
  - The project was around 8-12 months - so long
    - This is where you need to constantly communicate
    - This is where you need to demonstrate business impact - less blackbox - business was concerned
    - Think about iterative way to realize impact also offers better instantaneous feedback loop
  - Circle back to TimeBoxing myself and breaking the problem down into smaller components - personally I was trying to solve the entire problem all over and then trying to also think about all edge cases
  - Learned to also communicate, think about what I want to communicate and being succinct with my communication to get to the main problem - anything ansciliary can be figured out later in the process.

Challenges:

- Non Technical Challenges:

  - Business did not know impact - demo the impact
  - Onboarding new people requires an initial time where quality needs to be maintained but need patience - need to be strategic a little with the stories and communicate and pair program especially in the beginnning
  - Vendor communications and establishing what was needed

- Technical Challenges:

  - Some request were making request to an API quiet often in the same request cycle - had to leverage dataloader pattern (Entitlements)
  - State Management vendor had a unique way to manage states
  - Business logic should be further downstream closer to data - in terms of rules - mistake
  - --- need more

- Cross functional Teams:
  - Worked with architects, vendors, internal tooling team, front end and product owners
  - Leveraged product owners to understand what features would be priority
  - communicated with vendors what was our priority
  - understood that out of plethora of features to implement and our consumers which ones were the crucial ones
    - We prioritized which business consumer had the highest value
    - We then catered to its requirements primarily before tailnig off into other features in the later end
    - We understood the issue at high level of what various consumers would need so that we designed the solution having context in mind and keeping our system agnostic and dynamic

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Project: GraphQL Federation Platform for Legacy API Modernization

⸻

SITUATION

In our business unit, we had a fragmented backend landscape—many applications called legacy SOAP APIs directly, each in their own way, leading to inconsistent data, duplicated logic, and brittle integrations. In parallel, we had a monolithic GraphQL service that had grown vertically without proper modularization, resulting in poor performance, low maintainability, and tight coupling between consumers and backend systems.

⸻

TASK

I was responsible for leading the system architecture redesign and implementation alongside two engineers, and for presenting architectural proposals to our Solution Architects. Our mandate was to build a scalable, modern API layer that could:
• Improve performance and maintainability,
• Support future feature development more easily, and
• Begin reducing our reliance on expensive, on-prem IBM-hosted SOAP systems.

⸻

ACTION

I kicked off with a high-level design and led a series of architecture and design review sessions to align on tradeoffs, dependencies, and long-term maintainability.

Key decisions and actions:
• GraphQL as an aggregation layer: Proposed GraphQL as the central gateway to unify calls to SOAP and REST services, abstracting backend complexity from clients.
• Federated GraphQL architecture using Apollo Subgraphs: Modularized our GraphQL schema and allowed us to scale services independently and onboard new teams with minimal friction.
• Performance improvements: Introduced the DataLoader pattern to batch and cache repeated queries within request cycles, especially for entitlement checks. Parallelized downstream calls wherever possible and implemented strategic caching and pagination to reduce load and improve responsiveness.
• Incremental migration approach: We chose to build incrementally, wrapping SOAP services behind GraphQL first, which allowed teams to migrate gradually while delivering short-term wins. Though we didn’t fully sunset legacy systems, this approach allowed rapid progress without a risky big-bang rewrite.

⸻

RESULTS
• Reduced average response time for our main API call from 1.8 seconds to 250–500ms.
• Significantly improved developer experience and code maintainability by consolidating logic in the GraphQL layer.
• Decommissioned direct SOAP API usage for several major applications.
• Moved away from costly on-prem IBM systems to our AKS-based cloud platform, reducing licensing and operational overhead.
• Created a centralized, autoscaling GraphQL platform that became the preferred integration layer for future features and teams.

⸻

GROWTH & LESSONS LEARNED

Technical Growth
• Deepened my understanding of GraphQL federation, API gateway patterns, and the tradeoffs between BFF vs federation in system design.
• Learned how to measure and resolve performance bottlenecks via:
• DataLoader
• Caching layers
• Parallel resolver strategies
• Gained a better sense of when to use SQL vs NoSQL:
• SQL for relational, structured internal data.
• NoSQL for unstructured, flexible external API payloads.
• Improved my ability to pitch architectural solutions by breaking them down into phased deliverables and measurable impact.

Non-Technical Growth
• Learned to prioritize iteration over perfection—shipping small but valuable features early helps drive alignment and momentum.
• Developed discipline in time-boxing problem solving and breaking down complex systems into smaller, testable components.
• Found that pairing with others and building fast PoCs was the fastest way to validate assumptions.
• Sharpened my communication—learning to be succinct, to identify what matters most to stakeholders, and to let go of ancillary detail when needed.

⸻

CHALLENGES

Technical
• Over-fetching and repeated resolver calls caused performance issues initially. We resolved this by using the DataLoader pattern.
• Some third-party vendors had unusual state handling which required custom integration logic.
• Initially placed too much business logic in the GraphQL gateway, which created tight coupling; we later refactored that logic closer to the data layer.

Non-Technical
• Stakeholders struggled to see early business value. We adjusted by providing iterative demos and visualizing impact in real time (latency drops, service migration maps).
• Onboarding new engineers during the project was tough. I invested time in pairing and documenting flows to accelerate ramp-up while maintaining quality.
• Vendor communications sometimes stalled due to unclear requirements, so I led with high-level use cases and clear timelines to align expectations.

⸻

CROSS-FUNCTIONAL COLLABORATION
• Collaborated with Solution Architects to align on technical direction and dependency sequencing.
• Worked with frontend teams and product owners to prioritize consumer features and ensure they could move quickly on the new platform.
• Partnered with vendors to map legacy services into subgraphs and define SLAs.
• Engaged with internal tooling teams to standardize observability, logging, and authentication strategies across subgraphs.
• Used a consumer-first prioritization model: started with the highest-impact consumers, delivered their required features first, then expanded scope incrementally across other teams.

⸻

WRAP-UP

This project gave me an opportunity to lead a meaningful platform transformation with strong technical depth, cross-team collaboration, and clear business outcomes. It taught me that delivering architectural change is as much about communication and iteration as it is about technical design. I’d be excited to bring that same mindset to Shopify—building resilient, modern systems while staying close to what unlocks value for the business.

⸻

Let me know if you’d like help making this into a bullet-form cheat sheet for the live interview, or help sketching a diagram to explain the architecture!
