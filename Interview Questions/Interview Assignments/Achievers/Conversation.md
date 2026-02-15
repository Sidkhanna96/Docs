- Software Engineering for one of our Platform Services teams. Jason will share more about the role, the team, and Achievers. You will also have a chance to ask questions related to those topics.

- Achievers:

  - What is it that excites you about achievers ?
  - How are you evaluating a successful candidate to join your team ?
  - Do you see alot of your engineers working within the company growing ?
  - How would you describe the environment within the company ?

- In terms of the behavioral questions, some of the key skills we are looking for are related to problem-solving, communication, teamwork, and coaching/mentoring fellow less experienced Engineers.

  - Problem Solving:
    - New Codebase try to find the pattern of the file
    - have it run - print something in the console
    - Ask people questions
    - understand the product
    - if new technology
      - try to break it down into smallest achievable components
      - timebox myself
      - reach out if confused
      - watch 30 min youtube video OR read article
      - Nowdays mostly ask chatGPT and be purposeful with how I construct my questions
  - Mentoring:

    - It depends largely on the person and where they're in their career
    - Go over the tech stack and the infrastructure
    - Break down the epic find the smallest component of a story and then incrementally get them to work on it - giving them overview and specific steps or outline and then letting them have a open 2 way communication
    - Example:

      - Belinda

        - SAR:
          - New Intern - we didn't know we will have one this year so surprise
          - I took the responsibility of understanding what she is curious about learning -> Then having a session for going over the basics of programming, our product and infrastructure. Then finding something that is not an immediate deadline, something in our tech debt - broke it down into the simplest step walked her through how to run the application AND then
          - Result of this is she is enjoying, likes to come at work, asks questions and is not afraid and is growing as an engineer

      - Francois
        - Someone who has mostly stayed on the SRE side and has not coded especially in nodejs
        - So I was leading this project of getting this BFF running
        - I pair programmed with the engineer broke the epic down into smallest steps gave him resources spoecific to his problem to reference to
        - Result of this is he was more comfortable with the new stack and started to give output in regular capacity
      - Karchie
        - So we have a developer who was not getting her work done on time and there were concerns from the manager in terms of work not being done
        - So I took her under my quarter deliverable - understood what she was curious about and where she felt underconfident - So she felt like she was missing alot of peaces in the entire full stack and couldn't focus on one part at a time, Then based on the work we had in the epic, I assigned to her work for backend primarily - since I knew she had put some previous effort in froentend- once she got comfortable with owning and entire peace of a puzzle to make her familiarize the entire breadth of the process
        - she felt more confident and is now 90% of owning an entire epic and me being her mentor throughout the process

- On the technical side, Jason and you will go over your professional history; you might be asked to provide more detail around any relevant projects and in particular how you have used specific tools/languages/frameworks (e.g., Go/Python/PHP/databases/cloud).
  - GraphQL backend engine
    - Alot of SOAP services, difficult to add business logic or new endpoints and underperformant application
    - I co-designed the backend engine in graphql - decided what technology to go with, the backend architecture what data sources
    - result of this was able migrate to a new service which improved performance from 1.5 seconds to under 500 ms
  - Member Search - Landing Page
    - Landing Page for our replatform initiative - stakeholder wanted a freeform search box
    - So I did some poc and investigation evaluated stakeholders requirement - they also wanted consistency - but since our datalake was 24 hours behind and our database was SQL there was no direct way to leverage Azure Cognitive search NOR Elastic Search with inverted index - alot of data for query would be massive and would be expensive underperformant calls with large payloads with massive amounts of usage of our DB resources
    - Result I re-evaluated the UI/UX experience - did some caching where reasonable, along with pagination - which coerced users to enter parameters which reduced the number of tables to search and deliver product on time and develop a feature appropriately once our infrastructure was up to date
  - Entitlement:
    - We had a excel type document being parsed as our entitlement rules logic system that we were paying 300k in licensing
    - Developed an internal tool, did data modelling, created RFC and then designed a tool with user testing to implement product
    - No production deployment or involvement of engineer, 10 min implementation of business rules engine and saved 300k per year
  - AKS Basics
    - Helm to package and deploy Kubernetes manifests
    - Jenkins to run the Helm charts and deploy to our Azure env
    - Terraform to provision resources
    - Istio to manage service mesh networking (traffic routing, security, observability)
    - Azure Cluster owns all of similar applications using similar resources
      - Isolated by namespace and resource quotas
