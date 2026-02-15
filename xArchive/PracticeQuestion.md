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

## Design URL Shortner - like Bit.ly

- Can take any DB -> Would say NoSQL since can handle heavy read/write like dynamo
  - In our use case RDBMS - 5k R/W per second with 5x spike - so can be leveraged!
  - NoSQL - 10k R/W per second with 10x spike - so much more resilient for even higher read write workload
- Unique -> Redis INCRBY -> Global Counter that can track the number for unique code generation with Base62 encoding (Since 64 has special character)
- Redirects fast -> Redis DB for storing the LRU Invalidation strategy to fetch the URL from DB and store in Redis for faster reads -> 1000 times faster than SSD
- Scale for Read and Write to DB:
  - Write and Read service separation - Write don't need much scaling so can be scaled if needed through replication!
    - Read can also be scaled through replication and since its a separate server it can handle its own set of requests!
  - replication
  - Sharding our database by unique short code for better fetching of read data also does not overwhelm the read aspect on the DB leading to higher scaling and faster reading

## Design Dropbox:

- DynamoDB - Loosely structured data
- Store files in blob storage -> presignedURL for upload and download through CDN
  - Download: CDN expensive need eviction policy like TTL and invalidation policy like delete on upadte/delete and write through policy where data is cached
- Sync files Local->Remote and Remote->Local
  - Local -> Remote -> File watcher like FSEvents and FileSystemWatcher on Windows -> Conflicts are resolved through last write wins
  - Remote -> Local -> Polling for old files and websocket for new files
- Large files:
  - Chunking of the file data on client side sending metadata to the DB and its status and then direct upload to the S3 DB and then s3 send notification through s3 notification that the chunk is uploaded and update the chunk status - we use fingerprint of sha256 hash to uniquely identify the chunks and file
  - When user comeback to resume client pull metadata and see what chunks have been updated and ignore them through fingerprinting and then upload the remaining ones
- Upload, Download and Syncing fast possible:
  - Chunking helps upload and download and sync -> Upload able to resume and shortening the size of file, download CDN improves download speed and also reverse chunking through Streams API in nodejs, and sync based on chunks that have been changed
  - compression algorithm on text - media/video already compressed to be ditributed
- File Security:
  - transit - https
  - rest - S3 configuration for encryption and also key in separate file for encryption
  - access control - presignedURL have expiry + presigned signature + restrictions like IP for no non authorized user downloading

## Design ticketmaster:

- For searching API Design add parameters as query param
- PostgresSQL DB
- separate db for search, event service and booking service
- booking table, ticket table
- Booking service - stripe payment and
  -> since PostgresSQL - we have ACID to prevent double booking across rows (Optimistic concurrency control) for multiple services trying to book the seat and the seat is unavailable - locking
- Booking experience to reserve tickets ->
  - If someone is trying to book a ticket and then before paying someone else books it is not good
  - Distributed lock with redis with TTL of 10 mins
- Viewing events and searching events scale
  - have a cache for common queries LRU
  - horizontal scaling of servers and dbs + LB
- Millions booking tickets simultaneously
  - have a queue -> Group of users can come in - Waiting queues
  - OR SSE -> Which makes the seat instantly unavailable still not the best interface
- Improve Search:
  - Elastic Search
  - Full text search on the indexed db PostgresSQL - can make it slow with additional storage space

## Design Facebooks News Feed

- user follow another user (Many-Many reln)
- DynamoDB - Eventual consistency, data is having high throughput and horizontal scaling is important
  - Post Table -> userId and its posts
    - sharded by userId
  - Follow Table -> userId and follow
    - Sharded/partition key by userId
- View Feed of people you follow
  - Follow Table -> Post Table (Fanout, millions of followers, posts, following)
    -> following large number of users (Fan out to post and follow)
    - Feed Table -> When post written to Post Table we update the feed table of the users following the users and add to postId to the Feed Table
- Large number of followers:
  - When users have large number of followers -> we can have async workers that write to the feed table for normal users with low number of followers
  - For large followers we fetch their posts from the Post Table directly and fetch the rest of the users data from the feed table
- Page through feed
  - First Request of feed -> We cache the data in Feed Cache of 500 and fetch progressive ones from there
- How uneven reads of posts ?
  - Feed Service for populating the Feed Table it fetches data from the Post Table directly and certain partitions of the Post Table the Post Table is sharded by userId so some partitions by a given user will be getting higher traction
    -> We can add a cache for not too much throughput on a given partition on the DynamoDB Post table
    -> To eleviate the cache having the same hotkeys issue we will create replication of the given shard

## Design Whatsapp:

- Every API request send by a client - there is a parallel command send to the other client which responds with an ack (Network response)
- Websocket -> L4 LB -> ChatServer

  - this has a open connection to each client

- Start group chat for 100 user limit:
  - Uses NoSQL Dynamo for high read / write
    - Chat Table - Chat groups
    - ChatParticipant Table - Chatgroups user part of
      - Range lookup on ChatId and participantId will give us limit of 100 users
      - **Seconday Index** participantId as partition key and chatId as sort key. All chats for a given user
- send/receive messages:
  - hashmap that contains userId to websocket connection (All user online and will receive it)
- Send messages when not online:
  - Inbox Table - undelivered messages for each user, if online message immediately - if login we deliver messages
  - Message Table - the actual contents of messages
- For Media:
  - S3 DB - direct db call to blob for upload and download for fast lookup
- Billions of simultaneous users
  - If multiple clients and one of the client is not connected to the same chat server can seem like they're offline
  - Pub/Sub stream - we publish the message to the pub/sub topic for the relevant userId
  - Pub/Sub is at most once - so if user not online they won't receive message from pub/sub - but we manage connectivity of the user through the inbox table also so when they come online they will have the message
- Multiple Clients for a given user - multiple devices
  - Register all clients for a user in a clients table (ClientId/userId)
  - when send message to client that are online i.e. through the pub/sub we send to all the client devices to sync it

## Design Leetcode

- Leaderboard
- NoSQL
  - since no relationship between the data
  - db indexed for pagination
- Code solutions in monaco editor
- Docker container
  - Have a runtime environment for each language
  - then run the code in the container
  - resource limits for each container
- leaderboard
  - coudl partition key by competitionId and view all submissions and calculate in memory every 5 seconds the leaderboard - not a good solution
  - Redis Sorted Set for leaderboard
- Security:
  - Read Only Filesystem - cannot write to filesystem the code, mount directory of code as read only and write any output in temp directory
  - Limit on CPU and memory + explicit timeout on the code from running in infinite loop
  - Network Access disabled to prevent API calls
  - seccomp on docker to prevent sustem calls that could compromise the host system
- Competition:
  - Bursty traffic - leads to Queue
  - Horizontal scaling of docker containers
  - Queue - between api server and the containers - buffer submissions during peak hours
    - ensures we don't loose any submissions during peak time - strong durability
    - API won't return submission immediately - user will need to poll every second by the client to check if the submiision has been processed - `GET /check/:id`
    - you can also introduce persistent connections like webdsockets to avoid polling - adds complexity

## Uber:

API:

    - When getting estimation of fare - Ride Object created in DB
    - When accept ride Fare - initiates ride matching process
    - polling for drivers location continuously - called by driver client - this enables us to match the rides entered into the system to nearby drivers
    - accept rideId

Design:

    - Mapping service to get destination/time
    - DB - contains Fare Calculator object -> Ride Calculator object for requesting
    - We have a location service that sends updates about driver location and also the passenger continuously
        - we can leverage location service that updates location for driver
        - we store the location of the driver in a RedisDB - this enables geohashing of lat/long - which ensures proximity searches and handles frequent location updates of driver - we indexed on the geohashed key
            - Frequent driver location updates:
                - further, can do adaptive location update intervals
                - update location based on contextual factors (Speed, direction, proximity to ride requests) + ondevice sensors to determine optimal interval for sending location updates
    - Lock on driver:
        - when a ride is requested for a driver it checks first redlock distributed lock if the driverId is locked or not if not
        then it sends a 10 second lock for the next passenger to accept the ride or not
    - No Ride is dropped / bursty traffic:
        - queue added infront of the ride sharing service and horizontally scale it based on traffic
    - For higher throughput and latency:
        - shard everything based on geohash - message queue, to SQL DB to Redis DB

## Youtube

video streaming formats:

- video codec
- video container
- bitrate
- manifest files

- Where do store the video data (frames, audio) AND what do we store for video data ?
- Where do we store video Meta data ?
  - 365M videos a year - horizontally scaling videos
  - horizontally partitioned db like cassandra (Wide column store) - videoId partitioned
- we do post processing of videos into smaller chunks and saving it into smaller formats so that it can be viewed and easily watchable
- We store all videos in blob storage, chunking for upload through direct URL and then
- Watching videos:
  - Adaptive bitrate streaming - bitrate is internet connection speed,
  - Manifest file - during video upload references all the video segments that are available in different formats - stored in S3 the url in DB will point to this manifest file
  - client choose video type based on network conditions/user settings. client retrieves the URL for the first segment, play segment and begin downloading the next segment
- How post processing is done: - break file into segments using ffmpeg - transcode (Convert from one form to another format), generate different video containers - create manifest files referencing the different segments in different video formats - mark the upload as complete
  ![alt text](image-13.png)
  The segment processing (transcoding, audio processing, transcription) can be done in parallel on different worker nodes since there's no dependencies between segments and the segments have been "split up". Given the graph of work and the one-way dependencies, the work to be done here can be considered a directed, acyclic graph, or a "DAG."
  Ideally, this work is done with extreme parallelism and on many different computers (and cores), given the CPU-bound nature of converting a video from one codec to another.
  Additionally, for actually orchestrating the work of this DAG, an orchestrator system can be used to handle building the graph of work to be done and assigning worker nodes work at the right time.
  Finally, for any temporary data produced in this pipeline (segments, audio files, etc), S3 can be used to avoid passing files between workers. URLs can be passed around to reference said files.

- Resumable uploads:

  - The client would divide the video file into chunks, each with a fingerprint hash.
  - videoMetadata table would have field called chunks - list of chunk JHSON each with fingerprint of the file chunk hash and the status of the fingerprint upload
  - post this videoMetadata above with everything notuploaded
  - upload each chunk to s3 - s3 would send event notification to a serverless that would update the videoMetadata by marking its chunk as uploaded
  - if video stopped uploading - client can just check if the chunk has been uploaded or not if uploaded skip the chunk

- Scaling of Youtube to watch 100M videos per day and uploading 1M videos per day

  - video service api - horizontally scale it
  - video metadata - caddandra DB horizontally scale - leaderless replication and sharding/partitioning
    - hot video bottleneck
  - Video processing service - have queue to handle bursts in video uploads. Have more worker nodes
  - s3 - scales exxtremely well. mult region and can elastically scale.
    - hot video bottleneck

- hot video:
  - cassandra replicate videometadata to few nodes + Cache LRU partition in videoId as well.
  - CDN cache popular video statically near the network locations. shorter distance

???

- speeding up uplaods
- resume streaming where left off
- view counts

## Tinder

- profile service and match service,
- we could use SQL for fetching the distance based on geo indexed table but it will be inefficient
- We will create a separate swipe and db (Cassandra) service - because that happens far less frequently
  - botec - 20M DAU x 100 swipes/day x 100 bytes per swipe -200GB a day - scale accordingly
  - partition by swiiping user_id - fast query based on querying that single partition of userId on localized caching
    - cassandra is capable for high writes since write optimized storage (It does have eventual consistency)
- When personA swiped weeks ago our swip service will check if they mutually agreed on person B if they did the swipe service will send push notifications through APNS or FCM
- Consistency challenge with Cassandra - swiped at same time
  - we partition the DB based on both sourceId and targetId - this way we can check the same db partition to handle this
  - we can do the same thing with redis cache (recommended), redis is in memory and do same partitioning - consistent hashing too!
- distance filter and relevant matches:
  - using cron jobs run periodically to find the data and store it in a stack cache - doing some pre-computation (Off peak hours)
  - Having a CDC on SQL DB to ElasticSearch -- for real time querying!!
    - indexes on field esp on geospatial data
    - elastic - is fast and can search on complex queries - large volume of read data with minimal latency (Users receive up to date matches) - not optimized for write heavy so need to batch the CDC
    - we combine above 2 - first give them cached data and then fetch from elastic data
      - Stale Feeds - Changed locations / interests
        - TTL of 1hr on cache, we only store data for active users (Since we know they will use it) - and re-compute with background job on schedule
- Avoid showing already swiped previously on:
  - db check not efficient since need to fanout on swipe DB to check for DB (In distributed not all nodes will have this if we have a available DB like cassandra)
  - Client can trigger once the preswipe cached data reaches 150 of 200 data then do another CRON job fetch to fetch from cassandra swip db implication to filter out the users
  - large swip history maintaining in cache could be difficult - have a bloom filter so that easier to find and search a given userId from large sets:
    - set() of swiped users - space effieient probablistic Data structure

## GoPuff

- Leverage latitude and longitude return list of DCs (1 hours distance is not accurate)
- DCs inventory - inventory table and item table - get item name and description before returning with the quantity (Separate table for item and quantity because of workloads)
- Nearby Service on DC DB for nearby DCs which Availability service calls - then the availability service also calls inventory table for the quantity of items
- Locking the DB so that two users don't order the same product
  - adding the orders table to the DB that holds inventory table - leads to locking the table as we can do a singular transaction
    - i.e. entire transaction holds that nothing is added to orders table if inventory is empty
- How to incorporate traffic and drive time:
  - sync the DCs table with in memory of our server since DCs rarely move and are constant lookup time would be fast for the lat/long added - so sync every 5 mins and then prune 60 miles away DCs and then use a Travel Time service to evaluating those DCs for faster lookup and more accuratae
- make availability lookups fast:
  - Redis and Read Replicas
    - Redis store any hits and then we check DB
    - PostgresSQL - partition the DB by region ID the localized memory of the DB will have the regionIds
- how do we find the range of geohash that can help us fetch the lat/lon within our range ?????
