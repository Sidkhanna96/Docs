# ToDo:

- Donne Martin System Design
- Hello Interview System Design - Covers top k and geolocation
  - Ad Click Aggregator
  - Live Chat

# Curious:

- Deep dive - Satisfy NFR - Is this LB / Multiple instances ?
- Core concepts - Indexing, Protocol, locking - No sharding / Federation ?
- Key technologies and tools ?
- API Design ? DB and Schema Design ? Common AWS technologies ?
- Message Queue structure
- Protocol structure
- Websockets vs HTTPs - Stateful vs stateless
- JWT vs session cookie storage
- fan out on read and fan out on write ?
- Should you call out cache and message queue - in deep dive vs HLD ?
- Fanout ?
- consistent hashing - Circular organization of the databases/servers and the clocking the resources on the clock and moving to the destination closest to the destination
- How do we handle locks ?
- gRPC when to use ?
- inverted index
- DB - optimization of faster retrieval and scaling
- replication of data vs scaling or having multiple shards - can you shard and replicate data is it common ?

# Section 1:

## Chapter 1:

### System / Product Design:

- **Product**: Design a system (Ride Sharing services, Chat application, Design Facebook)
- **Infrastructure**: Design a Rate Limiter, Design a key value store - Durability and Consensus Algorithms
- **OOD/OOP**: SOLID -> Describe Class structure of a parking lot system

### Mindset/Approach:

- Break the problem down into smaller pieces - tackle the important pieces
  - Solve Smaller pieces with **Core Concepts**
  - Recognizing common technologies and applying them
- Move forward when you're stuck
- Don't be defensive on feedback - work with interviewer to solve the problem

## Chapter 2:

- **Requirements**: API Design, DB and Schema design, AWS technologies
- **Core concepts** - Helps solve smaller pieces: Indexing, locking, consistency, Security, Server Protocol - Websockets, REST, SSE
- **Common Technologies**: Like AWS / EKS - stack / serverless, Blob Storage, Queues -> Message Queue, Streams, Cache, CDN

- 10 main categories of problem - in Section 2

# Section 2

## Delivery Framework

![alt text](image-1.png)

- Requirements
  - Functional Requirements - top 3 Most important:
    - Users is able to ?
  - Non Functional Requirements - top 3 relevant:
    - System should be ?
      1. CAP - Consistency vs Availability
      2. Env - memory limit to deal with, device is mobile, low internet connection
      3. Scalability / throughput - Burst traffic, Read vs Write
      4. Latency
      5. Durability - ACID vs BASE - TCP / UDP
      6. Security - entitlement / Authentication
      7. Fault tolerance - Failover, recovery mechanism
      8. Compliance - Data protection and other regulations
  - Capacity Estimation
    - Avoid it - call it out if necessary
- Core Entities:
  - different entities in system - (Not data models) - User, tweet, follow example - What all actors and what are the nouns
- Core system:
  - Core entities that your system will exchange and data models will persist (Essentially what data is being moved around - think user, tweets, follow, followers) - bullet this - What actors in the system
- **API System/Interface**
  - REST vs GraphQL - Go REST - explain graphQL
  - Wire Protocol - Websockets vs TCP vs UDP - define the wire protocol
  - HTTP - is traditional req - res model - TCP - stateless
  - Websockets Two way communication between client and server model - TCP (simultaneous data exchange) - Stateful, authentication mechanism
    ![alt text](image-2.png)
- Data Flow ??? - 13 ish minutes till here
- **High Level Design** - 10-15 mins here:
  - Key technologies
  - Drawing boxes and different layer of your system to interact with each other (Servers, DB and Caches)
    ![alt text](image-3.png)
  - Be explicit with how data flows
    - Request and response for each api
    - log the columns that are going to be populated in DB with each request
    - Build from one api to next api one by one
      ![alt text](image-4.png)

## Core Concepts

### Scaling:

- Throughput - # of users per minute
- Vertical vs Horizontal:

  - Vertical - Adding more resources - CPU / memory, If capacity estimation dictates you could add more resources, and reduce complexity of horizontal
  - Horizontal - Adding more machines, Need to tackle distribution of workload and data - Consistent Hashing tackles this

- Horizontal:

  - Work distribution: Selecting which node to use for an incoming request for server Load Balancer - round robin/consistent hashing/for asynchrnous jobs through queueing system - multiple instances
  - Data distribution:
    - Distribute data across the system:
      - Keeping data in memory
      - Keeping data in a DB thats shared across all nodes
        - Sharding - shard nodes based on userId - serving a subset of userIds and then let them keep the cache locality
        - eliminate joins by designing schema
        - denormalization - duplicating data across multiple servers
      - When a service needs to talk to multiple services it leads to fanout since dependency on all downstream services (Higher risk and failure)
        - More sensitive to failures and alot of network traffic if need to talk to bunch of nodes through scatter gather pattern
    - Race conditions and consistency of data issues to tackle in horizontal

### CAP Theorem:

- Consistency vs Availability:
  - Availability should be default
  - Consistency:
    - all DB server nodes will see the same data at the same time, When a write occurs all subsequent reads will have the same response
    - some DB nodes may become unavailable to maintain this consistency
    - Example: Inventory Management - stock levels need to be precisely tracked, Booking system with limited availability of seats, Banking system - keeping consistent data across all nodes to prevent fraud
  - Availability:
    - different nodes can have different values temporarily while they're being inconsistent

### Locking

- Locking is one client can access the shared resource at a time (- inventory units)

  - Important for enforcing correctness but bad for performance - Race condition other resources cannot access DB because other users is using it - this can lead to data loss and corruption

- 3 things to worry about for locking:
  - **Granularity**: Only lock as little as possible - only lock the user whose information is updated not the table.
  - **Duration of the lock**: Only lock for small time as needed - so lock user profile update for duration of update not the entire request of requesting the update
  - **Bypass the lock**:
    - ![alt text](image-5.png)
      - You are trying to update the data in DB - you read the specific row - and its associated version number - then you make your changes and then try to apply the change and if no new version great if a new version exist then you do a retry to throw error

### Indexing

- indexing data by keys for fast retrieval - through hashmap or B-Tree
- We can also sort the data based on key and then do a binary search

### Database:

- Can create indexes on any column or group of columns
- geospatial indexes - index location based data - for finding nearest restaurant or uber
- vector database - high dimensional data - similar images or similar documents
- full text indexes - index text data - search for documents or search for tweets
  - PostgresSQL has all these indexes
- Secondary Indexes - like geospatial, full text, vector - leveraged by Elastic Search for faster querying of non primary key columns - whatever is added to primary database it is captured by change data capture for faster secondary querying - it does add extra latency and point of failure

### Communication Protocol

- 90% of communication through HTTPs / gRPC internally
- externally - HTTPs, long polling, Websockets, SSE

![alt text](image-7.png)

- HTTP(s) - req/res - stateless request. The services should not depend on the state of the client like sessions
- long polling - client sends request and the server holds the request until it has new data to respond to the client to - this keeps repeating
- websockets - real time bidirectional communication between client and server - since can be taxxing on firewall and load balancer to maintain these long many open connections - a message broker is added in the middle of the websocket client and server - to communicate with this message broker - no need for long connection in your backend
- SSE - send updates from the server to client - unidirectional; Single long lived HTTP request through which the server sends repeated updates whenever new data is available

(Message Queue)
![alt text](image-8.png)

### Security

- Authentication/Authorization
  - API Gateway or Auth0 for authorization is enough
- Encryption:
  - Protect data in transit (Protocol) and data at rest (Storage encryption) - Transit - SSL/TLS protocol for encryption of data - DB that supports encryption
    ![alt text](image-9.png)
- Data Protection:
  - protection from unauthorized - access, use or disclosure - Rate limiting and throttling - since alot of data can be exposed through non-conventional endpoints and those are found through scraping

### Monitoring

- Infra monitoring - health and performance of the system - CPU / memory usage / disk usage and network usage - New Relic
- Service Level Monitoring - health and performance of the service - request latency, error rates and throughput
- Application Level Monitoring - health and performance of application - # of users, # of active sessions, # of active connection - key business metrics - google/adobe analytics

## Key Technologies

### Core Database:

- SQL (Postgres / MySQL)
- NoSQL (Mongo / Dynamo)
- illustrate why you're using a db as opposed to comparing one over the other

RDMS:

- default but ACID and transactional along with many ways to optimize and scale them

  - Sharding

- SQL Joins:
  - arbitary joins between tables - but performance bottleneck - minimize wherever possible
- indexes - faster querying
  - implemented through B-Tree OR hash table
  - many indexes in RDBMS
  - multi column indexes
  - specialized indexes (Geosptaial, full text)
- RDBMS transaction:
  - Grouping multiple operations into one transaction - so that you don't have invalid data if one of the transaction fails - if one fails all fails.

NoSQL:

- unstructured data and handle large volumes of it
- scale horizontally easily
- 4 types- key value, document, column and graph
  ![alt text](image-10.png)

- When to use ?
  - store different types of data structures without fixed schema
  - scalability of high user data and high user loads
  - real time data processing of high volumes of data that is unstructured
- Note:

  - SQL can also have json data with flexible schema in columns
  - SQL can horizontally scale with right architecture
  - Talk about why you would use a given DB as opposed to why not you would use another DB

- Consistency Models - NoSQL offers strong to eventual consistency range of models.
- indexing - supports it through B-Tree and Hash Table
- Scalability is done through consistent hashin or sharding

### Blob Storage

- Amazon s3 - stores files, videos and images - traditional DB could be expensive
- you get back a URL for data stored
- blob storage services work in conjunction with CDN - so faster retrievel, CDN is reverse proxy that serve static data and have world around network.
- SQL will have pointers to the images the URLs

Traditional architecture:

![alt text](image-11.png)

**Upload**:

- ask server for presigned URL, server records the presigned URL in DB
- client uploads to presigned URL - Blob storage triggers notification that the status is updated

**Download**:

- client request specific file and are returned its presigned URL
- presigned URL is used via CDN - which proxies the request to the underlying blob storage

**About blob storage:**

- Extremely durable - replication for making sure data is safe
- highly scalable
- cost effective
- secure - encryption at rest and in transit - access control features of who can access your data
- upload and download directly from client - presigned URLs grant temporary access to blob
- chunking - multipart upload API in S3 - chunking the file in smaller pieces - resume upload if fails partways and upload files in parallel

### Search Optimized Database:

When searching texts or events etc.

- SQL - LIKE statement is inefficient
- search optimized db - use tokenization, stemming and indexxing to make search queries fast and efficient -> inverted indexes (Words to documents that contain them)

**Things to know:**

- Inverted indexes - make search queries fast and efficient - maps from words to documents that contain them
- Tokenization - breaking piece of text into invidual words - mapping word to documents
- Stemming - reducing words to their root form - matching different forms of the same word - running/runs -> run
- fuzzy search - similar to a given search term - slight misspelling -> Algoirthms like edit distance

Elasticseearch

### API Gateway

- Redirects the request from client to the associated microservice
- Provides - authentication, rate limiting and logging (Apigee)

### Load Balancer

- Client -> Gateway -> LB -> Service
- L4 - for persistent sessions like websockets use L4 otherwise even for sticky sessions L7

### Queue

- handles bursty traffic the server sends message to the queue and forgets about it. pool of workers on the other end processes the messages on their own pace.
- Queue break the latency requirements - but provide ability to individually scale servers

Use Cases:

- Buffer for Bursty Traffic - Ride sharing
- Distribute work across a system - distribute expensive image processing task - worker nodes pull task from queue

![alt text](image-12.png)

Things to know:

- **Message Ordering** - FIFO, priority or time based
- **Retry mechanism** - you can configure retry mechanism - delay between and max # of attempts
- **dead letter queues** - store messages that cannot be processed
- **scaling with partitions** - Queues can be partitioned across multiple servers. Each partition processed by a different set of workers. like DB need to specify partition key to ensure that related messages are stored in the same partition
- **backpressure** - sometimes adding a queue obscures the problem - if receiving 300 request as opposed to 200 queue will always be full and we need to scale the server in this instance queue in a way a bottleneck. With backpressure if a queue is full you reject messages to slow down the rate at which new messages are accepted

kafka

### Streams / Event Sourcing:

- Real time processing of data OR event sourcing (changes in applications are stored as sequence of event - can playback these events to reconstruct the transaction state at any point in time)

- Stream retain data for a configurable period of time (Unlike message queues) - allowing consumers to re-read messages from specific time.

Use Cases:

- **Processing large amount of data in real time** - real time analytics of user engagements (Like, comments shares) or posts -> Stream to ingest high volumes of engagement events generated by users across the globe
- **event sourcing** - banking every transaction needs to be recorded - stream like kafka event sourcing - each transaction is an event that can be stored, processed and replayed. Allows real-time processing, audit transaction, rollback changes and reconstruct the state of any account
- **multiple consumers reading from same stream** - real time chat applications - when user sends a message its published to a stream associated with the chat room. Stream acts as a centralized channel where each participant receives the message simultaneously - allowing for real time communication. **pub-sub pattern**

Things to know:

- scaling - can scale across multiple servers like db you need partition key
- multiple consumer groups - allows different consumers to read from the same stream independently - processing same data in different way - one group stores in dashboard another stores it in db
- replication - can replicate data across multiple servers
- windowing - grouping events together based on time or count - process events in batches (Hourly or daily aggregates of data)

kafka

### Distributed Lock

- ticketMaster lock a ticket for 10 mins
- lock somthing across different systems for an extending period of time
- Redix or Zookeeper - distributed key value store - use the atomicity of KV store to lock a ticket-123 to status locked - they're also timed to expire

Use Cases:

- e-commerce checkout, locking driver of uber to the customer so no one else can get the driver, auction bidding system, CRON Job - task executed by only one server at a time - prevent duplication of a given task across multiple servers

Things to Know:

- **Locking Mechanism**: Redlock mechanism on redis - multiple redis instances ensure the lock is acquired and released in a safe and consistent manner
- **Lock Expiry**: locks expire in certain amount of time
- **Locking granularity**: lock single or group of resources (multiple ticketts)
- **Deadlocks**: if process tries to get lock on a and then b and another gets a lock on b and trying a - both waiting for lock on a and b respectively, to prevent this lock expiry is a common way to tackle

### Distributed Cache

- expensive to compute data or frequently used data - save it in memory through cache

Use Cases:

- Save aggregated metrics: when creating dashboard and storing the data in multiple sources the calculation could be expensive on the system so store this data in cache
- Reduce number of DB queries: user sessions are stored in cache
- speed up expensive queries: twitter follower posts stored in cache since complex query to fetch all posts from all user following - multiple table joins

Things to know:

- **eviction policy**: which items are removed from the cache
  - LRU: least recently used
  - FIFO: evicts in order added
  - LFU: Removes items that are least frequently used
- **Cache Invalidation**: data in cache is up to date - if venue of event changes delete it from your cache
- **Cache write strategy**: data written in cache in a consistent way
  - Write through cache - write to both cache and DB - ensures consistency but slower write operations
  - write around cache: bypassing and storing data in DB - read times for data fetch increase, reduces cache pollution
  - Write Back Cache: Writes data to the cache and then async writes the data to the datastore through the cache. Faster for write operations but can lead to data loss if cache is not persisted on disk - since cache can be volatile
  - modern cache store more the KV stores - can also store data in sorted list for example, exemplify what type of data structure to store in cache

Redis

### CDN:

- CDN type of cache - dsitributed servers and delivers content closest to the geographic location - serve static content like images, videos and HTML files
- check CDN cache for content if not on CDN then serve from origin and then store it in cache

Things to know:

- CDN - can also store dynamic content - normally not
- CDN can be used to cache API response - if API is used frequently store responses in cache
- Eviction policies - TTL on CDN or cache invalidaation strategy
