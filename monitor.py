from apig_sdk import signer
import requests

sig = signer.Signer()
# Set the AK/SK to sign and authenticate the request.
sig.Key = ""
sig.Secret = ""

# The following example shows how to set the request URL and parameters to query a VPC list.
r = signer.HttpRequest("GET", "https://vpc.my-kualalumpur-1.alphaedge.tmone.com.my/v1/{ProjectID}/vpcs?limit=10")
r.headers = {"content-type": "application/json"}
sig.Sign(r)
resp = requests.request(r.method, r.scheme + "://" + r.host + r.uri, headers=r.headers, data=r.body)
print(resp.status_code, resp.reason)
print(resp.content)

# The following example shows how to set the request URL and parameters to query a ECSs list.
r = signer.HttpRequest("GET", "https://ecs.my-kualalumpur-1.alphaedge.tmone.com.my/v2/{ProjectID}/servers")
r.headers = {"content-type": "application/json"}
sig.Sign(r)
resp = requests.request(r.method, r.scheme + "://" + r.host + r.uri, headers=r.headers, data=r.body)
print(resp.status_code, resp.reason)
print(resp.content)
