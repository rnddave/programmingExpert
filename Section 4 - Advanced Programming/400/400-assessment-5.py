###################################
# 400.05 - Asynchronous Fetcher
###################################

"""
write a [BatchFetcher] class
- meant to fetch lots of records from a database very quickly

constructor: 
- takes in a [database] object 
- has an [async] method called [async_fetch]
-- this method should take a record identifier [record_id] 
-- returns whatver the database has in storage for that record 

[BatchFetcher]
- should implement the async method [fetch_records]
-- which takes in a list [record_ids]
-- and should return the list of records corresponding to those in [record_ids]
"""
