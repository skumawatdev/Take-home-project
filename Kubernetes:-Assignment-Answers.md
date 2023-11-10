# Kubernetes:-Assignment-Answers

**Que.1. What are different types of services?**
      Ans.  ClusterIP, NodePort, LoadBalancer, ExternalName, Headless, Ingress.

**Que.2. What is a pod?**
      Ans.  A Pod is the smallest deployable unit in Kubernetes, containing one or more tightly coupled containers that share network and storage resources.
      
**Que.3. Create a Pod with the above-created custom image; when a pod dies, Kubernetes should automatically restart.**
      Ans.   
           ![Capture](https://github.com/skumawatdev/Take-home-project/assets/60931208/3dcd93e7-dee5-499a-b0b4-0da9c0091d05)
           
           ![2](https://github.com/skumawatdev/Take-home-project/assets/60931208/af68ec1c-c056-42c4-ad85-b4c708e5d584)
           
           ![replica](https://github.com/skumawatdev/Take-home-project/assets/60931208/48ee8800-9b34-45e2-b6a2-6dd74531ac14)





**Que.4.How to access the custom application with a specific port?**
      Ans.  You can expose the application using a Service of type NodePort or LoadBalancer and specify the port in the Service configuration, 
      and it will map to the port in the Pod.

