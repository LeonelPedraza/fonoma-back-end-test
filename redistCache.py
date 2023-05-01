import redis

r = redis.Redis(
  host='redis-14547.c283.us-east-1-4.ec2.cloud.redislabs.com',
  port=14547,
  password='EAAdTZ2DjO6Re9vqRZrRMdUJKPepqet0')

def setCache(total_price: float):
  return r.set(total_price, total_price) 
  
def getCache(total_price: float):
  cache = r.get(total_price)
  if cache:
    return cache
  return None