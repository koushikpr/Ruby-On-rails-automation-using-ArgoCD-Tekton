# Ruby-On-rails-automation-using-ArgoCD-Tekton

This Project demonstrates how to deploy a Ruby on rails project Using ARgoCD and Tekton Dashboard


This is a comprehensive DevOps coding assessment that involves multiple steps and technologies, including Docker, Kubernetes, ArgoCD, and Tekton. Below, I'll outline how you can approach each step of the assessment.

Step 1: Docker
You will need to create a Dockerfile for a simple Ruby on Rails application with a PostgreSQL database running in separate containers. 

Step 2: Kubernetes
You will need to create a YAML file to deploy the Ruby on Rails application and PostgreSQL database using Kubernetes. Use Minikube or K3d for local Kubernetes clusters. You can set up a StatefulSet for PostgreSQL and create a Deployment for your Ruby on Rails application. Additionally, configure an Ingress or Service with your preferred ingress controller to expose the application.  apply them to your Kubernetes cluster using the kubectl apply -f command.

Step 3: ArgoCD
Create a private GitHub repository and store your Kubernetes manifest files and ArgoCD configuration in this repository. Create the necessary ArgoCD application.yaml file to define the application to deploy. Ensure you have argocd-cm and argocd-rbac-cm config maps properly configured. Also, include the config file to add the private GitHub repository as a source for ArgoCD. You can use ArgoCD to manage the deployment of your application using GitOps.
```
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

Access ArgoCD Dashboad
```
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d

```


Step 4: Tekton
Set up Tekton pipelines and the Tekton dashboard. Create a pipeline that fetches the source code from the public fork of your Ruby on Rails application, builds the Docker image, and pushes it to Docker Hub. You will also need to configure credentials for Docker Hub in the pipeline. After configuring your pipeline, manually run it from the Tekton dashboard to build and push the Docker image.

```
kubectl apply -f https://storage.googleapis.com/tekton-releases/pipeline/latest/release.notags.yaml
kubectl apply --filename https://github.com/tektoncd/dashboard/releases/latest/download/tekton-dashboard-release.yaml
kubectl create secret docker-registry docker-hub-secret \
  --docker-server=https://index.docker.io/v1/ \
  --docker-username=030902 \
  --docker-password=Removed \
  --docker-email=karanboltz@gmail.com

```
Access the Tekton Dashboard using the external IP or port-forwarding.
Create a new PipelineRun for your build-and-push-pipeline and specify the desired Git source, resource, and other parameters.
Manually trigger the PipelineRun from the Tekton Dashboard.
The pipeline will download the source code from your public forked repository, build the Docker image, and push it to Docker Hub using the specified Docker Hub secret.

