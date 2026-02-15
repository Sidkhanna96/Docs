- Google Maps
- Ad click Aggregator
- Live Comments
- Confluence same time editing
- Why cassandra

- Common Scaling techniques - Scaling higher throughput ? DB / Server / Async

  - More Servers and DBs - Replication
  - Separate Servers
  - Async for bursty traffic like Message Queue
  - DB:
    - Sharding
    - Federation
    - Denormalization

- Common Latency techniques ?

  - Indexing
  - Caching
  - CDN

- Common Consistency techniques ?

  - SQL DB
  - Optimistic Locks
  - Distributed Locks

- General downsides:

  - Service not being available and not having those features
  - Point of failure new - adds complexity with new component
  - CDN is expensive

- General - CDN, S3 storage - segmentation, replication, precomputation (Through storing data in a redis cache)

## Design URL Shortner - like Bit.ly

// Global Counter

- Dynamo DB - NoSQL (Can also pick SQL since not heavy/reads or writes) - data seems non-relational mostly and suspect higher traffic fluctuations. 5k RPS for SQL 10k RPS NoSQL (5x and 10x spike respectively)
- **Making shorten URL unique:**
  - Global counter in Redis -> INCR opern Single threaded and Atomic -> hence no race conditions and locking of the data
- **Fast Redirects:**
  - Another Redis DB which will have the used data and write server will access
  - Cache Invalidation through TTL, Cache Eviction through LRU, Cache write through strategy
- **Scaling for High throughput:**
  - Separate Read/Write Servers - each handling its own load -> Read is higher throughput than write
  - Replication of Reads - autoscaler
  - Partition of DB through shorten URL since unique range of Ids would access the said URLs

## Design Dropbox:

// S3 Blob Storage, Sync - WatchEvents/Polling, Chunking, New Table for sharing a file as opposed to searching entire table of pre-existing files

- DynamoDB - Availability and non relational data
- Amazon S3
  - Upload - directly upload to presignedURL
  - Download - get the presignedURL OR download it from the CDN Cache -> Invalidation - through edit/delete of files delete in CDN, TTL through cache-control header
- Sharing a file
  - Rather then adding to pre-existing file table which leads to parsing the entire table to see which files the user has access to we create a share table with the userId and the associatef fileId
- Sync files
  - FSWatcheEvents and FileWatchSystem for any local changes and then queue to be uploaded
  - Polling for files that are stale and, fresh file we can have a websocket connection and pushes events to the client
- Large Files:
  - chunking of files -> Client breaks the files and passes the metadata, then does upload to presignedURL
  - once chunk uplaoded the status is updated through s3 notification
  - fingerprint of each chunk -> hash sha256 of the content of file
- Fast upload/download/sync:
  - CDN, Chunk, PresignedURL
  - Compression Algorithm on text contents.
- Security:
  - Transit HTTPS
  - REST - S3 Encryption
  - Access Control through Sharelist -> PresignedURL have TTL, and signature containing the IP and URL Path

## Design TicketMaster:

// Separate service - View, Search, Book; Queue + Websocket; Elastic Search; Distributed Lock

- PostgreSQL - Consistency
- Separate services -> View, Search, Book events (Stripe for payment processing)
- Booking Experience - SQL only maintains the lock for the request entering information and its gone
  - Redis Distributed Lock with TTL - Check Redis to see if there is a lock on the seat if it is its not available
- Scaling view:
  - Caching, Horizontal scaling of the API
- Scaling Booking:
  - SSE -> unavailable and available pretty quick
  - Queue + Websocket -> Create websocket connection with the client on the queue and dequeue to proceed
- Improve Search:
  - PostgresSQL -> full text search based on indexing of the column -> Slower to query than standard indexes
  - Elastic Search -> CDC -> Excellent for searching -> Inverted index full text search
- Reduce load on search infra for repeated queries:
  - Redis
  - LRU caching abilities in elastic

## Facebok News Feed:

// DynamoDB since availability; Feed Table (Fanout) -> Precompute the result on POST; Async Workers; POST Cache with replication on shard

- Post/Follow/feed Service - Post/Follow/Post Table
  - If fetch people you follow and then all the people you follow find their posts and its too large this is very inefficient
- Page through feed:
  - Feed cache -> TTL with chronological order of top 500 posts then when request next we fetch the next set from the timestamp
- Large Number of users following:
  - Fanout of fetching followers and then their posts
  - Feed Table -> Shard it based on userId - on POST of posts - we call feed service which precomputes the top 200 postIds for all the people following the poster
- Large Number of followers:
  - Async workers - each worker will prepend the followers of the poster and add the post to the feed table for the follower
  - For large accounts we flag it and don't use the Async workers and do a hybrid query
- Uneven post read for users with massive followers -> Keep hitting the Post Table for getting the same result ?
  - We can add post cache with LRU and TTL - Eviction and Invalidation policy -> Issue same partitioning/sharding issue - where some shards and partitions will get higher throughput
  - Replication on those shards

## Design WhatsApp:

// Pub/Sub - different from kafka and event stream topic; Websocket connection; Sync - but on different clients - sending messages and receiving messages

- DynamoDB - For availability
- Group Chat <= 100 -> Chat / ChatParticipant Table:
  - Participants of a group chat -> index based on chatId
  - Group Chats user is part of -> Global Secondary Index -> partition on participantId sort by chatId
- Send/Receive when not online for 30 days:
  - Messages Table (Inbox - recipientId/messageId, Message):
    - if websocket connection there send the messages from Inbox -> Client sends ack
    - if websocket connection not there - when user logs in we pull from inbox
- S3 Blob Storage - Media
- Billions of simultaneous users -> In chat Server multiple replication - websocket connection to different replication might not send the the data to online users
  - Pub/Sub stream Redis (NOT KAFKA)-> userId has a subscription created - any messages received on the subscription are passed to associated websocket
  - When chat servers send messages all the message is received by all subscribing chat servers and the messaeg is forwarded from here
- Multiple clients -
  - Clients Table - if client is online just send messages to all associated clients for the given device - they will subscribe to a specific topic

## Design Leetcode:

// Docker container, Scaling -> Async Queue -> Need to poll the DB continuously

- DynamoDB for availability -> and we don't need complex queries
- Testcases within the data structure
- Run code in docker container
- Security -> CPU / Memory Threshold, Timeout, Disable any network access, readonly for the file/folder, seccomp configuration in docker for preventing system calls
- Live leaderboard:
  - Making request to DB will put massive load on it - Periodic polling 5s
  - We can have Redis Sorted set list - Periodic polling
- Scaling -> Horizontal scaling w/t Queue:
  - this way we don't prematurely create a lot of containers -> req/res is going to be async -> Need consistent polling
    - Websocket can work for constant checking but adds complexity

## Uber:

// Redis Location DB - geohashing for constant polling; Redis Lock for locking the driver

- PostgresSQL for relational DB
- Ride Service / Location Service / Ride Matching Service
- Google maps for estimating distance
- Driver Location updates:
  - Continuously polling their location and update to DB -> Heavy updates on DB
  - Redis Location DB - Geohashing the data - saved as a single string easier to find the proximity - GEOADD/GEOSEARCH
  - Frequent overload - Adaptive Location updates - speed, direction
  - We can also have a Websocket connection for the driver sending the requests especially when driving
- Multiple Ride Requests:
  - Redis Distributed Lock (Having a DB reqiures TTL on the API Server which if API crashes the server dies)
- No Rides are dropped during peak demands:
  - Queue between the ride service and ride matching service
- Further scaling:
  - Read replica / Horizontal scaling
  - Sharding the DB based on the geohash

## Youtube

// Chunking - Uploads; PostComputation - segmentation - transcoding - manifest files for video chunks Download; Adaptive Bitrate Streaming - for variable network conditions

- Video Codec - FFMPEG -> transcode video into other formats
- Bitrate -> Number of bits sent per second -> lower quality formats sent for lower bit rate
- Manifest Files -> metadata for the segmented videos - i.e. format

- Uploading Videos -> Chunking -> S3
  -> Store it as segments of different format
- Users can watch videos:
  -> Adaptive Bitrate Streaming - Clients run an algorithm based on network conditions
  -> Use the segments of videos to download based on format and then line up other segments for download
- Processing videos using adaptive bitrate streaming
  - FFMPEG for splitting up files and transcoding to different formats (done in postcomputation)
  - Do any other process aspects on segments (transcript, audio) (Can be done in parallel)
  - Create manifest files referencing different segments in different video formats
- Resumable uploads
  - Chunking
- Scale to large number of videos watched every day
  - Shard Dynamo based on video Id for videoMetadata -> If video gets hot make replication of the shard partition -> Add Cache for further LRU processing
  - horizontally scale the service apis
  - Add CDN for frequently watched videos

## Tinder

// Geohashing - Redis for nearby people (ElasticSearch) ; Separate Swipe and Profile DB; Redis Precomputation for generating new set of matches and look at the profile db for filtering out any users

- Cassandra - Write Heavy, easy to query single partition
- Separate Profile/Feed w/t Swipe - Swipe is more often
- APN and FCM - for notification service
- For Consistent Matching:
  - Redis - key:value -> key of 2 users in sorted and value is answer for each user
- Low latency for feed stack - Especially geospatial DB:
  - Search optimized DB like elasticsearch
  - Add Cache - Precomputation for users preferences to fetch cached profile data
- Filter out matches that have been already swiped on:
  - Client stores the swipe data too (Along with the swipe DB) - in client side cache
  - When approaching the end of the swipe - ping backend for generating a new set of cache in backend

## GoPuff

// Serializable - all orders within POSTGRESQL if out of quantity; Travel Time estimation service to further filter out DCs

- DC Table -> NearbyService -> Item Table and Inventory Table are then queried based on the dc table Ids
  - We could also do elastic search on CDC and search those tables based on geohash
- Ordering Table (PostgresSQL) -> Atomic -> Serializable if a single product does not exist or is out of stock entire transaction is cancelled
- Incorporate Traffic - search DC Table by 60 mins distance - then use a Travel Time estimation service to further filter out DCs
- Availability lookups faster - Read replica of the PostgresSQL db and partition by region id

---

## Yelp

## Strava

// Uber, Whatsapp, FB live comments - Real time data sharing

## FB Live Comments

// Cursor - for Last N comments; Pub/Sub

- DynamoDB - Availability
- New Comments posted while watching video:
  - Polling with since parameter to fetch all comments that were posted since the comment
  - Not instantaneous, if increase polling and there are more users - the DB won't be able to keep up with demand (10k - 15k max)
    - replication has issues since if someone comments on DB1 and another user is routed to another DB2 instance they won't see the comments since its eventual consistency
    - partitioning of say by videoId would only still support only 10k - 15k max rps and other videos are still there
- Viewers can see comments before they joined the feed (Infinite scrolling):
  - Offset Pagination - inefficient - comments grow - the DB would need to parse through all rows preceeding the offset to get the list of comments needed
  - Cursor - starting point for fetching a set of results (Unique Id to fetch set of results - initially most recent comment). As user scrolls above the unique Id keeps updating for cursor. This way the DB does not need to parse through all comment index preceeding it like in offset to find a point. Instead we can point to a given commentId and go through comments that were posted before it!
- Real time broadcast:

  - Websockets - Sends data to the client without additional requests automatically from the comment management system - Read to Write ratio is higher though
  - SSE - Client sends comments through API requests, But SSE is a persistent connection that the server sends to the client. (Lack of LB support though and only select connection from browser so only few videos)

- ## How will system scale to support millions of concurrent viewers:

# FB Post Search

# Instagram

# Youtube top K

// Dictionary, Heap, Snapshots, Replication, Sharding

- Count on videos and Videos uploaded
- Have a heap and dictionary count to keep track of the top and the total counts respectively, kafka view stream is where we read from the video source
- System Failures:
  - Replication + Snapshot
  - Replicate data across multiple hosts
  - Store snapshot in blob storage (Once all replications have snapshot we can delete the previous snapshots)
- Scale Write Throughput - Writing 100ks of counts per second:
  - Sharding - through consistent hashing through zookeeper by videoId partitioning - Elastic partitioning
- Maintain Time window
  - ???????????????????????????

# Google Docs

// Operation Transformation (OT), Cassandra append only, Zookeeper and consistent hashing, Snapshots

- Document Service to store metadata of the doc
- Another Document Service that stores all the OT into Document Operations DB
- When Document is loaded - send all previous operations when the document is loaded
- When update happens - Apply OT on the client side - since it takes sequence of order and rewrites them in a consistent way
- See the cursor - just on change of position send the curosor position to the document service and it will store it in memory
- Scaling to millions of websocket connections - Zookeeper and consistent hashing
- Storage under control
  - Snapshots of the document with documentversionId in metadata and operations DB
  - take snapshots when all users disconnect

# Robinhood

# Web Crawler

# Ad Click Aggregator
