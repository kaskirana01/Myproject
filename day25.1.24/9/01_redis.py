import redis

# 链接redis
r = redis.StrictRedis(host ='localhost', port= 6379 ,password='password')

# 设置键值对
r.set('放假','下午两点考完试你就走')
data = r.get('放假')
print(data.decode('utf-8'))

# 方式2
pipe = r.pipeline()
pipe.set('a',100)
pipe.set('bb',20)
print(pipe.get('a'))
pipe.execute()

print(r.get('a'))